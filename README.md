# The Fundraising OS

> "Most rounds aren't lost on the pitch. They're lost on the process — the list you never built, the intro you didn't map, the follow-up that landed three days late."

Inbound won't fill a round. You have to build the target list yourself, research the right partners, find the warm paths in, write outreach that reads like it was written for one specific investor, track every conversation, and keep it all moving in parallel without dropping a thread. And once you're in conversations, the operational signals matter as much as the pitch — how fast you follow up, how specific your outreach is, how ready your data room is the moment someone asks, how consistently you keep investors warm even when there's nothing to report.

I'm Ludovic Bodin. I wrote *Atomic Scaling* and built [Atomic Scaling OS](https://os.atomicscaling.com) to run a company's growth on the 3P3R Method®. **The Fundraising OS** is its companion: 12 Claude skills that orchestrate the operational raise so you can spend your attention on the conversations that matter.

The single biggest strategic choice in a raise isn't which funds — it's **how** you raise: a quiet, opportunistic *passive* process, or a sharp, time-boxed *active* one. The OS makes that call deliberately, then configures its own intensity to match.

This is a **Human-Assisted Autonomous Organization (HAAO)**. The skills do the work. You make the calls.

Twelve specialists, all slash commands, all Markdown, all free, MIT license. Fork it. Adapt it. Raise with it.

## Who this is for

**Founders running an early raise** — pre-seed through Series A — who can't rely on inbound and want the operational process handled with discipline.

**Solo and small teams** — who'd rather spend their hours in investor conversations than in a spreadsheet of follow-ups.

**Anyone who read *Atomic Scaling*** — and wants the same systematic leverage applied to fundraising.

## The one thing to do first

Run `/raise-context`. It interviews you, builds your single source-of-truth file (`raise-context.md`), pressure-tests every claim, and tells you exactly what's missing before it reaches an investor. **Every other skill inherits its numbers, names, and narrative from this file.** The quality of the whole machine is capped by the quality of that file.

## Quick start

1. Install the Fundraising OS (see below)
2. Run `/raise-context` — build your source of truth
3. Run `/fundraising-plan` — decide passive vs. active, set the intensity
4. Run `/investor-list` — build the ~40 funds worth your time
5. Run `/warm-intro-map` — find the best path to each partner

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
/plugin install fundraising-os@kalibrio/fundraising-os
```

### Option B: Manual install

Run this in your **terminal** (not inside Claude Code):

```bash
git clone https://github.com/kalibrio/fundraising-os.git ~/.claude/plugins/fundraising-os
```

Then open Claude Code and reload plugins:

```
/reload-plugins
```

### Share with your team (optional)

```bash
cp -Rf ~/.claude/plugins/fundraising-os .claude/plugins/fundraising-os && rm -rf .claude/plugins/fundraising-os/.git
```

Everything lives inside `.claude/`. Nothing touches your PATH or runs in the background.

## The Raise Loop

The Fundraising OS is a process, not a collection of tools. Four phases, twelve skills, one context file. The phases run roughly in order; warmth runs the whole time, and the close comes at the end.

**Foundation → Build → Run → Sustain & Close**

`/raise-context` defines the source of truth that every skill reads. `/fundraising-plan` decides whether you run a passive or active process and sets the intensity for everything after it. `/investor-list` and `/warm-intro-map` build the targets and the paths in; `/deck` and `/financial-projection` sharpen the story and the numbers. `/outreach`, `/pipeline`, and `/data-room` run the live process. `/investor-comms` keeps every investor warm — including the ones who passed — `/pace` is the chief of staff that sets the tempo and keeps every skill in sync, and `/closing` drives a clean window to the wire. Nothing falls through the cracks because every skill knows what came before it.

## The 12 skills

### Foundation
- **`/raise-context`** — Context Engine. The single source of truth. Interviews you, pressure-tests every claim, flags what's missing before it reaches an investor.
- **`/fundraising-plan`** — Raise Strategist. Passive vs. active vs. hybrid. Sets the mode and the intensity for every skill downstream.

### Build
- **`/investor-list`** — Target Builder. The ~40 funds worth your time, researched and scored by fit, as a paste-ready sheet. Depth over volume.
- **`/warm-intro-map`** — Path Finder. The strongest warm path to each partner, plus the forwardable note your network can send in 15 seconds.
- **`/deck`** — Narrative Architect. Story first, slides second. Headlines that are claims; a traction page partners screenshot.
- **`/financial-projection`** — Model Builder. A driver-based model plus the one-page assumptions memo you actually defend.

### Run
- **`/outreach`** — Message Writer. Outreach written for one partner — a researched hook, one proof, a small ask. Never mail-merge.
- **`/pipeline`** — Process Manager. Weekly Monday brief, same-day follow-up generators, stage tracking across every thread. Nothing drops.
- **`/data-room`** — Diligence Anticipator. A data room that pre-answers DD. Claim-to-proof map, ranked gap list, staged access.

### Sustain & Close
- **`/investor-comms`** — Warmth Engine. Monthly updates and two parallel tracks (yes & no). Out-execute the reason they passed, in writing.
- **`/pace`** — Chief of Staff. Paces the communication, decides which skill runs next, keeps every artifact in sync, and surfaces the one thing that has to happen today. The glue that orchestrates the whole raise.
- **`/closing`** — Close Driver. Plain-language term-sheet readout, the terms that actually matter, negotiation prep, the close window. Not legal advice.

## Honest by construction

These skills draft; you decide. They never send an email, commit to terms, or make a representation on your behalf. No skill fabricates a number, a name, or a claim — if the context file lacks it, the skill flags the gap rather than inventing it, because anything overstated surfaces in diligence and ends the conversation. `/closing` explains terms so you can brief your lawyer efficiently; it is not legal advice.

## License

MIT — see [LICENSE](LICENSE). Fork freely; pull requests welcome.

Built by [Ludovic Bodin](https://atomicscaling.com) · Author of *Atomic Scaling*.
