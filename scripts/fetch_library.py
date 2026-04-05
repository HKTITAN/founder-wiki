"""
Fetch the complete YC Library catalog from Algolia.
Outputs raw/_sources.json with metadata for all entries.
"""

import json
import requests
import sys

APP_ID = "45BWZJ1SGC"
# Secured API key from ycombinator.com/library page source
API_KEY = "MDlkNDAyNzM1YjA2YTQwYjBkMGIwNjk2Mzg4NDQ3ZGRkMTdhZWJmODM0MDdiNDVhMTNlNDRiYzFlOGZiMGI5MmFuYWx5dGljc1RhZ3M9eWNkYyUyQ2xpYnJhcnkmcmVzdHJpY3RJbmRpY2VzPUxpYnJhcnlfYm9va2ZhY2VfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTJDJTVCJTIya2Jfcm9vdF8xNzYlMjIlMkMlMjJrYl9yb290XzkxMiUyMiU1RCU1RA=="
INDEX = "Library_bookface_production"

SEARCH_URL = f"https://{APP_ID}-dsn.algolia.net/1/indexes/{INDEX}/browse"


def fetch_all():
    """Browse the entire Algolia index, paginating with cursors."""
    headers = {
        "X-Algolia-Application-Id": APP_ID,
        "X-Algolia-API-Key": API_KEY,
        "Content-Type": "application/json",
    }

    all_hits = []
    cursor = None
    page = 0

    while True:
        params = {"hitsPerPage": 1000}
        if cursor:
            params["cursor"] = cursor

        resp = requests.post(SEARCH_URL, headers=headers, json={"params": "&".join(f"{k}={v}" for k, v in params.items())})

        if resp.status_code != 200:
            # Try GET-based browse
            get_url = f"https://{APP_ID}-dsn.algolia.net/1/indexes/{INDEX}/browse"
            get_params = {"hitsPerPage": 1000}
            if cursor:
                get_params["cursor"] = cursor
            resp = requests.get(get_url, headers=headers, params=get_params)

        if resp.status_code != 200:
            print(f"Error: {resp.status_code} {resp.text[:500]}")
            # Fall back to search endpoint
            break

        data = resp.json()
        hits = data.get("hits", [])
        all_hits.extend(hits)
        page += 1
        print(f"Page {page}: {len(hits)} hits (total: {len(all_hits)})")

        cursor = data.get("cursor")
        if not cursor or not hits:
            break

    return all_hits


def fetch_via_search():
    """Fallback: use search endpoint with empty query, paginating."""
    headers = {
        "X-Algolia-Application-Id": APP_ID,
        "X-Algolia-API-Key": API_KEY,
        "Content-Type": "application/json",
    }

    all_hits = []
    page = 0
    hits_per_page = 100

    while True:
        body = {
            "query": "",
            "hitsPerPage": hits_per_page,
            "page": page,
        }

        url = f"https://{APP_ID}-dsn.algolia.net/1/indexes/{INDEX}/query"
        resp = requests.post(url, headers=headers, json=body)

        if resp.status_code != 200:
            print(f"Error on page {page}: {resp.status_code} {resp.text[:500]}")
            break

        data = resp.json()
        hits = data.get("hits", [])
        total = data.get("nbHits", "?")
        all_hits.extend(hits)
        print(f"Page {page}: {len(hits)} hits (total so far: {len(all_hits)} / {total})")

        if len(hits) < hits_per_page:
            break
        page += 1

        if page > 50:  # safety
            break

    return all_hits


def extract_metadata(hit):
    """Extract clean metadata from an Algolia hit."""
    return {
        "id": hit.get("objectID", ""),
        "title": hit.get("title", ""),
        "slug": hit.get("slug", ""),
        "type": hit.get("type", hit.get("content_type", "")),
        "url": hit.get("url", ""),
        "authors": hit.get("authors", []),
        "topics": hit.get("topics", hit.get("tags", [])),
        "date": hit.get("date", hit.get("created_at", "")),
        "description": hit.get("description", hit.get("summary", "")),
        "youtube_url": hit.get("youtube_url", hit.get("video_url", "")),
        "body": hit.get("body", hit.get("content", "")),
        "_raw_keys": list(hit.keys()),  # keep track of available fields
    }


def main():
    print("Attempting browse endpoint...")
    hits = fetch_all()

    if not hits:
        print("Browse failed, trying search endpoint...")
        hits = fetch_via_search()

    if not hits:
        print("No hits found. Check API key.")
        sys.exit(1)

    # Extract metadata
    sources = [extract_metadata(h) for h in hits]

    # Separate by type
    types = {}
    for s in sources:
        t = s["type"]
        types[t] = types.get(t, 0) + 1

    print(f"\nTotal: {len(sources)} entries")
    print(f"Types: {json.dumps(types, indent=2)}")

    # Save raw hits for debugging
    with open("raw/_algolia_raw.json", "w") as f:
        json.dump(hits, f, indent=2, default=str)

    # Save clean sources
    with open("raw/_sources.json", "w") as f:
        json.dump(sources, f, indent=2, default=str)

    # Print a sample
    if sources:
        print(f"\nSample entry keys: {sources[0]['_raw_keys']}")
        print(f"Sample title: {sources[0]['title']}")
        print(f"Sample type: {sources[0]['type']}")
        print(f"Sample url: {sources[0]['url']}")

    # Print first 3 full samples
    print("\n--- First 3 entries ---")
    for s in sources[:3]:
        print(json.dumps({k: v for k, v in s.items() if k != '_raw_keys' and v}, indent=2))
        print()


if __name__ == "__main__":
    main()
