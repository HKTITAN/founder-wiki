"""
Fetch all YC Library blog posts — v3 with images and dates.
- Preserves images: downloads locally and rewrites URLs to local paths
- Extracts publication dates from page content / meta tags
- Preserves all hyperlinks
- Idempotent: safe to re-run
"""

import asyncio
import hashlib
import json
import os
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
from markdownify import markdownify as md
from playwright.async_api import async_playwright

CONCURRENT = 5
BASE_URL = "https://www.ycombinator.com/library"
RAW_DIR = Path(__file__).parent.parent / "raw"
POSTS_DIR = RAW_DIR / "posts"
IMAGES_DIR = POSTS_DIR / "images"

# Shared httpx client for image downloads
http_client: httpx.AsyncClient | None = None


def clean_markdown(html: str) -> str:
    """Convert HTML to markdown, preserving images and links."""
    markdown = md(html, heading_style="ATX", strip=["script", "style", "nav"])
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    # Strip any remaining HTML tags EXCEPT img (shouldn't be any after markdownify)
    markdown = re.sub(r"<(?!img\b)[^>]+>", "", markdown)
    return markdown.strip()


async def download_image(url: str, slug: str) -> str | None:
    """Download an image and return the local relative path, or None on failure."""
    global http_client
    try:
        # Determine file extension from URL
        parsed = urlparse(url)
        path_part = parsed.path
        ext = Path(path_part).suffix.lower()
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif"):
            ext = ".png"  # fallback

        # Use content hash for filename to deduplicate
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        filename = f"{url_hash}{ext}"

        slug_dir = IMAGES_DIR / slug
        slug_dir.mkdir(parents=True, exist_ok=True)
        local_path = slug_dir / filename

        if local_path.exists() and local_path.stat().st_size > 0:
            # Already downloaded — idempotent
            return f"images/{slug}/{filename}"

        resp = await http_client.get(url, follow_redirects=True, timeout=15)
        if resp.status_code == 200 and len(resp.content) > 0:
            local_path.write_bytes(resp.content)
            return f"images/{slug}/{filename}"
        return None
    except Exception:
        return None


async def rewrite_images_in_markdown(markdown_text: str, slug: str, page_url: str) -> str:
    """Find markdown images and download them, rewriting URLs to local paths."""
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    matches = list(img_pattern.finditer(markdown_text))
    if not matches:
        return markdown_text

    # Download all images concurrently
    async def process_match(m):
        alt = m.group(1)
        src = m.group(2).strip()
        # Skip data URIs (e.g. base64 YC logo)
        if src.startswith("data:"):
            return m.group(0), None  # mark for removal
        # Make absolute URL
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = urljoin("https://www.ycombinator.com", src)
        elif not src.startswith("http"):
            src = urljoin(page_url, src)

        local_path = await download_image(src, slug)
        if local_path:
            return m.group(0), f"![{alt}]({local_path})"
        else:
            # Keep original URL if download fails
            return m.group(0), m.group(0)

    replacements = await asyncio.gather(*[process_match(m) for m in matches])

    for original, replacement in replacements:
        if replacement is None:
            # Remove data URI images entirely
            markdown_text = markdown_text.replace(original, "", 1)
        else:
            markdown_text = markdown_text.replace(original, replacement, 1)

    return markdown_text


async def extract_date(page) -> str | None:
    """Try to extract publication date from the page."""
    # Strategy 1: look for meta tags
    for meta_name in [
        'meta[property="article:published_time"]',
        'meta[name="date"]',
        'meta[name="publish-date"]',
        'meta[property="og:article:published_time"]',
    ]:
        el = await page.query_selector(meta_name)
        if el:
            content = await el.get_attribute("content")
            if content:
                # Parse ISO date
                m = re.match(r"(\d{4}-\d{2}-\d{2})", content)
                if m:
                    return m.group(1)
                m = re.match(r"(\d{4})", content)
                if m:
                    return content[:10] if len(content) >= 10 else content

    # Strategy 2: look for visible date text on the page
    # Common selectors for date elements
    for selector in [
        "time",
        '[class*="date"]',
        '[class*="Date"]',
        '[class*="published"]',
        '[class*="timestamp"]',
        '[data-testid*="date"]',
    ]:
        el = await page.query_selector(selector)
        if el:
            text = (await el.inner_text()).strip()
            parsed = parse_date_text(text)
            if parsed:
                return parsed
            # Also check datetime attribute
            dt = await el.get_attribute("datetime")
            if dt:
                m = re.match(r"(\d{4}-\d{2}-\d{2})", dt)
                if m:
                    return m.group(1)

    # Strategy 3: look for date patterns in the prose area or nearby
    # Get text from around the title area
    for selector in [
        '[class*="prose"]',
        "article",
        "main",
    ]:
        el = await page.query_selector(selector)
        if el:
            text = await el.inner_text()
            # Look for date patterns in first ~500 chars
            snippet = text[:500]
            parsed = parse_date_text(snippet)
            if parsed:
                return parsed

    # Strategy 4: scan the full page text for date patterns
    body = await page.query_selector("body")
    if body:
        full_text = await body.inner_text()
        # Look in first 2000 chars for date patterns
        parsed = parse_date_text(full_text[:2000])
        if parsed:
            return parsed

    return None


MONTH_MAP = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "jun": "06", "jul": "07", "aug": "08", "sep": "09",
    "oct": "10", "nov": "11", "dec": "12",
}


