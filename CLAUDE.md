# CLAUDE.md — Fundraising OS

Context and deployment playbook for Claude Code. If asked to "deploy", "publish",
or "ship this", follow the **Deploy** section below exactly.

## What this repo is

The **Fundraising OS** — a Claude Code plugin of **13 skills** that run a startup
raise (starting with whether/when to raise at all), plus its marketing site. This single repo does double duty:

1. **The plugin marketplace** — installed with
   `/plugin marketplace add kalibrio/fundraising-os`.
2. **The website** — served via GitHub Pages from `/docs` at
   `fundraising.atomicscaling.com` (mirrors how `os.atomicscaling.com` is hosted
   from `kalibrio/atomic-scaling-os`).

## Structure

```
.claude-plugin/plugin.json     plugin manifest
.claude-plugin/marketplace.json marketplace manifest — REQUIRED for
                                /plugin marketplace add to work
skills/<command>/SKILL.md       13 skills; folder name == slash command
  raise-decision · raise-context · fundraising-plan · investor-list ·
  warm-intro-map · deck · financial-projection · outreach · pipeline ·
  data-room · investor-comms · pace · closing
docs/                         index.html, atomic-logo.jpg, ludovic.jpg,
                              favicon.svg, CNAME (fundraising.atomicscaling.com)
README.md · INSTALL.md · LICENSE
```

## Deploy

**Preconditions:** `gh auth status` shows you're authenticated with write access to
the `kalibrio` org, and `git` is available. Run from the repo root.

1. **Commit any pending changes.**
   ```bash
   git add -A && git commit -m "Deploy Fundraising OS" || echo "nothing to commit"
   ```

2. **Create the PUBLIC repo and push.** (The plugin installer reads the repo
   anonymously, so it MUST be public.)
   ```bash
   gh repo create kalibrio/fundraising-os --public --source=. --remote=origin --push
   ```
   If the repo already exists, instead do:
   ```bash
   git remote add origin https://github.com/kalibrio/fundraising-os.git 2>/dev/null || true
   git push origin master
   ```
   (The repo's default branch is **master** — do not rename it; Pages builds from it.)

3. **Enable GitHub Pages from `/docs` on `master`.** (Ignore a 409 — means already on.)
   ```bash
   gh api -X POST repos/kalibrio/fundraising-os/pages \
     -f "source[branch]=master" -f "source[path]=/docs" || true
   gh api repos/kalibrio/fundraising-os/pages --jq '.html_url, .status'
   ```

4. **DNS (one record, the only manual-ish step).** The site needs:
   ```
   CNAME   fundraising   →   kalibrio.github.io
   ```
   in the `atomicscaling.com` zone. If a DNS provider CLI or MCP connector is
   available, set it; otherwise surface this exact record to Ludovic to add at his
   registrar. `docs/CNAME` already declares the custom domain.

5. **Enforce HTTPS** once the cert is issued (give DNS a few minutes first):
   ```bash
   gh api -X PUT repos/kalibrio/fundraising-os/pages -F https_enforced=true || true
   ```

6. **Verify.**
   ```bash
   curl -sI https://fundraising.atomicscaling.com | head -1   # expect 200 after propagation
   gh api repos/kalibrio/fundraising-os --jq '.visibility'     # expect "public"
   ls skills | wc -l                                           # expect 13
   ```
   Then confirm the plugin installs (in a Claude Code session):
   ```
   /plugin marketplace add kalibrio/fundraising-os
   /plugin install fundraising-os@fundraising-os
   ```
   Type `/` then `raise` → you should see `/raise-decision`, `/raise-context`,
   `/fundraising-plan`, … (13 total). Manual fallback: copy each `skills/<name>`
   folder into `~/.claude/skills/` (or the project's `.claude/skills/`).

## Guardrails

- **Public repo** — non-negotiable; private breaks `/plugin marketplace add`.
- **Don't rename skill folders** — the folder name *is* the slash command and the
  site/README reference them by that name.
- **Keep `docs/CNAME`** = `fundraising.atomicscaling.com`.
- **Don't touch** `atomic-logo.jpg` / `ludovic.jpg` — they're the live brand assets.
- This mirrors `os.atomicscaling.com` (site on GitHub Pages). If Ludovic would
  rather host the **site** on AWS S3 + CloudFront (his usual default for non-OS
  static sites), then push only the plugin to GitHub and `aws s3 sync docs/ …`
  to the bucket instead — **ask him first**.
