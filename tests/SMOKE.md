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

For discovery checks, expect 15 names in `claude plugin details` and Codex's
`skills/list` response, with no load errors for the installed project skills.

## Meeting preparation and scoring (v1.3.0)

Copy `tests/fixtures/meeting-prep/` into a separate temporary project per app,
install the skills, then submit `request.txt`. Review the saved outputs:

- All four IDs, original notes and Relationship Owner values survive in TSV.
- Clear Seed: 100 fit / 100% coverage, eligible, Circle 1.
- Thin Thesis: 100 fit / 25% coverage, research needed, Circle 4. Old fund news
  is not proof of current deployment.
- Rival Fund and Growth Only are blocked, Circle 5, for their documented
  conflict and stage/check-size mismatch respectively. Neither enters a wave.
- Scoring evidence and arithmetic are saved; only Clear Seed is recommended.
- The Clear Seed brief calls the meeting proposed/unconfirmed, retains Alex
  and September 10 last contact, and cites local evidence without claiming sync.
- Brief and pitch prep use €20,000 MRR and unknown retention, flag the old
  deck's unsupported claims, and label €50,000 MRR as a target.
- The prep pack contains five hypothetical questions with honest answer
  outlines; it never claims the founder answered them or completed a rehearsal.
- Context, original deck, pipeline and installed skills are unchanged.

Also test a fresh interactive conversation: ask to practice a two-minute
opening with `pitch-rehearsal`. It should invite the founder to speak and wait,
not invent a founder answer or finish a mock meeting. Reply with an opening
claiming the old deck's unsupported revenue/retention; it should correct the
claims from context, offer focused feedback, and ask at most one investor
question before waiting. No voice/body-language assessment from text alone.

These synthetic checks demonstrate the tested paths, not guaranteed output
quality for every company or connected tool.
