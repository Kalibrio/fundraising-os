# Install Fundraising OS

The same 15 skills work in **Claude Code** and **Codex**. Pick one installation
method per app to avoid duplicate skill names. The skills are free under MIT;
your AI app's subscription or usage charges still apply.

## Claude Code — plugin

Use a current Claude Code release with plugin support and Git installed. In a
Claude Code terminal session, run these slash commands one at a time:

```text
/plugin marketplace add kalibrio/fundraising-os
/plugin install fundraising-os@fundraising-os
/reload-plugins
```

Start with:

```text
/fundraising-os:raise-decision
```

Plugin skills use the `fundraising-os:` prefix. For example:

```text
/fundraising-os:raise-context
/fundraising-os:fundraising-plan
/fundraising-os:investor-list
/fundraising-os:investor-brief
/fundraising-os:pitch-rehearsal
/fundraising-os:pipeline
```

**Desktop:** use the Code tab in the Claude desktop app, choose a **Local**
session and select your raise folder. The `+` menu → **Plugins** manages desktop
plugins. If the marketplace command is unavailable there, use the Claude Code
CLI commands above, or the standalone installer below. Do not paste terminal
commands into ordinary Claude.ai chat.

To verify from a terminal:

```sh
claude plugin list
claude plugin details fundraising-os@fundraising-os
```

Expect version **1.3.0** and **15 skills**. If the skills are missing, reload
plugins or start a new session.

## Codex — project skills

Use a current Codex app, CLI or IDE extension with local skills support.
Download the [repository ZIP](https://github.com/Kalibrio/fundraising-os/archive/refs/heads/master.zip)
and extract it, or clone the repository if you do not already have a checkout:

```sh
git clone https://github.com/Kalibrio/fundraising-os.git
cd fundraising-os
```

From the extracted repository or existing checkout, run this in a **terminal**
(Python 3.9 or newer; Windows can use `py -3` instead of `python3`):

```sh
python3 scripts/install.py --app codex --project /path/to/my-raise
```

Replace `/path/to/my-raise` with your raise folder; quote paths containing spaces.
The installer copies all 15 skill folders **and their reference files** into
`my-raise/.agents/skills/`. It does not change global app settings or create a
schedule. Existing, different skills are protected; see Updating below.

Open **that raise folder** in Codex and start a new conversation. Type `$` to find
the skills, or invoke one directly:

```text
$raise-decision
```

Then, if the team chooses to raise:

```text
$raise-context
$fundraising-plan
$investor-list
```

**Prefer asking Codex to install it?** Paste this into Codex in your raise folder:

```text
Install all 15 skills from https://github.com/Kalibrio/fundraising-os into this
project's .agents/skills directory, including all bundled reference files.
Use scripts/install.py --app codex --project with this project's absolute path
from the downloaded repository. Preserve any existing skills that differ.
Then tell me to start a new conversation and run $raise-decision.
```

The repository also includes a `.codex-plugin/plugin.json` compatibility manifest
for plugin packagers. The supported public Codex install path here is the project
skills installer; Claude's `/plugin` commands are not Codex commands.

## One project, both apps

From the downloaded repository, install both sets of project skills:

```sh
python3 scripts/install.py --app both --project /path/to/my-raise
```

This creates `.agents/skills/` for Codex and `.claude/skills/` for Claude Code.
With **standalone Claude skills**, use `/raise-decision`; with **Codex**, use
`$raise-decision`. Do not also install the Claude plugin for the same workflow
unless you intentionally want both namespaced and standalone copies.

Open the same raise folder in either app. They read the same `raise-decision.md`,
`raise-context.md`, `fundraising-plan.md`, `investors.tsv` and `pipeline.md`.
Finish one app's edits before starting the other on those files; this package
does not provide concurrent editing or conflict resolution.

## Claude.ai web — guided chat

This is a chat workflow, not a plugin installation or background agent.

1. Download and extract the repository ZIP linked above.
2. Create or open a Claude project.
3. Add the relevant `skills/<name>/SKILL.md` files to project knowledge. If your
   upload flow requires unique names, rename local copies to `<name>-skill.md`.
4. Include the bundled references for the skills you use: the raise-context
   template and, for investor scoring, `skills/investor-list/references/scoring.md`.
5. Ask: **"Use the raise-decision skill to help us decide whether to raise."**
6. Save generated artifacts and provide the latest versions in later chats.

Use ordinary language here, not Claude Code slash commands. File generation and
web research depend on the tools enabled in your chat. Uploading instructions
does not create automatic synchronization with a local project or a CRM.

## What runs, and what does not

- **On request:** decision interviews, research (with browsing), deck content,
  financial models, meeting briefs, pitch practice, outreach drafts, pipeline
  reviews and data-room checklists. Investor scoring separates fit from evidence
  coverage; no Apify, Exa or paid data-room account is required.
- **Persistent state:** local apps read and update files in the raise folder.
  Chat-only sessions return inline content or downloadable files when supported.
- **Decks and spreadsheets:** the skills use an available presentation or
  spreadsheet capability, or code libraries when available. There is no required
  skill named `pptx` or `xlsx`. Without file-generation tools, they return a
  clearly labelled text/CSV fallback instead of claiming a finished file.
- **Scheduling:** daily, weekly and monthly cadences are recommendations. Set up
  a scheduled task in your host app separately if you want recurring runs. Give
  it the correct project and sources; use a prompt such as "Use the pipeline
  skill to review overdue threads, save a brief, and draft follow-ups."
- **Integrations:** no email, calendar, CRM or Drive connection is bundled.
  Supply updates yourself or configure an appropriate integration separately.
  Research without browsing is labelled unverified.
- **External actions:** drafts are not sent automatically. Sending, sharing or
  publishing requires your instruction and an available integration. Drafting
  does not change a thread's last-contact date.

## Updating

**Claude plugin:**

```text
/plugin marketplace update fundraising-os
/plugin update fundraising-os@fundraising-os
/reload-plugins
```

**Project skills:** download the latest ZIP, or run `git pull --ff-only` in a
clean existing checkout. Re-run the installer with the original app/project
arguments. Identical skills are left alone. If it reports differences, review
those folders and use `--replace` to install the new version while preserving
previous versions under the raise folder's `.fundraising-os-backups/`:

```sh
python3 scripts/install.py --app both --project /path/to/my-raise --replace
```

Your raise artifacts and unrelated skills are not replaced. Start a new session
after updating. Backups are local files, so do not publish them if they contain
private customizations.

## Troubleshooting

- **Claude reports an unknown skill:** plugin install uses
  `/fundraising-os:raise-decision`; standalone install uses `/raise-decision`.
- **Codex cannot find a skill:** open the folder passed to `--project`, check
  `.agents/skills/raise-decision/SKILL.md`, and start a new conversation.
- **Installer reports a conflict:** it protects existing skills. Review the
  conflict before using `--replace`, which saves the previous version.
- **A skill needs missing context:** provide facts or run `raise-context`.
  Unknowns stay `TBD`; a missing number is not permission to invent it.
- **The app cannot browse or create files:** enable the appropriate host
  capability or use supplied sources and the documented fallback.

Official references: [Claude plugins](https://code.claude.com/docs/en/plugins),
[Claude desktop](https://code.claude.com/docs/en/desktop),
[Codex skills](https://learn.chatgpt.com/docs/build-skills).
