---
name: warm-intro-map
description: "Map the best possible warm-introduction path to each investor target before any cold email is sent, and draft the forwardable intro-request notes that mobilise the founders' networks. Use this skill whenever the user asks how to get introduced to a VC/fund/partner, wants to map their network to investors, asks \"who can intro me to X\", wants to find warm paths or an intro path, or is about to start outreach. Trigger it right after the investor list is built and before outreach — a warm path changes everything about how the first email should read."
---

# Warm Intro Map

A warm intro from someone the partner trusts is worth more than ten perfect cold
emails. Before sending anything, find the strongest path to each target — through
whichever founder actually holds the relationship — and arm your connectors with
a note they can forward without thinking.

Prepare drafts by default. Generating a draft does not mean it was sent and must
not advance a thread to Contacted. Send or publish only when the user explicitly
requests it and an appropriate integration is available; record a sent date only
after confirmed delivery or a user-reported send.

Research with the web tools available in the host app. If browsing is unavailable,
work from supplied sources and label unverified facts; do not claim fresh research
or invent investor details, relationships, or citations.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## Prerequisites

- `investors.tsv` from the project folder (the partners to reach, written by
  `investor-list`). If it's missing, run `investor-list` first.
- `raise-context.md` §11 (founder networks — one subsection per founder: cap
  table, advisors, customers, where each network concentrates) and §1/§9 (the
  one-liner and spine, so the forwardable note is sharp).


When selecting new outreach targets, honor `Eligibility` when present in
`investors.tsv`: hold `blocked` and `research needed` rows out of recommended
contact waves; explain the blocker or missing research. User-directed exceptions
must remain visible. Legacy sheets without this column still work: use their
conflict notes and available evidence, without inventing clearance. Preserve
all existing/custom TSV columns when updating rows. Do not erase existing live
threads or change their stage solely because a score changed.

## Procedure

1. **Build the connector inventory** from §11 — across ALL founders' subsections,
   tagging each connector with the founder who holds the relationship: existing
   investors, advisors, notable customers/design partners, and dense network
   nodes (funds, schools, former employers, cities). These are your bridges, and
   the ask must come from the founder the connector actually knows — an intro
   request relayed through the wrong founder is a cold email wearing a warm coat.

2. **For each target partner, find the strongest path.** Rank path types by
   strength:
   - **Tier A** — a portfolio founder of that exact partner, or a co-investor
     they trust. (The single best path; a "this founder is great" note from
     someone they've made money with is gold.)
   - **Tier B** — an advisor/operator with a real relationship to the partner.
   - **Tier C** — a shared strong node (same firm alumni, mutual close contact).
   - **Cold** — no path; route to personalised cold outreach in `outreach`.
   Use the available web search tool to check portfolio overlaps and co-investment patterns; do not
   fetch LinkedIn directly. Where you can only infer a path, mark it `unverified`
   and tell the user to confirm the relationship is real before using it.

3. **Pick ONE best path per target.** Don't scattershot the same partner through
   three people — connectors talk, and it reads as desperate. Reserve a named
   backup path only.

4. **Draft the forwardable note.** For each connector, write a short note the
   *connector* sends to the *partner* — written as if from the connector, not from
   you. It must be: 4–6 sentences, lead with why the connector rates you, one
   crisp line on what the company does (from the spine), one proof point, and a
   soft ask ("worth a quick chat?"). Also draft the even shorter note the
   *owning founder* sends *to the connector* — in that founder's voice — asking
   for the intro and giving them the forwardable blurb so saying yes costs them
   nothing.

5. **Update `investors.tsv`** — set each target's `Warm Path?` column to the
   resolved answer so `outreach` and `pipeline` inherit it.

## Output format

For each target with a path:

```
TARGET: [Partner, Fund]   PATH: [Tier A/B/C]  via [Connector name] (relationship held by [Founder])   [verified/unverified]
— Note to connector (the ask, sent by [Founder]): [2–3 sentences]
— Forwardable blurb (connector → partner): [4–6 sentences, sounds like the connector]
```

Then a table of any **cold** targets routed to `outreach`, and a flagged list
of **unverified** paths the user must confirm first.

## Principles

- **Make saying yes effortless.** A connector should be able to forward in 15
  seconds. If your note makes them write anything, it's too much work and won't go.
- **Protect your connectors' credibility.** Never ask someone to vouch beyond what
  they actually know. A connector burned once won't intro you again.
- **One path, done well.** Sequencing beats spraying. Warm the best path first;
  hold the backup unless it goes cold.
