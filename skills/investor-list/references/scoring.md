# Investor fit and evidence rubric

Start with the company's target stage, geography, intended investor check range,
lead requirement, sector and excluded competitors. Honor user-specified weights
and gates; record overrides so the next run remains comparable.

## Eligibility before ranking

- `eligible`: required stage, geography, check-size overlap and lead requirement
  are supported; relevant portfolio screening found no direct conflict as of
  the cited research date.
- `research needed`: a required condition or conflict check is unknown. This is
  not rejection and not clearance for outreach.
- `blocked`: a documented hard mismatch or direct competitor conflict. State
  the exact reason; scores and warm paths cannot override it.
- `user exception`: the user explicitly accepted a named blocker. Retain the
  blocker and the decision; never infer acceptance from a prior row's presence.

Do not interpret the total round amount as the desired individual check size.
No lead requirement means follower status is not a blocker. Do not treat an
adjacent company as a direct competitor without explaining the overlap.

## Dimensions

Score each known dimension 0 (mismatch), 0.5 (partial fit), or 1 (clear fit),
with a short rationale and source. Use `unknown` for absent or ambiguous evidence.

| Dimension | Weight | Evidence to assess |
|---|---:|---|
| Sector | 25 | Explicit thesis and relevant investments |
| Stage | 20 | Stage mandate compared with this round |
| Geography | 10 | Investment mandate and company's location |
| Check size | 10 | Supported initial check range versus desired ticket |
| Lead behavior | 10 | Ability and willingness to fulfill the intended role |
| Portfolio relevance | 10 | Relevant experience; gate direct conflicts separately |
| Recent activity | 10 | Dated investment/deployment evidence; default recent window 12 months |
| Partner relevance | 5 | This person's sourced responsibilities, deals or thesis |

An old fund announcement alone does not prove current deployment. Outside the
recent window use unknown unless evidence establishes inactivity or a dated
user-approved alternative. For dimensions that do not constrain this raise,
record why they are not applicable and remove their weight from both denominators.

Calculate, showing arithmetic in `investor-scoring.md`:
- `known weight` = sum of applicable weights with known scores.
- `earned weight` = sum of weight × score for those dimensions.
- **Fit Score** = 100 × earned weight / known weight, rounded to one decimal;
  `unknown` when known weight is zero. This measures fit on known evidence only.
- **Evidence Coverage** = 100 × known weight / total applicable weight, rounded
  to one decimal. If no dimensions apply, both metrics are unknown.

Thus a perfect sector match with everything else unknown is 100 fit but only
25% coverage with default weights. It remains `research needed`, never a top
recommendation. A confirmed mismatch contributes zero earned weight while still
counting toward evidence coverage. Scores are prioritization aids, not investment
probabilities, and coverage does not guarantee sources are current or correct.

## Preserve the Circle interface

Use the following defaults for eligible candidates, applying the highest tier
whose conditions they meet:
- Circle 1: fit ≥85 and coverage ≥80%.
- Circle 2: fit ≥70 and coverage ≥65%.
- Circle 3: fit ≥55 and coverage ≥50%.
- Circle 4: weaker fit, insufficient evidence, or `research needed`.
- Circle 5: `blocked`; preserve on a clearly excluded row if already in the list.

A `user exception` stays Circle 4 by default with the accepted reason visible;
follow an explicit user ranking instead if supplied. Preserve user-assigned
Circles and record any proposed change separately until authorized to rescore.
Sort by Circle, then fit, coverage and warm path. Blocked/research-needed rows
are excluded from the proposed outreach/calibration wave. Do not pad a wave if
few eligible targets exist. Name evidence still needed to qualify more targets.

## Durable outputs

Keep the existing `investors.tsv` base columns and append `Fit Score`,
`Evidence Coverage`, `Eligibility`, `As Of`. Use the review date for As Of.
In `investor-scoring.md`, use the same row ID/fund/partner, dimension scores,
evidence dates/links, gate decisions, arithmetic and research gaps. This makes
scores auditable without forcing every downstream skill to parse eight new
columns. Never silently replace a source-backed value with an unsupported one.
