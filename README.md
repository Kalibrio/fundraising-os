# The Fundraising OS

**15 skills for Claude Code and Codex to decide, prepare and run a startup raise.**

Decide whether and when to raise, build the target list, find warm paths, prepare
the story and numbers, draft outreach, and keep every investor thread moving.
The same Markdown skills work in both apps and share the same project files.
Built by Ludovic Bodin, author of *Atomic Scaling*. Free under the MIT license;
your AI app's subscription or usage charges still apply.

[Website](https://fundraising.atomicscaling.com/) · [Six-week plan and pacing FAQ](https://fundraising.atomicscaling.com/#six-week-plan) · [Full installation guide](INSTALL.md)

## Start in Claude Code

Run in a Claude Code terminal session:

```text
/plugin marketplace add kalibrio/fundraising-os
/plugin install fundraising-os@fundraising-os
/reload-plugins
/fundraising-os:raise-decision
```

The `fundraising-os:` prefix is required for plugin commands. Desktop users can
manage plugins through the Code tab's Plugins menu; see [INSTALL.md](INSTALL.md).

## Start in Codex

Download and extract the [repository ZIP](https://github.com/Kalibrio/fundraising-os/archive/refs/heads/master.zip),
or use your existing checkout. From that directory, run in a terminal
(Python 3.9+):

```sh
python3 scripts/install.py --app codex --project /path/to/my-raise
```

Open your raise folder in Codex, start a new conversation and run:

```text
$raise-decision
```

The installer includes all 15 skills and their references in `.agents/skills/`.
Use `--app both` to also install standalone Claude skills in `.claude/skills/`.
It protects existing skills; `--replace` backs up different versions before
updating. [Details, updates and Claude.ai web instructions →](INSTALL.md)

## The first three steps

1. **Decide:** `raise-decision` gathers each founder's position and returns
   **raise now**, **not yet** (with measurable milestones), or **don't raise**.
2. **Set the facts:** if raising, `raise-context` builds `raise-context.md`, the
   source of truth for numbers, narrative, team and networks. Unknowns stay `TBD`.
3. **Plan the process:** `fundraising-plan` chooses passive, active or hybrid,
   names the raise lead and sets the intensity before research or outreach.

Invoke by app: `/fundraising-os:<name>` for the Claude plugin,
`/<name>` for standalone Claude skills, or `$<name>` for Codex.

## The 15 skills

| Phase | Skill | Output or purpose |
|---|---|---|
| Decide | `raise-decision` | Team decision, dilution math, milestone gates → `raise-decision.md` |
| Foundation | `raise-context` | Facts, narrative and founder networks → `raise-context.md` |
| Foundation | `fundraising-plan` | Mode, timing, ownership and decision gates → `fundraising-plan.md` |
| Build | `investor-list` | Evidence-scored partners, eligibility and research gaps → `investors.tsv`, `investor-scoring.md` |
| Build | `warm-intro-map` | Verified or unverified introduction paths and forwardable drafts |
| Build | `deck` | Narrative and slide content → `deck.md`; editable deck when tools permit |
| Build | `financial-projection` | Driver-based model, downside case and assumptions memo |
| Build | `pitch-rehearsal` | Interactive practice, tough questions and evidence-based answer feedback |
| Run | `investor-brief` | Source-backed preparation for a specific investor meeting |
| Run | `outreach` | Partner-specific email drafts in the relationship owner's voice |
| Run | `pipeline` | Durable thread state → `pipeline.md`; brief and follow-up drafts |
| Run | `data-room` | Diligence index, claim-to-proof map and ranked gaps |
| Sustain | `investor-comms` | Updates for live investors and those who passed |
| Sustain | `pace` | Next skill, artifact consistency and founder workload |
| Close | `closing` | Term-sheet explanation, negotiation preparation and close checklist |

## Prefer prompts in Claude chat?

Use the [copyable 15-step prompt sequence](https://fundraising.atomicscaling.com/#claude-prompts).
It includes a chat setup prompt, one prompt per skill, when to use it, and which
outputs to carry forward. No plugin is required for these concise adaptations;
keep the latest outputs and supply them when starting a new chat.

## Prepare for the next investor meeting

Ask for `investor-brief` with the fund/partner name and meeting details. It uses
supplied notes or available research to prepare talking points, objections,
questions and a proposed next step. Then use `pitch-rehearsal` for an interactive
mock conversation, or request a one-shot preparation pack.

| App | Meeting brief | Pitch practice |
|---|---|---|
| Claude plugin | `/fundraising-os:investor-brief` | `/fundraising-os:pitch-rehearsal` |
| Codex | `$investor-brief` | `$pitch-rehearsal` |

Investor scoring reports fit, evidence coverage and eligibility separately.
A strong thesis match with missing stage/check-size evidence stays a research
candidate. No Apify, Exa, CRM or paid data-room account is required.

## Shared files, on-demand work

Open the same raise folder in Claude Code or Codex to continue the work. Finish
one app's edits before using the other on those files. The package has no
concurrent-edit synchronization.

These are skills that run **when invoked**, not an installed background service.
Daily scans, weekly briefs and monthly updates are suggested cadences; recurring
runs need a separately configured host-app schedule. No email, calendar, CRM or
Drive integration is bundled. Supply current information or connect those tools
separately. A draft is not a sent email and does not reset last contact.

Research uses the host's web tools; without browsing, supplied evidence is used
and unverified details are marked. Decks and spreadsheets use the host's available
artifact tools or code libraries, without assuming a skill named `pptx` or `xlsx`.
If the session cannot create files, it returns labelled text/CSV fallbacks.
See [capabilities and limits](INSTALL.md#what-runs-and-what-does-not).

## Honest by construction

You make the decisions. The skills prepare material and maintain the process;
they do not automatically send messages, share a data room, or commit to terms.
External actions require your instructions and an available integration. Missing
facts are surfaced instead of invented. `closing` helps you brief your lawyer;
it does not replace legal advice.

## Development and verification

Both plugin manifests point to the same `skills/` directory. The Claude
marketplace installs the plugin; Codex users can install project skills with the
bundled installer. The `.codex-plugin/plugin.json` manifest is also available for
Codex plugin packagers.

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
claude plugin validate skills
```

Use the [synthetic runtime fixture](tests/SMOKE.md) to check actual behavior in
both apps. See [AGENTS.md](AGENTS.md) for maintainer and deployment instructions.

## License

[MIT](LICENSE). Fork freely; pull requests welcome.

Built by [Ludovic Bodin](https://atomicscaling.com) · Companion to
[Atomic Scaling OS](https://os.atomicscaling.com).
