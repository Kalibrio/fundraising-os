---
name: outreach
description: "Write outreach that reads like it was written for one specific investor, by one specific founder — cold emails, intro-request notes, and the message that rides along a warm intro — each grounded in real research on that partner and drafted in the voice of the founder who owns the relationship. Use this skill whenever the user wants to write investor emails, cold outreach to VCs, a message to send a fund, an intro request, or wants to personalise their fundraising outreach. Trigger it after the investor list and warm-intro map exist. Never produces templated mail-merge spam — each message is built from that partner's actual thesis and a real reason to talk now."
---

# Outreach

The difference between ignored and answered is specificity. A partner can smell a
mail-merge in one line. Each message must prove you researched *them*, give one
concrete reason this is relevant to them *now* — and come from the right founder,
in that founder's actual voice.

Prepare drafts by default. Generating a draft does not mean it was sent and must
not advance a thread to Contacted. Send or publish only when the user explicitly
requests it and an appropriate integration is available; record a sent date only
after confirmed delivery or a user-reported send.

Research with the web tools available in the host app. If browsing is unavailable,
work from supplied sources and label unverified facts; do not claim fresh research
or invent investor details, relationships, or citations.

Use the user's instructions and existing decisions as the authority. Read and write
raise artifacts in the user's project folder, not the installed skill directory.
In chat-only sessions, use the supplied files and return updated artifacts inline
or as downloads; do not claim a project file was saved unless it was.

## Prerequisites

- `fundraising-plan.md` from the project folder — the mode sets the shape:
  active means waves on a clock, passive means opportunistic single sends. If
  it's missing, run `fundraising-plan` first.
- `investors.tsv` (written by `investor-list`) — the partner, the fit, the warm
  path. If it's missing, run `investor-list` first.
- The warm-intro map (`warm-intro-map`) — to know if this is warm or cold, and
  which founder holds the path.
- `raise-context.md` §1, §4, §9, §13 — one-liner, traction, spine, voice.

## Decide the sender and message type first

**Sender:** each message goes out from one named founder — the one who owns the
relationship (warm: whoever the connector or partner actually knows; cold:
usually the raise lead from `fundraising-plan.md`, unless another founder is the
obvious hook — e.g. the technical founder writing to a technical partner). Draft
in *that* founder's voice, and say in the output who sends it. A CEO-voiced email
signed by the CTO reads as ghostwritten, because it is.

- **Warm (riding an intro):** the connector has already vouched. The email is
  short, picks up the thread, and gives the partner an easy yes. Don't re-pitch
  what the intro already said.
- **Cold (no path):** you must earn the reply in the first two lines. Heavier on
  the specific reason you're writing *them*.

## Procedure

1. **Research the one hook.** For this partner, find the single most specific, true
   reason to reach out now: a company they backed that rhymes with yours, a thesis
   they published, a market view they hold. Use the available web search tool; cite the hook to
   yourself so it's real, not flattery.
2. **Open with the hook, not yourself.** First line references them or the timing.
   Never open "I'm the founder of X and we're raising."
3. **One crisp what + one proof.** The spine (§9) in a sentence, plus the single
   strongest true traction fact (§4). No feature lists.
4. **Make the ask small and specific.** "Worth 20 minutes next week?" beats "let me
   know if you'd like to learn more." For warm intros, the ask is even lighter.
5. **Match the sending founder's voice** (§13 — per-founder if the team noted
   differences). Short paragraphs, no corporate throat-clearing, no adjectives
   doing the work of facts.

## Length & format rules

- Cold email: ≤ 130 words, ≤ 5 short paragraphs, one link (deck or one-pager),
  a subject line that's specific not clever.
- Warm reply: ≤ 80 words.
- Always: one clear ask, one link max, no attachments on first contact.

## Output

For each target, produce:

```
TARGET: [Partner, Fund]   TYPE: [warm/cold]   SENDER: [founder — why them]
HOOK: [the specific true reason]
SUBJECT: [specific]
BODY:
[the email, in the sender's voice]
```

Plus a short note on what to personalise further if the user knows something you
don't. Never output the same body twice with the name swapped — if two targets
would get near-identical emails, the research wasn't deep enough; say so.

## Principles

- **Written-for-one or not sent.** If you could send it to any fund, it's spam.
- **Brevity is respect.** Partners read on their phone between meetings. Every word
  that isn't earning the reply is costing it.
- **Honesty compounds.** The relationship outlasts the round. Never imply more
  traction, momentum, or competing interest than is true — it surfaces in DD and
  ends the conversation.
