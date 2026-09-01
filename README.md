# The Fundraising OS

> "Most rounds aren't lost on the pitch. They're lost on the process — the list you never built, the intro you didn't map, the follow-up that landed three days late."

Inbound won't fill a round. You have to build the target list yourself, research the right partners, find the warm paths in, write outreach that reads like it was written for one specific investor, track every conversation, and keep it all moving in parallel without dropping a thread. And once you're in conversations, the operational signals matter as much as the pitch — how fast you follow up, how specific your outreach is, how ready your data room is the moment someone asks, how consistently you keep investors warm even when there's nothing to report.

I'm Ludovic Bodin. I wrote *Atomic Scaling* and built [Atomic Scaling OS](https://os.atomicscaling.com) to run a company's growth on the 3P3R Method®. **The Fundraising OS** is its companion: 13 Claude skills that run the raise as a system — starting with whether and when to raise at all — so you can spend your attention on the conversations that matter.

The two biggest strategic choices in a raise aren't which funds. The first is **whether to raise at all** — `/raise-decision` puts that question to every founder independently, runs the dilution math and the alternatives, and returns a verdict that is allowed to say no. The second is **how** you raise: a quiet, opportunistic *passive* process, or a sharp, time-boxed *active* one. The OS makes both calls deliberately, then configures its own intensity to match.

This is a **Human-Assisted Autonomous Organization (HAAO)**. The skills do the work. You make the calls.

Thirteen specialists, all slash commands, all Markdown, all free, MIT license. Built for founding teams, not just solo founders. Fork it. Adapt it. Raise with it.

## Who this is for

**Founding teams deciding whether to raise** — the decision skill collects every founder's position independently, surfaces the disagreements, and returns a verdict with teeth.

**Founders running an early raise** — pre-seed through Series A — who can't rely on inbound and want the operational process handled with discipline.

**Solo and small teams** — who'd rather spend their hours in investor conversations than in a spreadsheet of follow-ups.

**Anyone who read *Atomic Scaling*** — and wants the same systematic leverage applied to fundraising.

## The one thing to do first

Run `/raise-decision`. Before any deck, list, or email, it answers the question that decides everything else: should you raise at all, and now? Each founder answers a short questionnaire independently; the skill surfaces where you disagree, runs the dilution math in dollars-per-founder, weighs the alternatives, and returns one of three verdicts — **raise now**, **not yet** (with the milestone gate that flips it), or **don't raise** (with what to do instead).

If the verdict is raise: run `/raise-context` next. It interviews you, builds your single source-of-truth file (`raise-context.md`), pressure-tests every claim, and tells you exactly what's missing before it reaches an investor. **Every other skill inherits its numbers, names, and narrative from this file.**

## Quick start

1. Install the Fundraising OS (see below)
2. Run `/raise-decision` — decide, as a team, whether and when to raise
3. Run `/raise-context` — build your source of truth
4. Run `/fundraising-plan` — decide passive vs. active vs. hybrid, set the intensity
5. Run `/investor-list` — build the target list sized to your mode

Stop there. You'll know if this is for you.

## Install — 30 seconds

