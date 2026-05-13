---
name: radar-entry-audit
description: Use when the user wants to review, audit, lint, or quality-check radar entries — for example "audit the radar", "review my radar entries", "check the radar for issues", "are these entries ADR-compliant", "find broken links in the radar", "which entries are missing rationale", or after a batch of new entries has been added. Scans markdown files under radar/ and reports on frontmatter completeness, ADR-shape rationale (context / decision / consequences), internal-link integrity, slug/title consistency, and orphan entries (present in old snapshots but never updated). Also flags entries that read like marketing rather than decisions. Trigger proactively after radar-entry-new or radar-entry-move runs.
---

# radar-entry-audit

Lint INFO tech radar entries against ADR-style quality criteria.

## When this fires

- "Audit the radar."
- "Review the latest snapshot."
- "Are there broken links in radar/?"
- "Which entries are missing a rationale?"
- After bulk additions or before publishing.

## What "good" looks like

A good radar entry is a small ADR. It has:

1. **Complete frontmatter** — `title` (quoted), `ring` (one of adopt/trial/assess/hold), `quadrant` (one of the four ids), `featured` (bool).
2. **A decision, not a description** — the body explains *why we chose this here*, not just what the tech does.
3. **Consequences captured** — a "Considerations at INFO" (or equivalent) section noting trade-offs, current focus, or constraints.
4. **Working internal links** — links of the form `/[quadrant]/[slug]/` resolve to a file under some `radar/*/<slug>.md`.
5. **Slug ↔ title coherence** — filename slug clearly matches the `title` field.

## Audit dimensions

Run these checks across all entries (or a user-specified subset like "the latest snapshot only"):

### 1. Frontmatter
- Missing fields → flag.
- `ring` outside the allowed set → flag.
- `quadrant` outside the allowed set → flag.
- Title not quoted, or empty → flag.

### 2. ADR shape
- Body shorter than ~80 words → likely a stub. Flag with severity *info* (some legitimate stubs exist, e.g. `superblocks.md`).
- No "why" framing — no occurrence of words like "because", "we decided", "in the context", "current focus", "considerations" — flag as *missing rationale*.
- Reads like marketing — heavy use of "powerful", "seamless", "best-in-class" without concrete INFO context — flag as *too promotional*.

### 3. Internal links
- For each `[text](/quadrant/slug/)` or `[text](/quadrant/slug)` link in the body:
  - `quadrant` segment must be one of the four valid quadrant ids.
  - At least one file `radar/*/<slug>.md` must exist.
- External links (http/https) — optionally check, but don't block on flakiness.

### 4. Cross-snapshot coherence
- For each slug, find every snapshot containing it. The latest occurrence is the "current" entry.
- If an entry's `featured: true` but the tech only appears in snapshots older than ~2 years → flag *possibly stale*.
- If an entry was moved to `hold` and a newer entry replaces it without a supersession note → flag *missing supersession link*.

### 5. Slug / title
- Slug should be the kebab-case lowercase form of the title (allowing for minor abbreviations like "and" → "and", "&" handled). Mismatches like `title: "Postgres"` in `postgresql.md` → flag.

## Procedure

1. Decide scope. Default = all entries under `radar/`. If the user names a snapshot, restrict to that dir.
2. Run `scripts/scan_radar.py` (bundled with this skill) to get a JSON index of every entry — frontmatter, body length, internal links, current ring per slug. Don't re-parse files one-by-one in the conversation; pipe the JSON through `jq`/Python for the actual checks. The script is also shared with `radar-decision-log` so the two skills produce comparable indices.

   ```bash
   python3 .claude/skills/radar-entry-audit/scripts/scan_radar.py --root radar > /tmp/radar.json
   ```

   The output's `current` map is what you want for "is this the latest entry for the slug"; the per-slug `entries` list is the history.
3. Group findings by severity:
   - **Error** — frontmatter invalid, broken internal link.
   - **Warning** — missing rationale, missing supersession note.
   - **Info** — short stubs, possibly stale, slug/title mismatch.
4. Report as a table grouped by file. For each finding give: file path, dimension, what's wrong, suggested fix. Keep it scannable.
5. Offer to auto-fix the trivial ones (frontmatter quoting, slug case) but ask before editing.

## Output shape

```markdown
## Radar audit — <scope>, <N> entries

### Errors (must fix)
| File | Issue | Fix |
| ---- | ----- | --- |
| radar/.../foo.md | ring "adopted" not in {adopt,trial,assess,hold} | change to `adopt` |

### Warnings
...

### Info
...

### Summary
- Errors: X
- Warnings: Y
- Info: Z
```

## Anti-patterns

- Don't auto-rewrite prose. "Reads like marketing" is a flag, not a fix — surface it, let a human rephrase.
- Don't enforce a strict template on body sections. The "Why X / Considerations at INFO" pattern is common but not universal; allow Nygard-sentence entries (see `radar/2020-09-01/react.md`).
- Don't treat `featured: false` as a defect. Some entries are deliberately unfeatured (industry givens).
