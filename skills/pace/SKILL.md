---
name: pace
description: "The orchestration layer of the Fundraising OS — decides which skill runs next and why, keeps the durable artifacts (raise-decision, raise-context, fundraising-plan, investors.tsv, pipeline.md) consistent with each other, and protects the founders' attention from the raise itself. Use this skill when the user asks how to sequence the fundraising work, which skill or phase comes next, whether the machine is in sync, how to keep the raise on track or orchestrate it, or wants a chief-of-staff view over the whole process. (For \"what should I do next\" on live investor threads — follow-ups, who to chase — that's the pipeline skill; pace answers \"which part of the machine runs next\".)"
---

# Pace

The other skills each do one job well; `pace` makes them move together. It does
not generate raise content, track investor threads, or write briefs about who to
email — `pipeline` owns what needs action. `pace` owns three things only: the
**sequence** (which skill runs next), the **sync** (do the artifacts agree), and
the **attention budget** (is the raise eating the company).

This skill runs when invoked. Its cadence is a recommendation, not an installed
schedule. Use the project files and user-supplied updates; do not imply that email,
calendar or CRM activity has been synced unless an available, authorized
integration actually supplied it. Report the date and source of the latest data.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## When this runs

Whenever the user is unsure which part of the OS to run, when the process feels
out of order, or periodically as a health check on the machine. Suggested
cadence: a quick orchestration check weekly, or at any phase transition.

## Prerequisites

Read whichever of these exist in the project folder: `raise-decision.md`,
`raise-context.md`, `fundraising-plan.md`, `investors.tsv`, `pipeline.md`.
Missing files are not errors here — they ARE the answer: the first missing
artifact in the sequence is usually the next skill to run.

## What it does

1. **Orchestrate the sequence.** Know which phase the raise is in and name the
   next skill to run and why. The canonical order:
   `raise-decision → raise-context → fundraising-plan → deck / financial-projection
   → investor-list → warm-intro-map → data-room → outreach → pipeline (+
   investor-comms) → closing`. Decision before context, mode before targets,
   deck and model before serious meetings, data room ready before an active
   launch. When a step is being skipped, say so and name the risk.

2. **Keep the artifacts in sync.** Check that the durable files agree with each
   other and with reality: the mode in `fundraising-plan.md` still matches the
   verdict and gate in `raise-decision.md`; `investors.tsv` is sized to the
   mode; `pipeline.md` isn't stale (last rewrite vs. today); the numbers the
   deck, model, and data room claim all trace back to the same
   `raise-context.md`. A figure that says one thing in the deck and another in
   the room is a trust leak — name the drift and the skill that fixes it.

3. **Match the tempo to the mode.** In passive, the machine runs patient and
   relationship-led; in active, on a tight clock with a real window. If the
   observed behaviour (outreach volume, pipeline cadence) doesn't match the
   declared mode, either the behaviour or the plan is wrong — flag it and route
   to `fundraising-plan` to re-decide.

4. **Protect the team's attention.** A raise will eat the company if you let it.
   Check the load per founder (from `pipeline.md`'s owner column): is the raise
   lead underwater while others are idle? Is the whole team in fundraising mode
   when the plan says one founder runs it? Guard build time — especially in
   passive mode, where staying heads-down is the point — and say what to drop.

## Output format

```
ORCHESTRATION — [date]
Phase: [where the raise is]   Mode: [from fundraising-plan.md]
Run next: [skill] — because [reason]
Then: [skill] → [skill].  Hold off on [skill] until [condition].
Sync check: [artifacts consistent / DRIFT: what disagrees, fix via which skill]
Attention check: [load per founder — anything eating the company]
```

For "what needs action on investor threads", route to `pipeline` — that's its
brief, not this one's.

## Principles

- **Direct, don't duplicate.** `pace` points to the right skill; it never redoes
  their work. Its value is sequence, sync, and follow-through — the moment it
  starts writing emails or briefs, it's the wrong skill.
- **The first missing artifact is the answer.** The machine's own files tell you
  where it is. Read them before opining.
- **Sync is the cheapest leverage.** Catching a drifted number costs a minute;
  an investor catching it costs the round's momentum.
- **The raise serves the company, not the reverse.** When in doubt, protect
  build time. A great quarter closes more rounds than a great follow-up.
