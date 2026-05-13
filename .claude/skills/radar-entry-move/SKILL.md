---
name: radar-entry-move
description: Use when a tech radar entry needs to change ring (adopt/trial/assess/hold), be promoted, demoted, deprecated, or superseded — for example "move Terraform from trial to adopt", "demote X to hold", "we're dropping Y", "Z is now adopted", "supersede the old entry", or "update the ring for ...". Creates an updated copy of the entry in a new or current dated snapshot under radar/, preserving the prior entry untouched (snapshots are immutable history) and adding a supersession note that links back to the previous decision. Trigger whenever a radar entry's status changes over time.
---

# radar-entry-move

Record a ring change for an existing radar entry as an ADR-style supersession.

## When this fires

- "Move React Testing Library from assess to adopt."
- "We're dropping Cypress — put it in hold."
- "Promote Pulumi to trial."
- "Mark Snowflake as superseded by Databricks."

## Why this is a *new file*, not an edit

Snapshots under `radar/<YYYY-MM-DD>/` are immutable — they record what the radar said *on that date*. A ring change is a new decision that supersedes the prior one. Never edit a file in an old snapshot dir; instead, write a new file in the current (or a fresh) snapshot dir.

This mirrors ADR practice: superseded ADRs stay on disk; a new ADR points back at the one it replaces.

## Procedure

1. **Locate prior entry.** Search `radar/*/<slug>.md` for the most recent occurrence. Read it to capture the previous ring and the existing prose.
2. **Pick target snapshot.**
   - If a snapshot dated today exists, use it.
   - If the latest snapshot is recent (e.g. <2 weeks) and the user is just nudging one entry, ask whether to add to that snapshot or open a new dated dir.
   - Otherwise create `radar/<YYYY-MM-DD>/` for today.
3. **Copy + update.** Start from the previous entry's content. Update frontmatter `ring:` to the new value. Reconsider `featured:` — promotions to adopt for a now-mainstream tech often flip to `false` (see `radar/2023-03-01/react.md`).
4. **Record the transition.** The repo's idiomatic style is **prose-led**: rewrite the opening paragraph so it states the new status and (briefly) why. Real example, `radar/2024-12-01/cypress.md` opens with:

   > [Cypress](https://www.cypress.io/) has been a valuable tool for functional testing at INFO… However, as we prioritize advanced testing capabilities and cross-browser support, Cypress is now on hold while we focus on [Playwright](/tools/playwright) as our preferred solution.

   No blockquote, no machine-readable "Status:" header — just an honest paragraph. Match that.

   If the user wants an explicit ADR-style supersession note (useful for promotions where the prior decision is itself worth citing), add it as an optional blockquote near the top:

   ```markdown
   > **Status (YYYY-MM-DD):** Moved from `<old-ring>` to `<new-ring>`.
   > Reason: <one-sentence why>.
   > Supersedes the entry from radar/<old-date>/.
   ```

   Default to prose. Use the blockquote only if the user explicitly asks for a machine-parseable trail, or if you're moving the same entry repeatedly and want the audit trail to read cleanly.

   Keep the rest of the body intact unless the user has new context worth adding. Don't silently rewrite prose that's still accurate.
5. **Hold/deprecate variant.** If moving to `hold`, the body should explain *why we're moving away* and (if known) what replaces it. Link the replacement via `/[quadrant]/[slug]/`. Renaming the existing "Why X?" section to "Previous Benefits" + adding a "Reasons for Holding" section is the established pattern (see `radar/2024-12-01/cypress.md`).
6. **Verify links.** Cross-references in the prose may now point to entries that themselves moved; spot-check the linked slugs still resolve to a file somewhere under `radar/*/`.

## Reasoning for ring transitions

| From → To | Typical reason | Body emphasis |
|-----------|---------------|---------------|
| assess → trial | Pilot worked, ready for limited rollout | What the pilot showed |
| trial → adopt | Proven in production | Where it's now standard |
| adopt → hold | Better alternative emerged, or tech is end-of-life | What replaces it |
| any → assess | Re-evaluation triggered by new info | What changed |
| trial → hold | Pilot failed | What didn't work |

## Output checklist

- [ ] New file written under `radar/<date>/<slug>.md` — original snapshot file untouched.
- [ ] Frontmatter ring updated; quadrant and slug unchanged.
- [ ] Opening paragraph (or optional blockquote) names the new status and why. Don't ship a silent ring-flip.
- [ ] Body still reads coherently — not just a frontmatter flip.
- [ ] If moving to hold: replacement (if any) is linked.

## Anti-patterns

- Don't edit the file in the old snapshot dir. That erases history.
- Don't change the slug or quadrant — that breaks URLs and the "same tech across time" link. If the quadrant is genuinely wrong, that's a separate cleanup, not a ring move.
- Don't fabricate a reason for the move. If the user hasn't said why, ask.
