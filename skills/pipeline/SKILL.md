---
name: pipeline
description: "Run the fundraising pipeline so no thread drops — maintains the durable pipeline.md state file, produces the weekly Monday brief of what needs action (grouped by which founder owns it), and generates same-day post-meeting follow-ups across every investor conversation in parallel. Use this skill whenever the user wants to track their raise, asks \"where are we with investors\", asks what to do next or what should I do next on the raise, wants a weekly fundraising update or brief, needs to follow up after an investor meeting, or is managing multiple VC conversations at once. Trigger it for any pipeline, cadence, follow-up, or \"what's the status\" request during a live raise. Operational signals — follow-up speed especially — are read by investors as how you'll run the company, so this skill optimises responsiveness, not just record-keeping."
---

# Pipeline

A raise is many conversations moving in parallel, each at a different stage, each
with a named founder on the hook for a next action that decays if missed. The
pipeline's job is that nothing drops and the right thing happens fast — because
how quickly and specifically you follow up is itself evidence to the investor.

Suggested cadence: the Monday brief weekly; the follow-up generator same-day
after every meeting.

This skill runs when invoked. Its cadence is a recommendation, not an installed
schedule. Use the project files and user-supplied updates; do not imply that email,
calendar or CRM activity has been synced unless an available, authorized
integration actually supplied it. Report the date and source of the latest data.

Prepare drafts by default. Generating a draft does not mean it was sent and must
not advance a thread to Contacted. Send or publish only when the user explicitly
requests it and an appropriate integration is available; record a sent date only
after confirmed delivery or a user-reported send.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## Prerequisites

- `pipeline.md` from the project folder — the durable state. **Read it first,
  every run**; this is what makes "nothing drops" survive across sessions. If it
  doesn't exist yet, create it from `investors.tsv` (every target starts at
  `Sourced`). If `investors.tsv` is also missing, run `investor-list` first.
- `fundraising-plan.md` — the mode sets the tempo (active: weekly-sprint
  cadence, 5-day overdue threshold; passive: relationship-tracking, gentler
  clocks). If missing, run `fundraising-plan` first.
- `raise-context.md` for the facts any follow-up will reference.

## The pipeline stages

```
Sourced → Intro requested → Contacted → Meeting 1 → Diligence → Partner meeting → Term sheet → Closed / Passed
```

`pipeline.md` tracks one line per thread: **stage, last touch date, days since
touch, next action, owner** (the named founder — Leon, not "us"; every next
action has exactly one), and any open question the investor raised. An action
without a named owner is an action nobody takes.

## Two modes

### Mode A — Weekly Monday brief
Produce a prioritised action list for the week, **grouped by owner** so each
founder can read their block and go:

```
FUNDRAISE — WEEK OF [date]
🔥 Needs action now (overdue follow-ups, >5 days since last touch on a live thread):
   [Founder]:
   - [Target] — [what to do] — [draft ready? y/n]
   [Founder]:
   - ...
⏳ Awaiting them (no action needed, note expected-by date):
   - [Target] — waiting on [what] — chase by [date] (owner: [founder])
🌱 Advance this week (warm targets to move a stage):
   - [Target] — next step [x] (owner: [founder])
📊 Funnel: [n contacted / n in meetings / n in DD / n term sheets] — soft-circled $[x] of $[target]
⚠️ Risks: [stalling threads, momentum gaps, any founder overloaded while another is idle]
This week's one priority: [single most important move — and whose it is]
```

Use the overdue threshold in `fundraising-plan.md`. If none is set, use more than
5 business days for active mode; ask for the passive/hybrid threshold instead of
silently imposing the active cadence. Exclude Closed and Passed threads from
live overdue alerts. Keep last-touch dates unchanged unless an actual interaction
occurred; reading a thread or drafting a follow-up is not a touch.
Preserve recorded next-action and chase dates unless the user supplies a change.
The overdue threshold controls alerts; it is not permission to postpone a planned
follow-up. Suggest any timing change separately instead of rewriting the date.

### Mode B — Post-meeting follow-up generator
After a meeting, draft the follow-up within the same day. A good follow-up:
- thanks briefly, then **answers the specific questions they raised** (pull facts
  from `raise-context.md`; if a question needs data you don't have, say when you'll
  send it and add it to the data-room gap list),
- sends only what they asked for (don't dump the whole data room),
- restates the next step and proposes a concrete time,
- is sent fast. Speed is the message.

```
FOLLOW-UP: [Partner, Fund] — meeting [date]
Open questions they raised: [list]
DRAFT:
[email — answers their questions, one clear next step]
To add to data room: [any artefact they asked for that doesn't exist yet]
```

## Procedure

1. Read `pipeline.md` (create from `investors.tsv` if first run), then apply
   whatever the user reports since last time: meetings held, replies, passes,
   new threads.
2. Compute days-since-touch and surface overdue threads first, using the mode's
   threshold from `fundraising-plan.md`.
3. For Mode A, produce the Monday brief. For Mode B, produce the follow-up.
4. **Rewrite `pipeline.md`** with the updated state — every thread's stage, last
   touch, days-since-touch, next action, and owner. This happens every run, not
   just when asked; `investor-comms`, `pace`, and `closing` all read this file
   and it must never be stale.
5. Report only recorded amounts. Keep soft-circled interest, signed commitments
   and wired cash separate. If an amount is absent, mark it `unknown` or `TBD`;
   absence of a record is not evidence of $0. Do not infer commitment amounts from
   a pipeline stage or include passed investors in live totals.
6. Always end with the single highest-leverage next action and its owner.

## Principles

- **Follow-up speed is a feature.** Same-day, specific follow-ups tell an investor
  you operate well. Make it the default.
- **Parallel, not serial.** Keep all live threads roughly in sync on timing so you
  can create a real close window, not a trickle.
- **One thread, one owner.** Shared ownership is how threads drop. Every next
  action names a founder, and the brief makes each founder's week legible at a
  glance.
- **Answer the actual question.** A follow-up that addresses their specific concern
  beats a polished generic recap every time.
