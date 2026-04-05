"""
Fetch all YC Library blog posts in parallel using Playwright.
Converts to markdown, writes to raw/posts/{slug}.md with YAML frontmatter.
"""

import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

from markdownify import markdownify as md
from playwright.async_api import async_playwright

CONCURRENT_PAGES = 10  # parallel browser tabs
BASE_URL = "https://www.ycombinator.com/library"
RAW_DIR = Path(__file__).parent.parent / "raw"


def slugify(text):
    """Convert title to filesystem-safe slug."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def clean_markdown(html):
    """Convert HTML to clean markdown."""
    markdown = md(html, heading_style="ATX", strip=['img', 'script', 'style', 'nav'])
    # Clean up excessive whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    # Remove any remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    return markdown.strip()


async def fetch_single_blog(page, blog_entry, results, semaphore):
    """Fetch a single blog post using a browser page."""
    slug = blog_entry['slug']
    title = blog_entry['title']
    url = f"{BASE_URL}/{slug}"

    async with semaphore:
        try:
            await page.goto(url, wait_until='networkidle', timeout=20000)

            # Extract content
            prose_el = await page.query_selector('[class*="prose"]')
            if not prose_el:
                # Fallback selectors
                for sel in ['article', 'main', '[class*="content"]']:
                    prose_el = await page.query_selector(sel)
                    if prose_el:
                        text = await prose_el.inner_text()
                        if len(text) > 300:
                            break

            if not prose_el:
                results.append({"slug": slug, "status": "no_content", "title": title})
                return

            html = await prose_el.inner_html()
            text = await prose_el.inner_text()

            if len(text) < 100:
                results.append({"slug": slug, "status": "too_short", "title": title})
                return

            # Convert to markdown
            content = clean_markdown(html)

            # Build frontmatter
            safe_title = title.replace('"', '\\"')
            author = blog_entry.get('author', 'Unknown')
            categories = json.dumps(blog_entry.get('categories', []))
            desc = blog_entry.get('description', '').replace('"', '\\"')
            frontmatter = f'---\nid: {slug}\ntitle: "{safe_title}"\ntype: post\nurl: {url}\nauthor: "{author}"\ncategories: {categories}\ndescription: "{desc}"\n---'

            # Write file
            out_path = RAW_DIR / "posts" / f"{slug}.md"
            out_path.write_text(f"{frontmatter}\n\n{content}", encoding="utf-8")

            results.append({
                "slug": slug,
                "status": "ok",
                "title": title,
                "chars": len(content),
                "words": len(content.split()),
            })
            print(f"  [{len([r for r in results if r['status'] == 'ok'])}/70] {title} ({len(content.split())} words)")

        except Exception as e:
            results.append({"slug": slug, "status": "error", "title": title, "error": str(e)})
            print(f"  [ERR] {title}: {e}")


async def main():
    # Load blog entries from sources
    with open(RAW_DIR / "_algolia_raw.json") as f:
        hits = json.load(f)

    blogs = [h for h in hits if h.get('media_type') == 'Blog']
    print(f"Fetching {len(blogs)} blog posts with {CONCURRENT_PAGES} parallel pages...\n")

    start = time.time()
    results = []
    semaphore = asyncio.Semaphore(CONCURRENT_PAGES)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # Create a pool of pages
        pages = []
        for _ in range(CONCURRENT_PAGES):
            ctx = await browser.new_context()
            page = await ctx.new_page()
            pages.append(page)

        # Process all blogs in parallel using the page pool
        tasks = []
        for i, blog in enumerate(blogs):
            page = pages[i % CONCURRENT_PAGES]
            task = asyncio.create_task(fetch_single_blog(page, blog, results, semaphore))
            tasks.append(task)

        await asyncio.gather(*tasks)
        await browser.close()

    elapsed = time.time() - start

    # Summary
    ok = [r for r in results if r['status'] == 'ok']
    errors = [r for r in results if r['status'] == 'error']
    no_content = [r for r in results if r['status'] == 'no_content']

    print(f"\n{'='*60}")
    print(f"Done in {elapsed:.1f}s")
    print(f"  Success: {len(ok)}")
    print(f"  Errors: {len(errors)}")
    print(f"  No content: {len(no_content)}")

    if ok:
        total_words = sum(r['words'] for r in ok)
        print(f"  Total words: {total_words:,}")
        print(f"  Avg words/post: {total_words // len(ok):,}")

    if errors:
        print(f"\nErrors:")
        for e in errors:
            print(f"  {e['title']}: {e['error']}")

    if no_content:
        print(f"\nNo content found:")
        for n in no_content:
            print(f"  {n['title']}")


if __name__ == "__main__":
    asyncio.run(main())
