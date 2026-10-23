"""Fetch the Google Scholar citation count and write it for the homepage badge.

Run by .github/workflows/google_scholar_crawler.yaml once a day. Writes
  results/gs_data.json            citations / h-index / i10-index and the fetch time
  results/gs_data_shieldsio.json  shields.io endpoint JSON used by the badge in _pages/about.md
Exits non-zero if the numbers cannot be fetched, so the workflow keeps the last good data.
"""
import json
import os
import sys
from datetime import datetime, timezone

from scholarly import scholarly

author_id = os.environ["GOOGLE_SCHOLAR_ID"]
author = scholarly.search_author_id(author_id)
scholarly.fill(author, sections=["basics", "indices"])
citations = author.get("citedby")
if not citations:
    sys.exit(f"no citation count returned for {author_id}")

os.makedirs("results", exist_ok=True)
data = {
    "name": author.get("name"),
    "citedby": citations,
    "hindex": author.get("hindex"),
    "i10index": author.get("i10index"),
    "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
}
json.dump(data, open("results/gs_data.json", "w"), indent=2)
json.dump({"schemaVersion": 1, "label": "citations", "message": str(citations)},
          open("results/gs_data_shieldsio.json", "w"))
print(json.dumps(data))
