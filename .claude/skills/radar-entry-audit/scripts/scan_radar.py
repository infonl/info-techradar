#!/usr/bin/env python3
"""
scan_radar.py — walk radar/<YYYY-MM-DD>/<slug>.md, parse frontmatter, emit JSON.

Designed to be shared by radar-entry-audit and radar-decision-log. Reading the
whole tree once and emitting a structured index avoids each skill reinventing
the file walk + frontmatter parser.

Output shape:

{
  "snapshots": ["2020-09-01", ...],          # chronological
  "entries": {                               # one record per (date, slug)
    "react": [
      {"date": "2020-09-01", "ring": "adopt", "quadrant": "...", "title": "...",
       "featured": true, "path": "radar/2020-09-01/react.md",
       "body_chars": 1234, "internal_links": ["/tools/vitest/", ...]},
      ...
    ]
  },
  "current": {                               # latest occurrence per slug
    "react": {"date": "...", "ring": "...", "quadrant": "...", "path": "..."}
  }
}

Usage:
    python scan_radar.py [--root radar/] [--quadrant tools]
    # prints JSON to stdout
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK_RE = re.compile(r"\]\((/[a-z0-9-]+/[a-z0-9-]+/?)\)")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)

VALID_RINGS = {"adopt", "trial", "assess", "hold"}
VALID_QUADRANTS = {
    "languages-and-frameworks", "methods-and-patterns",
    "platforms-and-operations", "tools",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm_text, body = m.groups()
    fm: dict = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip().strip('"').strip("'")
        if v in ("true", "false"):
            v = v == "true"
        fm[k.strip()] = v
    return fm, body


def scan(root: Path) -> dict:
    snapshots = sorted(
        p.name for p in root.iterdir() if p.is_dir() and DATE_RE.match(p.name)
    )
    entries: dict[str, list[dict]] = {}
    for date in snapshots:
        for md in sorted((root / date).glob("*.md")):
            slug = md.stem
            text = md.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(text)
            entries.setdefault(slug, []).append({
                "date": date,
                "slug": slug,
                "ring": fm.get("ring"),
                "quadrant": fm.get("quadrant"),
                "title": fm.get("title"),
                "featured": fm.get("featured"),
                "path": str(md),
                "body_chars": len(body.strip()),
                "internal_links": LINK_RE.findall(body),
            })
    current = {
        slug: occurrences[-1]
        for slug, occurrences in entries.items()
    }
    return {"snapshots": snapshots, "entries": entries, "current": current}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="radar", type=Path)
    ap.add_argument("--quadrant", help="filter current entries by quadrant")
    ap.add_argument("--slug", help="dump only this slug's history")
    args = ap.parse_args()

    if not args.root.is_dir():
        print(f"error: {args.root} not a directory", file=sys.stderr)
        return 1

    data = scan(args.root)

    if args.slug:
        data = {"slug": args.slug, "history": data["entries"].get(args.slug, [])}
    elif args.quadrant:
        data["current"] = {
            slug: rec for slug, rec in data["current"].items()
            if rec.get("quadrant") == args.quadrant
        }

    json.dump(data, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
