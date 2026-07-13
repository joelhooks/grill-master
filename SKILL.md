---
name: grill-master
description: 'Chart a working brief for an effort too big for one agent session, then work it one question at a time until the finish line is clear. Use when: (1) the user has a loose idea to charter — "grill-master this", "chart a brief", "this needs a brief"; (2) the user names an existing brief or its question to work; (3) another skill needs multi-session decision planning. Supersedes wayfinder.'
basis:
  - https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
---

# grill-master

A loose idea has arrived — too big for one agent session, and nobody can see the finished shape yet. grill-master turns it into a **working brief**: a shared `.svx` artifact holding the **finish line**, the open **questions**, and the **decision ledger**. Sessions then work the brief one question at a time until nothing is left to decide.

**The unfolding rule** governs every session: answer one question, then re-read the brief as a whole and record what the answer changed — questions invalidated, unknowns now askable, scope sharpened. The shape unfolds out of decisions; each answer reshapes what the next session sees.

All file formats, frontmatter contracts, the claim rules, and the ready-question scan live in [CONVENTIONS.md](CONVENTIONS.md) — follow it exactly whenever you create or edit brief, question, or asset files.

## Decide, don't implement

Each question resolves a decision; the brief is done when someone could go build the thing without another decision. The pull to just do the work is the signal you've reached the brief's edge — record the decision and hand off. A brief's **Notes** may explicitly authorize execution (say so at charter time); absent that, sessions produce decisions.

## Refer by name

Briefs and questions have names — their titles. In everything the human reads, refer to them by name with the file linked; a wall of slugs is illegible. The path rides inside the name, never in place of it.

## The brief

One directory per effort: `.brain/projects/<effort>/`, holding the brief file, one file per question, and any assets. The brief is an **index**, not a store — each decision lives in exactly one place (its question file); the brief gists it in one ledger line and links. Its sections:

- **Finish line** — the explicit, observable conditions that end the effort. Named first, at charter: it fixes scope, so it shapes every question.
- **Notes** — domain, skills every session should consult, standing calls made mid-effort (attributed, dated), execution authorization if granted.
- **Decision ledger** — one line per answered question: name-link plus a one-line gist.
- **Not yet specified** — unknowns too soft to phrase as questions yet. The test: can you state the question precisely now, even if you can't answer it? Sharp → its own question file (blocked is fine). Soft → one line here, graduating to a question file when an answer sharpens it.
- **Out of scope** — work ruled past the finish line. It never graduates; it returns only if the finish line is redrawn, as a fresh effort. When an existing question turns out to sit past the finish line, close it and leave one line here saying why, linking it.

Open questions are **not** listed in the brief — they are found by the scan in CONVENTIONS.md. **Ready** means open, unblocked, unclaimed.

## Questions

A question is one session-sized decision or investigation, in its own file. Four kinds:

- **research** (AFK) — a fact outside the working tree that a decision waits on: docs, the docs brain, third-party APIs. Produces a linked asset.
- **prototype** (HITL) — raise the fidelity of the discussion with a cheap concrete artifact to react to, via the `prototype` skill. Links the artifact as an asset.
- **grilling** (HITL, the default) — a live decision conversation via `grill-me` (add `grill-with-docs` when the effort should accrete a glossary or ADRs), one question at a time, recommendation first.
- **task** (either) — work that must happen before something can be *decided*: provisioning, access, moving data so its shape can be seen. Earns its place by unblocking a decision. Records what was done and the facts later questions depend on.

HITL means the human speaks for themselves; the session that answers its own grilling has broken the question — reopen it.

**Claim before any work**: stamp yourself as `assignee` per CONVENTIONS.md. The claim is the assignment; a claim older than 24 hours on a still-open question is presumed dead and may be taken over with a note. **One question per session** — a second question needs a second session (a worker, or a fresh invocation). Expect concurrent sessions on the same brief.

## Charter a brief

The user arrives with a loose idea.

1. **Pin the finish line** with `grill-me`. Look up facts yourself; put decisions to the human one at a time, recommendation first. Done when the human confirms finish-line conditions they could test an outcome against.
2. **Fan out breadth-first** — grill across the whole space, not deep on any thread, surfacing open questions and soft unknowns. If everything fits in this one session, skip the brief and say so. Done when the human has nothing more to add at this altitude.
3. **Create the effort** per CONVENTIONS.md: brief file, one file per sharp question, blockers wired in a second pass (files need paths before they can reference each other). Done when the scan returns exactly the ready set you expect.
4. **Fire workers at the ready research questions** — AFK questions don't need you or the human. One worker per question, each claiming before work: herdr pi panes (per `herdr-orchestration`) when herdr is available, Agent subagents otherwise, with a brief task file per CONVENTIONS.md. Done when every ready research question is claimed and running.
5. **Commit, push, stop.** The charter session answers nothing itself; report the brief by name with its ready questions.

## Work a brief

The user names a brief, or a brief plus a question.

1. **Read the brief** — the index only; open question files as needed.
2. **Choose the question**: the one the user named, else the first ready question from the scan. **Claim it** before any work.
3. **Resolve it by kind** (see Questions above), zooming into related closed questions on demand.
4. **Record it**: answer section in the question file, status closed, one ledger line on the brief.
5. **Unfold**: re-read the whole brief against the answer. Graduate unknowns that are now sharp into question files; close questions the answer invalidated (out-of-scope line if they sit past the finish line); append mid-effort calls to Notes. Done when the brief reads true end to end — then commit and push.

## Register

Mechanics stay plain fields — status, blockers, assignee, finish line, out of scope — legible to any agent that has never read this skill. The metaphor budget is two words: sessions **grill**; briefs **unfold**.
