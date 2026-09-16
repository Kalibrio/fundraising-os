---
name: raise-decision
description: "Decide whether and when to raise — as a team, before any fundraising machinery runs. Use this skill whenever the user asks \"should we raise\", \"do we need to raise money\", \"when should we raise\", \"are we ready to raise\", \"raise or bootstrap\", says they're thinking about raising, or is weighing outside capital against alternatives. Also trigger it whenever any downstream fundraising skill (fundraising-plan, investor-list, outreach, deck, pipeline…) is invoked and no `raise-decision.md` exists — the machine must not start on an undecided question. Designed for founding teams of 1–5; surfaces founder disagreements instead of papering over them, and is explicitly allowed to answer \"don't raise\"."
---

# Raise Decision

Every skill downstream of this one assumes the answer is yes. This is the skill
that's allowed to say no. Raising is a five-year relationship, permanent dilution,
and months of founder attention — taken on because it changes the company's
trajectory, not because raising is what startups do. Decide first, together,
on paper. Then run the machine, or don't.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## Prerequisite

Read `raise-context.md` if it exists — §2 (amount, valuation, runway), §3 (the
founders), §4 (traction). If it doesn't exist yet, that's fine: this decision can
run on rough numbers, and a RAISE NOW verdict routes into `raise-context` anyway.
Ask which founders are involved before anything else — the decision belongs to
all of them.

## Procedure

### 1. The founder questionnaire — answered independently

Output a short questionnaire the user copy-pastes to **each founder separately**.
Independent answers are the point: answered in a group call, the loudest voice
sets the anchor and real disagreement never surfaces. Collect the answers as they
come back and record them verbatim per founder.

```
RAISE QUESTIONNAIRE — answer alone, gut answers, 10 minutes
1. Readiness: on today's numbers, would you take a meeting with a good
   investor next week — yes / not yet / no? Why?
2. Dilution: what % of the company are you personally willing to give up
   in this round? What % total before exit?
3. Time: fundraising will eat ~50% of at least one founder for 2–4 months.
   Are you willing to be that founder? Should someone else be?
4. With capital: what does the company look like in 12 months if we raise?
   (3 concrete outcomes)
5. Without capital: what does it look like in 12 months if we don't?
   (3 concrete outcomes — be honest, not catastrophic)
6. Gut call: raise now / raise later at a milestone / don't raise. One line why.
```

### 2. Surface the disagreements

Lay the answers side by side, per question. Where founders agree, note it and move
on. Where they disagree — different dilution tolerance, different 12-month picture,
different gut call — **name each disagreement explicitly as an agenda item for the
team conversation.** Do not average, soften, or arbitrate them away. "Leon wants to
raise now, Max thinks the numbers are 6 months early" is the most valuable line in
the output; the team resolves it in a room, not in this file.

### 3. The dilution math, plainly

From context (or rough inputs), compute what the raise actually costs:

> Raising **$X** at **$Y pre-money** sells **X / (X+Y)** of the company. At your
> target exit that's a dollar figure per founder — say it out loud.

Worked example: raising $1.5M at $6M pre-money = $7.5M post → **20% dilution**.
Four founders at 25% each drop to 20% each. At a $50M exit, those 5 points are
**$2.5M per founder** — the price of the capital. If the $1.5M credibly turns a
$50M outcome into a $100M one, 20% of $100M ($20M each) beats 25% of $50M
($12.5M each) and the raise pays for itself. If it doesn't change the trajectory,
it just cost each founder $2.5M. Run this with the team's real numbers.

### 4. The alternatives, each with its "right when"

- **Revenue growth / customer-funded** — right when the product already sells and
  the constraint is time, not money.
- **Angels only (small SAFE, no lead)** — right when $100–500k unlocks the next
  milestone and you don't want a process or a board.
- **Venture debt / revenue-based financing** — right when revenue is predictable
  and you'd rather pay interest than equity.
- **Grants / competitions / non-dilutive** — right when you qualify and the
  timeline doesn't matter (they're slow).
- **Stay bootstrapped** — right when the team controls its burn, growth is
  compounding without capital, and nobody's answer to Q5 was actually bad.

If one of these beats the raise on the team's own answers, say so — that IS the
verdict, not a footnote to it.

### 5. Verdict — one of three, with teeth

Never default to "raise". Pick one:

- **RAISE NOW** — the signals line up and the team is aligned (or has resolved
  its disagreements). Next step: complete `raise-context`, then run `fundraising-plan` to choose how.
- **NOT YET** — the right move at the wrong time. Define the **milestone gate**:
  the specific numbers or events that flip the answer ("MRR crosses $20k",
  "retention D30 > 25%", "design-partner LOIs signed") plus a **revisit date**.
  Until the gate, the team builds; this skill re-runs at the date or the gate,
  whichever comes first.
- **DON'T RAISE** — venture capital is wrong for this company or this team's
  goals (dilution tolerance, lifestyle intent, a market that won't return a
  fund). Say why plainly, and name what to do instead from the alternatives.
  This is a legitimate, complete outcome — not a failure state.

### 6. Write the file

Write `raise-decision.md` to the project folder:

```
RAISE DECISION — [date]
Verdict: [RAISE NOW / NOT YET / DON'T RAISE]
Reasoning: [3–5 lines]
Dilution math: [$X at $Y pre → Z% — $N per founder at target exit]
Per-founder positions: [founder → gut call → key concern, one line each]
Disagreements & how resolved: [each one, and the resolution — or "open, discuss on (date)"]
Milestone gate (if NOT YET): [specific numbers/events] — revisit: [date]
Instead (if DON'T RAISE): [the chosen alternative and first step]
Next step: [raise-context → fundraising-plan | build until gate | alternative path]
```

`fundraising-plan` reads this file and will not run an active raise against a
NOT YET or DON'T RAISE verdict without the team explicitly overriding it here.

## Principles

- **The team decides, not the loudest founder.** Independent answers first,
  disagreements on the table second, alignment third. A raise one founder
  resents is a time bomb on the cap table.
- **"Don't raise" is a real answer.** Most companies shouldn't raise venture
  money; the ones that should, should raise deliberately. This skill exists to
  tell the two apart.
- **A NOT YET needs numbers.** "When we're ready" is not a gate. A gate you can
  measure is what turns waiting into a plan.
- **Dilution is paid by people.** Percentages feel abstract; dollars per founder
  at exit don't. Always translate.