def parse_date_text(text: str) -> str | None:
    """Try to parse a date from free text. Returns YYYY-MM-DD or YYYY-MM."""
    # "Month DD, YYYY" or "Month YYYY"
    m = re.search(
        r"\b(January|February|March|April|May|June|July|August|September|October|November|December)"
        r"\s+(\d{1,2}),?\s+(\d{4})\b",
        text,
        re.IGNORECASE,
    )
    if m:
        month = MONTH_MAP[m.group(1).lower()]
        day = m.group(2).zfill(2)
        year = m.group(3)
        if 2000 <= int(year) <= 2030:
            return f"{year}-{month}-{day}"

    # "Month YYYY" without day
    m = re.search(
        r"\b(January|February|March|April|May|June|July|August|September|October|November|December)"
        r"\s+(\d{4})\b",
        text,
        re.IGNORECASE,
    )
    if m:
        month = MONTH_MAP[m.group(1).lower()]
        year = m.group(2)
        if 2000 <= int(year) <= 2030:
            return f"{year}-{month}"

    # "DD Mon YYYY" or "DD Month YYYY"
    m = re.search(
        r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})\b",
        text,
        re.IGNORECASE,
    )
    if m:
        day = m.group(1).zfill(2)
        month = MONTH_MAP[m.group(2).lower()[:3]]
        year = m.group(3)
        if 2000 <= int(year) <= 2030:
            return f"{year}-{month}-{day}"

    # YYYY-MM-DD
    m = re.search(r"\b(\d{4})-(\d{2})-(\d{2})\b", text)
    if m and 2000 <= int(m.group(1)) <= 2030:
        return m.group(0)

    # MM/DD/YYYY
    m = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", text)
    if m and 2000 <= int(m.group(3)) <= 2030:
        return f"{m.group(3)}-{m.group(1).zfill(2)}-{m.group(2).zfill(2)}"

    return None


async def fetch_one(browser, blog, semaphore):
    slug = blog["slug"]
    title = blog["title"]
    url = f"{BASE_URL}/{slug}"

    async with semaphore:
        ctx = await browser.new_context()
        page = await ctx.new_page()
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)

            # Extract date before looking at prose
            date = await extract_date(page)

            prose = await page.query_selector('[class*="prose"]')
            if not prose:
                await ctx.close()
                return {"slug": slug, "title": title, "status": "no_content", "date": date}

            html = await prose.inner_html()
            text = await prose.inner_text()

            if len(text) < 50:
                await ctx.close()
                return {"slug": slug, "title": title, "status": "too_short", "date": date}

            content = clean_markdown(html)

            # Download images and rewrite URLs
            content = await rewrite_images_in_markdown(content, slug, url)

            author = blog.get("author", "Unknown")
            categories = json.dumps(blog.get("categories", []))
            desc = (blog.get("description") or "").replace('"', '\\"')
            safe_title = (title or "").replace('"', '\\"')

            date_line = f'\ndate: "{date}"' if date else ""
            frontmatter = (
                f"---\n"
                f"id: {slug}\n"
                f'title: "{safe_title}"\n'
                f"type: post\n"
                f"url: {url}\n"
                f'author: "{author}"\n'
                f"categories: {categories}{date_line}\n"
                f'description: "{desc}"\n'
                f"---"
            )

            out_path = POSTS_DIR / f"{slug}.md"
            out_path.write_text(f"{frontmatter}\n\n{content}", encoding="utf-8")

            await ctx.close()
            return {
                "slug": slug,
                "title": title,
                "status": "ok",
                "date": date,
                "words": len(content.split()),
                "chars": len(content),
            }

        except Exception as e:
            await ctx.close()
            return {"slug": slug, "title": title, "status": "error", "error": str(e)}


async def main():
    global http_client

    with open(RAW_DIR / "_algolia_raw.json") as f:
        hits = json.load(f)

    blogs = [h for h in hits if h.get("media_type") == "Blog"]
    print(f"Fetching {len(blogs)} blogs with images+dates ({CONCURRENT} concurrent)...\n")

    # Ensure directories exist
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    start = time.time()
    semaphore = asyncio.Semaphore(CONCURRENT)

    async with httpx.AsyncClient() as client:
        http_client = client
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            tasks = [fetch_one(browser, b, semaphore) for b in blogs]
            results = await asyncio.gather(*tasks)
            await browser.close()

    elapsed = time.time() - start
    ok = [r for r in results if r["status"] == "ok"]
    errors = [r for r in results if r["status"] == "error"]
    no_content = [r for r in results if r["status"] == "no_content"]
    with_date = [r for r in results if r.get("date")]

    print(f"\nDone in {elapsed:.1f}s")
    print(f"  Success: {len(ok)}")
    print(f"  Errors: {len(errors)}")
    print(f"  No content: {len(no_content)}")
    print(f"  With dates: {len(with_date)}")
    if ok:
        total_words = sum(r["words"] for r in ok)
        print(f"  Total words: {total_words:,}")

    for r in ok:
        date_str = r.get("date", "no date")
        print(f"  [{r['words']:5d}w] [{date_str}] {r['title']}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  {e['title']}: {e['error']}")

    if no_content:
        print("\nNo content:")
        for r in no_content:
            print(f"  {r['title']}")


if __name__ == "__main__":
    asyncio.run(main())
