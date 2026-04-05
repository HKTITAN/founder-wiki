"""
Fetch all YC Library blog posts — fixed version with isolated browser contexts.
Each page gets its own context to prevent content cross-contamination.
"""

import asyncio
import json
import os
import re
import time
from pathlib import Path

from markdownify import markdownify as md
from playwright.async_api import async_playwright

CONCURRENT = 5  # fewer but fully isolated
BASE_URL = "https://www.ycombinator.com/library"
RAW_DIR = Path(__file__).parent.parent / "raw"


def clean_markdown(html):
    markdown = md(html, heading_style="ATX", strip=['img', 'script', 'style', 'nav'])
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = re.sub(r'<[^>]+>', '', markdown)
    return markdown.strip()


async def fetch_one(browser, blog, semaphore):
    slug = blog['slug']
    title = blog['title']
    url = f"{BASE_URL}/{slug}"

    async with semaphore:
        # Each fetch gets its OWN context and page — fully isolated
        ctx = await browser.new_context()
        page = await ctx.new_page()
        try:
            await page.goto(url, wait_until='networkidle', timeout=20000)

            prose = await page.query_selector('[class*="prose"]')
            if not prose:
                await ctx.close()
                return {"slug": slug, "title": title, "status": "no_content"}

            html = await prose.inner_html()
            text = await prose.inner_text()

            if len(text) < 50:
                await ctx.close()
                return {"slug": slug, "title": title, "status": "too_short"}

            content = clean_markdown(html)
            author = blog.get('author', 'Unknown')
            categories = json.dumps(blog.get('categories', []))
            desc = blog.get('description', '').replace('"', '\\"')
            safe_title = title.replace('"', '\\"')

            frontmatter = (
                f'---\n'
                f'id: {slug}\n'
                f'title: "{safe_title}"\n'
                f'type: post\n'
                f'url: {url}\n'
                f'author: "{author}"\n'
                f'categories: {categories}\n'
                f'description: "{desc}"\n'
                f'---'
            )

            out_path = RAW_DIR / "posts" / f"{slug}.md"
            out_path.write_text(f"{frontmatter}\n\n{content}", encoding="utf-8")

            await ctx.close()
            return {
                "slug": slug, "title": title, "status": "ok",
                "words": len(content.split()), "chars": len(content),
            }

        except Exception as e:
            await ctx.close()
            return {"slug": slug, "title": title, "status": "error", "error": str(e)}


async def main():
    with open(RAW_DIR / "_algolia_raw.json") as f:
        hits = json.load(f)

    blogs = [h for h in hits if h.get('media_type') == 'Blog']
    print(f"Re-fetching {len(blogs)} blogs with isolated contexts ({CONCURRENT} concurrent)...\n")

    start = time.time()
    semaphore = asyncio.Semaphore(CONCURRENT)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [fetch_one(browser, b, semaphore) for b in blogs]
        results = await asyncio.gather(*tasks)
        await browser.close()

    elapsed = time.time() - start
    ok = [r for r in results if r['status'] == 'ok']
    errors = [r for r in results if r['status'] == 'error']
    no_content = [r for r in results if r['status'] == 'no_content']

    print(f"\nDone in {elapsed:.1f}s")
    print(f"  Success: {len(ok)}")
    print(f"  Errors: {len(errors)}")
    print(f"  No content: {len(no_content)}")
    if ok:
        total_words = sum(r['words'] for r in ok)
        print(f"  Total words: {total_words:,}")

    for r in ok:
        print(f"  [{r['words']:5d}w] {r['title']}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  {e['title']}: {e['error']}")


if __name__ == "__main__":
    asyncio.run(main())
