---
name: radar-decision-log
description: Use when the user wants a timeline, history, decision log, or movement report for tech radar entries — for example "show the history of React on the radar", "decision log for terraform", "which techs moved last year", "generate an ADR index", "what changed between snapshots", or "build me a movement table". Reads radar/<date>/ snapshots, reconstructs the per-tech ring history across time, and emits a chronological decision log similar to an ADR index. Can scope to a single tech, a quadrant, or the whole radar. Trigger when the user asks about radar history or wants to see how decisions evolved.
---

# radar-decision-log

Reconstruct the temporal decision log for INFO tech radar entries.

## When this fires

- "What's the history of Terraform on the radar?"
- "Show me everything that moved into hold since 2023."
- "Generate the ADR index for the radar."
- "Which techs were added in 2024?"
- "Diff the last two snapshots."

## How to read snapshots

`radar/` contains dated dirs (`YYYY-MM-DD/`). Each dir holds *only the entries that were created or changed on that date*. To reconstruct a tech's history:

1. List every dated dir in chronological order.
2. For each tech (filename slug), find every snapshot that contains it.
3. Read frontmatter from each occurrence to capture `ring` over time.
4. The first occurrence = creation. Subsequent occurrences = ring changes or prose updates. The last occurrence = current state.

A tech that appears once and never again is still active — its state is whatever the last snapshot said.

## Modes

### Single-tech timeline

Input: one slug (e.g. `terraform`). Output: a table of every snapshot that touched it.

```markdown
## Terraform — decision log

| Date       | Ring  | Quadrant                  | Note |
|------------|-------|---------------------------|------|
| 2022-09-22 | trial | platforms-and-operations  | Added |
| 2022-12-05 | trial | platforms-and-operations  | Prose update |
| 2024-12-01 | adopt | platforms-and-operations  | Promoted |

**Current ring:** adopt (as of 2024-12-01)
```

If the user wants the *why*, also surface the supersession note or the diff of body text between consecutive entries.

### Quadrant or whole-radar movement report

Input: a date range, optionally a quadrant filter. Output: every ring change in that range.

```markdown
## Movement report — 2024-01-01 to 2025-01-22

### platforms-and-operations
- **Terraform**: trial → adopt (2024-12-01)
- **Pulumi**: → assess (2024-12-01, new)

### tools
- **React Testing Library**: → adopt (2025-01-22, new)
- **Cypress**: → hold (2024-12-01)
```

Group by quadrant; within a quadrant, order by snapshot date then alphabetical.

### ADR index

Input: none. Output: a flat list of every entry with its current ring, sorted by quadrant, formatted like an ADR index. Useful as a published-artifact rendering of the radar.

```markdown
## INFO Tech Radar — Decision Index

### Languages & Frameworks
- [React](/languages-and-frameworks/react) — adopt (since 2020-09-01, last touched 2023-03-01)
- ...

### Methods & Patterns
- ...
```

## Procedure

1. Confirm scope: single tech / quadrant / whole radar / date range.
2. Run `scripts/scan_radar.py` (bundled with this skill, mirrored from `radar-entry-audit`) to get a JSON index. It already builds `slug → [(date, ring, quadrant, ...), ...]` for you — no need to re-walk the tree in the conversation.

   ```bash
   # Whole-radar dump:
   python3 .claude/skills/radar-decision-log/scripts/scan_radar.py --root radar > /tmp/radar.json

   # Single tech:
   python3 .claude/skills/radar-decision-log/scripts/scan_radar.py --slug terraform
   ```

3. Use the JSON's `entries.<slug>` for timelines and `current` for "what's the current ring".
4. Render the requested view.
5. If the user asks for *why* a transition happened, read the supersession note (if any) from the entry on that date, or diff the body against the previous occurrence. Note: the repo's idiomatic move-style is prose, not a `> **Status:**` blockquote — so look at the opening paragraph of the new entry, not just metadata.

## Output rules

- Always include the date a transition happened — the radar's value is the timeline, not just the current state.
- For "current ring", trust the most recent snapshot containing the slug.
- If a slug appears in only one snapshot, label it "Added <date>" and use that ring as current.
- Don't infer a "removed" status from absence — the radar doesn't model deletion. If a tech genuinely should be removed, that's a `hold` entry, not a missing file.

## Anti-patterns

- Don't assume snapshots are full re-statements. They aren't — they're differential. Reading only the latest snapshot misses every tech that hasn't changed recently.
- Don't sort by file path. Always sort by snapshot date for timelines.
- Don't generate the report by hand for large scans. Script it.
