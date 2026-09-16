# Fundraising OS maintenance

This repository contains 15 shared skills, Claude and Codex compatibility
manifests, a project-local installer, and a static GitHub Pages site.

## Structure

- `skills/<name>/SKILL.md`: one shared source for both apps. Keep the existing stable
  names; bundled references must stay inside their owning skill directory.
- `.claude-plugin/`: Claude plugin and marketplace manifests.
- `.codex-plugin/plugin.json`: Codex compatibility manifest for packaging.
- `scripts/install.py`: standalone project skills installer, Python 3.9+,
  standard library only. Copies to `.agents/skills` and/or `.claude/skills`.
- `docs/`: live site at `https://fundraising.atomicscaling.com/`.
- `INSTALL.md`: installation, updating, supported capabilities and limits.

## Changes and checks

Keep platform-specific commands in installation documentation. Within shared
skills, refer to other skills by name and use available host capabilities rather
than assuming a tool or skill exists. Raise artifacts belong in the user's
working project, never the installed plugin directory. Preserve the user's
instructions and existing authorization.

Run `python3 -m pip install -r requirements-dev.txt` in a virtual environment,
then `python3 -m unittest discover -s tests -v`. When Claude Code is installed,
also validate the two Claude manifests and `skills/` with `claude plugin validate`.
Check Codex discovery using its `skills/list` app-server method after installing
into a temporary project's `.agents/skills/`. An install/list check does not prove
workflow behavior; use a synthetic raise fixture for behavioral smoke tests.
Do not use real company data in public test fixtures.

Bump both plugin versions together for user-facing skill changes. Update
installation version examples and the site's release label at the same time.

## Publish

The repository is public; the default branch is `master`. GitHub Pages serves
`/docs` from that branch. Keep `docs/CNAME` equal to `fundraising.atomicscaling.com`
and preserve the brand images. Do not change hosting providers for routine edits.

For authorized releases, commit only the intended files on a branch, open and
merge a PR after the checks pass, then verify the Pages build and the live site.
Do not recreate the repository, rename its default branch, or commit unrelated
working changes. Test a fresh public Claude marketplace installation after a
plugin release, and run the published standalone installer into a temporary
project for Codex. Use temporary configuration for installation tests so the
maintainer's normal installed skills and settings stay unchanged.
