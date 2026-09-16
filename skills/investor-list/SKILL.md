---
name: investor-list
description: "Build a researched, ranked target list of the investors actually worth your time for this raise — sized to the fundraising mode — written to investors.tsv and output as a tab-separated sheet ready to paste into Google Sheets. Use this skill whenever the user asks to build an investor list, find VCs/angels/funds to pitch, identify which funds or target funds fit their round, research investors, or expand/score their fundraising target set. Trigger it even for casual phrasings like \"who should I raise from?\" or \"find me funds for a seed round\". Prefers depth over volume — 40 right-fit targets beat 400 names."
---

# Investor List

Inbound won't fill a round. You build the list yourself: the funds whose thesis,
stage, check size, and portfolio mean they will actually get what you're building.
Every target researched and scored, in a sheet you can run a pipeline against —
sized to the mode, not to a default.

Research with the web tools available in the host app. If browsing is unavailable,
work from supplied sources and label unverified facts; do not claim fresh research
or invent investor details, relationships, or citations.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## Prerequisites

1. Read `fundraising-plan.md` from the project folder — the mode sizes this
   list. **Active:** the full ~40-target tiered list. **Passive:** a small
   curated set (~10), Circle 1–2 only — a passive raise doesn't need a gauntlet.
   **Hybrid:** build the curated set now, note the expansion to ~40 for when the
   flip trigger fires. If `fundraising-plan.md` is missing, run
   `fundraising-plan` first — you cannot size a list without a mode.
2. Read `raise-context.md`, especially §2 (the raise), §5 (market),
   §10 (ideal investor profile), and §8 (competition → conflicts to exclude). If
   the ideal-investor profile is `TBD`, stop and run the `raise-context` skill
   first — you cannot target without it.

## Procedure

1. **Derive the target archetype** from §10: stage, check size, sector theses,
   geo, and the portfolio signals that indicate fit. Note anti-fit conflicts
   (funds holding a direct competitor) to exclude. Take the target count from
   the mode (see Prerequisites).

2. **Source candidates.** Use the available web search tool per thesis/geo bucket — search each
   bucket separately rather than one broad query (e.g. "seed funds creator economy
   Europe", "AI infra pre-seed leads", then named-partner searches). Pull from:
   recent relevant rounds in your space (who led them), thesis blog posts, partner
   social activity, and the founders' networks in §11 (every founder's, not just
   the raise lead's). Do NOT
   fetch LinkedIn directly (bot-blocked) — use the available web search tool and the fund's own site.

3. **Research each candidate** enough to score it. For the fund: stage, check
   size, lead vs. follow behaviour, recent activity (are they deploying now?),
   relevant portfolio. For the *partner* (target the human, not just the logo):
   what they've backed, what they write about, any public thesis you map to.

4. **Score fit and evidence separately.** Read
   [the scoring rubric](references/scoring.md) for weights, calculations,
   eligibility gates and Circle assignment. Apply it to each candidate and
   record the supporting facts, sources and dates in `investor-scoring.md`.
   Missing evidence is unknown, not a positive match or a zero. Keep confirmed
   mismatches and direct competitor conflicts out of active outreach, and
   distinguish those from research gaps. A warm path affects access, not fit.

5. **Sequence.** Mark a small first wave (3–6 "calibration" targets you like but
   aren't your dream lead) so you can learn from real conversations before
   approaching the top of Circle 1.

6. **Write `investors.tsv`** to the project folder — the same TSV content as the
   paste block below. This file is the durable spine of the raise:
   `warm-intro-map`, `outreach`, and `pipeline` all read it. On a re-run, update
   it in place (add/rescore rows), don't fork a second list.

## Output format — paste-ready TSV

One code block, tab-separated, with this base header below. Preserve these columns and existing IDs for downstream skills;
append the scoring columns shown rather than renaming or removing old columns:

```
#	Fund	Partner	Circle	Stage	Check Size	Thesis Fit (1 line)	Recent Relevant Deal	Lead/Follow	Warm Path?	Conflict?	Source	Notes	Fit Score	Evidence Coverage	Eligibility	As Of
```

- **Warm Path?** = `yes` / `maybe` / `cold` (the `warm-intro-map` skill resolves these).
- **Conflict?** = name a direct competitor, `none found` with dated research,
  or `unknown` when unchecked. Never treat missing research as clearance.
- **Source** = links or supplied document locations; detailed dimension evidence
  lives in `investor-scoring.md`. Distinguish evidence dates from review dates.
- **Fit Score**, **Evidence Coverage**, **Eligibility**, **As Of** follow the
  rubric. On updates preserve existing custom columns, relationship notes and
  user decisions. Supplied lists may be scored at their existing size; do not
  pad a requested review to the mode’s target count.
- Sort by Circle ascending, then fit, coverage and warm path as in the rubric.
- After the block, give a 3-line summary: how many in each Circle, the suggested
  calibration wave, and up to 3 well-supported dream targets to save for last.

## Principles

- **Target partners, not funds.** Deals are championed by one human. Every row's
  research should make the eventual outreach personal.
- **Conflicts are disqualifiers, not footnotes.** A direct competitor holding
  creates a disclosure concern. Exclude from recommended outreach unless the user
  explicitly accepts the conflict; preserve that exception visibly.
- **No padding.** A clean 35 beats a bloated 80. Volume creates pipeline noise
  the `pipeline` skill then has to manage.
