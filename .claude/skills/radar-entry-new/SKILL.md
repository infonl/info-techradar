---
name: radar-entry-new
description: Use when the user wants to add a new technology to the INFO tech radar, propose a new entry, draft a radar item, capture a tech decision in ADR style, or asks "add X to the radar", "create radar entry for Y", "propose Z for assess/trial/adopt/hold". Scaffolds a markdown file in the latest dated snapshot under radar/ with correct frontmatter (title, ring, quadrant, featured) and an ADR-shaped body (context, decision, considerations at INFO, consequences). Cross-links related entries by quadrant slug. Trigger this skill whenever a tech radar entry needs to be created, even if the user phrases it as "we decided to use X" or "let's evaluate Y".
---

# radar-entry-new

Scaffold a new INFO tech radar entry as an ADR-style decision record.

## When this fires

- "Add React Testing Library to the radar"
- "We're adopting Vitest, write the entry"
- "Propose Pulumi for assess"
- "Draft a hold entry for Snowflake"
- The user describes a tooling/language/platform/method choice that should be recorded.

## Repo conventions

Each radar entry is `radar/<YYYY-MM-DD>/<slug>.md`. Snapshots are *differential* — an entry is only re-written into a new dated dir when its ring or prose changes. The latest dated dir under `radar/` is the active snapshot; if no snapshot exists for today, ask the user whether to add to the most recent snapshot or create a new one (use today's date `YYYY-MM-DD`).

**Quadrants** (from `config.json`):
- `languages-and-frameworks`
- `methods-and-patterns`
- `platforms-and-operations`
- `tools`

**Rings**: `adopt`, `trial`, `assess`, `hold`.

**Slug**: lowercase, hyphenated, derived from title. Match how it would render in the URL `/<quadrant>/<slug>/`.

## Frontmatter

```yaml
---
title: "Display Name"
ring: adopt | trial | assess | hold
quadrant: languages-and-frameworks | methods-and-patterns | platforms-and-operations | tools
featured: true | false
---
```

`featured: true` for entries that should surface on the landing page. Default `true` for new entries unless the user says otherwise or the tech is already widely assumed (see `radar/2023-03-01/react.md` for an example of `featured: false` on a "given").

## Body — ADR shape

Existing entries follow a Nygard-style decision sentence. Use this skeleton; adapt prose so it reads naturally rather than like a template.

```markdown
[Optional one-line link/intro: [Tech](https://...) is a short description.]

### Why [Tech]?

- **Bullet 1:** the leading benefit, plain language.
- **Bullet 2:** secondary benefit.
- **Bullet 3:** integration / fit with existing stack — link to related radar entries via `/[quadrant-id]/[slug]/`.

### Considerations at INFO

- Adoption context — who is using it, on what projects.
- Trade-offs we explicitly accept.
- **Current Focus:** what we're doing with it now.

[Closing sentence: one-line restatement of the decision and its purpose.]
```

For deeper "decision sentence" entries (see `radar/2020-09-01/react.md`), open with:

> In the context of [need], facing [alternatives], we decided for [Tech] and neglected [rejected options], to achieve [goal], accepting [trade-off], because [reason].

Use this longer form when the decision rejects specific alternatives. Use the bulleted form when adopting an additive tool.

## Internal linking

Whenever you mention another tech that already exists in the radar, link it as `/[quadrant-id]/[slug]/`. Find existing entries by checking `radar/*/` for a matching filename. Trailing slash is *inconsistent in the repo* — both `/tools/vitest/` and `/tools/playwright` exist in production entries. Either is fine; pick one form and stay consistent inside a single file.

To discover related entries quickly, run `scripts/scan_radar.py` (bundled in `radar-entry-audit` and `radar-decision-log`) — its `--quadrant <id>` output lists every current slug in that quadrant. Use it to pick the 1–3 most relevant cross-links.

## Formatting conventions to match

These are repo conventions, not style preferences — match them or the new entry visually clashes with neighbouring files:

- **Quote the title.** `title: "Vitest"` not `title: Vitest`.
- **Blank line between bullet items** in the body. Existing entries (`cypress.md`, `playwright.md`, `snowflake.md`) use paragraph-style bullets:

  ```markdown
  - **Speed:** first benefit prose.

  - **DX:** second benefit prose.
  ```

  Not tight bullets. The blank line is intentional — it's how the radar's markdown renderer breathes.
- **Open with a one-line external link sentence**: `` `[Tech](https://…) is a short description.` `` Then the `### Why X?` heading. See any entry under `radar/2024-12-01/` for the pattern.
- **Close with a one-sentence restatement** of the decision (most entries do this — it reads as the "so what" line).
- **Don't add a `tags:` field.** The radar derives tags from quadrant + filename, not frontmatter.

## Procedure

1. Confirm with the user (if not already given): title, ring, quadrant, featured.
2. Determine target snapshot dir. Default = latest `radar/<date>/`. If user wants a fresh snapshot or it's been months, ask before creating a new dated dir.
3. Compute slug. Verify no clash: if `radar/*/<slug>.md` exists, this is a *move*, not a new entry — hand off to `radar-entry-move` instead.
4. Draft body. Reuse the user's words for rationale where possible — don't invent justifications.
5. Cross-link 1–3 related radar entries. Look in the latest snapshot and earlier ones for matching slugs.
6. Write the file. Show the user the result; do not commit unless asked.

## Output checklist

- [ ] Frontmatter has title (quoted), ring, quadrant, featured. No stray fields (no `tags:`, no `date:`).
- [ ] Slug filename matches the title's kebab-case form.
- [ ] At least one "Why" bullet and one "Considerations at INFO" bullet.
- [ ] Bullets separated by blank lines (paragraph-bullet style).
- [ ] Internal links use `/[quadrant]/[slug]` form, consistent within the file.
- [ ] No invented rationale — everything ties back to what the user said or to facts about the tech.

## Anti-patterns

- Don't write marketing prose. The radar is a decision log, not a brochure.
- Don't list every feature of the tech. Focus on *why this, why now, here at INFO*.
- Don't add `featured: true` to a tech that's already an industry default — set `false` and note "this is now a given" in the body, like `react.md` in 2023-03-01.
