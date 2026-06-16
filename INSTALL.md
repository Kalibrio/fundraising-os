# Install The Fundraising OS

Two ways to use the 11 skills. The first (Claude Code Desktop) is the recommended setup — it's what the skills are designed for, and it works without ever touching a terminal.

| You want to… | Use |
|---|---|
| Run the skills on your Mac/PC with file output (sheets, drafts, the data-room index written into your project folder) and one-click updates from GitHub | **[Path A — Claude Code Desktop](#path-a--claude-code-desktop-recommended-5-minutes)** |
| Run a skill in your browser at claude.ai with no install (slower, no file output) | **[Path B — Claude.ai web chat](#path-b--claudeai-web-chat)** |

---

## Path A — Claude Code Desktop (recommended, 5 minutes)

If you've never used Claude Code before, follow these exact steps. No terminal needed.

### Step 1 — Download Claude Code Desktop

1. Open your browser and go to **https://claude.com/code**
2. Click **"Download for Mac"** (or Windows / Linux — the page auto-detects your OS).
3. Open the downloaded file and install the app.
4. Open **Claude Code** and sign in with the same Claude account you use on claude.ai.

You should now see a Claude Code window — a chat with a text box at the bottom and a sidebar showing your project folder.

### Step 2 — Open any folder as a project

Claude Code needs a "project folder" — it can be anything, even an empty one. The skills write their outputs (your `raise-context.md`, investor sheet, outreach drafts, data-room index) into this folder.

1. In Claude Code: **File menu → Open Folder…**
2. Pick any folder. If you don't have one ready, create a folder on your Desktop called `my-raise` and pick that.

### Step 3 — Install the Fundraising OS plugin

Type these into the chat box at the bottom of the Claude Code window — the same place you'd type a message.

**Type this and press Enter:**

```
/plugin marketplace add kalibrio/fundraising-os
```

Claude Code confirms it added the repo as a marketplace. Takes 1–2 seconds.

**Then type this and press Enter:**

```
/plugin install fundraising-os@kalibrio/fundraising-os
```

Claude Code confirms the plugin is installed and 11 skills are now available.

### Step 4 — Test that it worked

In the chat box, type a `/` (forward slash). A menu pops up showing available commands. Start typing `raise` — you should see:

```
/raise-context
```

If you see it, you're done installing.

### Step 5 — Run your first skill

```
/raise-context
```

It interviews you, builds your `raise-context.md` source-of-truth file in your project folder, and tells you exactly what to fix before you start outreach. Then:

```
/fundraising-plan     → decide passive vs. active, set the intensity
/investor-list        → the ~40 funds worth your time, as a paste-ready sheet
/warm-intro-map       → the best path to each partner
```

### Updating

When the OS is updated on GitHub, refresh in Claude Code:

```
/plugin marketplace update kalibrio/fundraising-os
```

---

## Path B — Claude.ai web chat

No install, runs in your browser. Slower and no file output, but good for trying a single skill.

1. Go to **https://claude.ai** and create a new **Project** (or open an existing one).
2. Add the skill files to the project's knowledge: from this repo, upload the `SKILL.md` files from `skills/` for the skills you want, plus `skills/raise-context/references/raise-context-template.md`.
3. In the project chat, describe what you need in plain language — e.g. *"set up my raise context"* or *"build my investor list"* — and Claude will follow the matching skill.

Because there's no project folder on the web, Claude returns the outputs inline (sheets as pasteable text, drafts as text). Copy them into your own Drive / data room.

---

## Troubleshooting

**`/plugin` command not found** — Update Claude Code to v1.0.33 or later, then restart it.

**Skills don't appear after install** — Run `/reload-plugins`, or quit and reopen Claude Code. Confirm with `/plugin list`.

**A skill asks for context it doesn't have** — Run `/raise-context` first. Every skill reads from `raise-context.md`; if a field is missing, the skill will flag it rather than invent a number.

**Manual install (corporate firewall, etc.)**

```bash
git clone https://github.com/kalibrio/fundraising-os.git ~/.claude/plugins/fundraising-os
```

Then in Claude Code: `/reload-plugins`.

---

Built by [Ludovic Bodin](https://atomicscaling.com). MIT license. Questions or improvements → open an issue or PR on [GitHub](https://github.com/kalibrio/fundraising-os).
