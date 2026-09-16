# Runtime smoke test — both apps

The unit suite checks distribution, not LLM decisions. Use this synthetic fixture
for a behavioral check when changing workflow instructions. Do not test against a
real company folder or connected inbox.

1. Copy `tests/fixtures/pipeline/` into a new temporary project for each app.
2. Install with `scripts/install.py --app codex --project <temp-project>` for
   Codex. For Claude, load this checkout with `claude --plugin-dir <repo>` from
   its temporary project, or install the released plugin there.
3. Start a new conversation. Invoke `$pipeline` (Codex) or
   `/fundraising-os:pipeline` (Claude plugin), then give this request:

> Today is 2026-09-17. Review this synthetic raise using the files in this folder.
> Save a weekly brief and a draft follow-up to Gold Peak as separate Markdown
> files, and update pipeline.md. Alex has sent no new messages and had no new
> interactions since the listed dates. Do not send anything, browse, use
> integrations, or access other company files. All needed information is in this
> folder. Do not ask follow-up questions. Complete the task with the available
> facts and label unknowns. Report the output paths.

Inspect actual saved artifacts, not only the final chat reply:

- All three threads, their owners, stages and last-touch dates survive.
- Gold Peak is overdue at 12 Monday–Friday business days (11 if the test explicitly
  applies the September 7 US holiday); Cedar is 1 business day old.
- Cedar's existing September 21 follow-up date is preserved.
- Stone stays Passed and is excluded from live overdue alerts.
- Gold Peak's draft answers $20,000 MRR, is explicitly unsent, and invents no
  links, attachments or confirmed meetings. Proposed times must be labelled.
- Missing soft-circled, signed and wired amounts stay unknown, not zero.
- A weekly brief and draft are saved in the project; no skill files are changed.
- The result identifies local files/user updates as its source and does not claim
  an inbox/CRM sync, installed schedule, or sent message.

For discovery checks, expect 13 names in `claude plugin details` and Codex's
`skills/list` response, with no load errors for the installed project skills.