**Requirements:** [Claude Code](https://docs.claude.com/en/docs/claude-code) (v1.0.33+) and Git.

> Want the full walkthrough — including how to use the skills in Claude.ai web chat, trigger phrases, and troubleshooting? See **[INSTALL.md](INSTALL.md)**.

### Option A: Install from marketplace (recommended)

Open Claude Code and run:

```
/plugin marketplace add kalibrio/fundraising-os
```

Then install the plugin:

```
/plugin install fundraising-os@fundraising-os
```

### Option B: Manual install

Run this in your **terminal** (not inside Claude Code):

```bash
git clone https://github.com/kalibrio/fundraising-os.git
cp -R fundraising-os/skills/* ~/.claude/skills/
```

Then restart Claude Code (or start a new session) — the skills load from `~/.claude/skills/`.

### Share with your team (optional)

```bash
git clone https://github.com/kalibrio/fundraising-os.git /tmp/fundraising-os && mkdir -p .claude/skills && cp -R /tmp/fundraising-os/skills/* .claude/skills/ && rm -rf /tmp/fundraising-os
```

Everything lives inside `.claude/`. Nothing touches your PATH or runs in the background.

## The Raise Loop

The Fundraising OS is a process, not a collection of tools. Five phases, thirteen skills, five durable files. The phases run roughly in order; warmth runs the whole time, and the close comes at the end.

**Decide → Foundation → Build → Run → Sustain & Close**

`/raise-decision` settles whether and when to raise — as a team. `/raise-context` defines the source of truth that every skill reads. `/fundraising-plan` decides whether you run a passive, active, or hybrid process and writes the mode to `fundraising-plan.md` — which every downstream skill reads before it runs. `/investor-list` and `/warm-intro-map` build the targets (`investors.tsv`) and the paths in; `/deck` and `/financial-projection` sharpen the story and the numbers. `/outreach`, `/pipeline`, and `/data-room` run the live process — `pipeline.md` is the durable state where nothing drops, with a named founder owning every next action. `/investor-comms` keeps every investor warm — including the ones who passed — `/pace` keeps every artifact in sync, and `/closing` drives a clean window to the wire.

## The 13 skills

### Decide
- **`/raise-decision`** — Decision Engine. Whether and when to raise, decided as a team: independent founder questionnaires, dilution math in dollars-per-founder, the alternatives to venture money, and a verdict with teeth — raise now, not yet (milestone gate), or don't raise.

### Foundation
- **`/raise-context`** — Context Engine. The single source of truth. Interviews you (and maps each founder's network), pressure-tests every claim, flags what's missing before it reaches an investor.
- **`/fundraising-plan`** — Raise Strategist. Passive vs. active vs. hybrid. Sets the mode, names the raise lead, and writes the intensity every skill downstream reads.

### Build
- **`/investor-list`** — Target Builder. The funds worth your time — sized to your mode (~40 active, a curated ~10 passive) — researched, scored by fit, and written to a durable `investors.tsv`.
- **`/warm-intro-map`** — Path Finder. The strongest warm path to each partner, plus the forwardable note your network can send in 15 seconds.
- **`/deck`** — Narrative Architect. Story first, slides second. Headlines that are claims; a traction page partners screenshot.
- **`/financial-projection`** — Model Builder. A driver-based model plus the one-page assumptions memo you actually defend.

### Run
- **`/outreach`** — Message Writer. Outreach written for one partner, in the voice of the founder who owns the relationship — a researched hook, one proof, a small ask. Never mail-merge.
- **`/pipeline`** — Process Manager. A durable `pipeline.md` read and rewritten every run: stage, days-since-touch, and a named founder owning every next action. Weekly Monday brief grouped by owner. Nothing drops — across sessions.
- **`/data-room`** — Diligence Anticipator. A data room that pre-answers DD. Claim-to-proof map, ranked gap list, staged access.

### Sustain & Close
- **`/investor-comms`** — Warmth Engine. Monthly updates and two parallel tracks (yes & no). Out-execute the reason they passed, in writing.
- **`/pace`** — Chief of Staff. Decides which skill runs next, keeps the plan, sheet, and pipeline files consistent with each other, and protects founder attention. The glue that orchestrates the whole raise.
- **`/closing`** — Close Driver. Plain-language term-sheet readout, the terms that actually matter, negotiation prep, the close window. Not legal advice.

## Honest by construction

These skills draft; you decide. They never send an email, commit to terms, or make a representation on your behalf. No skill fabricates a number, a name, or a claim — if the context file lacks it, the skill flags the gap rather than inventing it, because anything overstated surfaces in diligence and ends the conversation. `/closing` explains terms so you can brief your lawyer efficiently; it is not legal advice.

## License

MIT — see [LICENSE](LICENSE). Fork freely; pull requests welcome.

Built by [Ludovic Bodin](https://atomicscaling.com) · Author of *Atomic Scaling*.
