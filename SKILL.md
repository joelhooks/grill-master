---
name: grill-master
description: 'Chart a working brief for an effort too big for one agent session, then work it one step at a time until the finish line is clear. Use when: (1) the user brings a loose idea, handoff, or artifact to charter — "grill-master this", "chart a brief"; (2) the user names an existing brief or one of its steps to work; (3) another skill needs multi-session decision planning. Supersedes wayfinder.'
basis:
  - https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
---

# 🔥 grill-master

An effort too big for one session fails a specific way: the outcome drifts from the intent, one unshared assumption at a time. grill-master exists to prevent that drift. It is workflow design: it turns a loose idea into a **working brief** — the operator's intent made checkable: the **finish line**, the shared **vocabulary**, the open **steps**, and the **decision ledger**. Sessions work the brief one step at a time until the finish line holds.

**The workflow unfolds.** A normal workflow is drawn before it runs; this one is discovered. The unfolding rule governs every session: take one step, then re-read the brief as a whole and record what the step changed — steps invalidated, unknowns now askable, terms settled, scope sharpened. Each step is structure-preserving (Alexander): it strengthens the whole that exists now instead of redrawing it. There is no territory to discover — only a whole to strengthen, one step at a time.

All file formats, claim rules, and the ready scan live in [CONVENTIONS.md](CONVENTIONS.md) — follow it exactly whenever you create or edit brief, step, or asset files.

## Decide, don't implement

Each step defaults to resolving a decision; the brief is done when someone could build the thing without another decision — and maintain it without archaeology. The pull to just do the work is the signal you've reached the brief's edge — record the decision and hand off. A brief's **Notes** may explicitly authorize execution — many do, and that is what turns task steps into build work; absent that, sessions produce decisions.

## Refer by name

In everything the human reads, call briefs and steps by their titles with the file linked — a wall of slugs is illegible. The path rides inside the name, never in place of it.

## The brief

One directory per effort: `.brain/projects/<effort>/` — the brief file, one file per step, any assets. The brief is an **index**, not a store: each resolution lives in its step file; the brief gists it in one ledger line and links. Its sections:

- **Finish line** — the explicit, observable conditions that end the effort, including how the result stays maintained after it. Named first, at charter: it fixes scope, so it shapes every step.
- **Vocabulary** — the terms this effort has settled, one line each. This is the effort's pattern language, and it is a record of negotiations, not a glossary: words don't carry meaning by themselves — drift is exactly that assumption failing — so each line is a settlement between operator and agent, and the workflow's steps get named in its terms. A term used two ways silently forks the work; any session that catches drift re-negotiates the term on the spot and lands the settled meaning before closing.
- **Notes** — domain, skills every session should consult, standing calls made mid-effort (attributed, dated), execution authorization if granted.
- **Decision ledger** — one line per closed step: name-link plus gist. Closed is not solved forever: when reality reopens a settled decision, charter a new step that names what it supersedes — the old resolution never gets edited, and the reappearance is natural, not failure.
- **Not yet specified** — unknowns too soft to phrase as steps. The test: can you state the step precisely now, even if you can't take it yet? Sharp → its own step file (blocked is fine). Soft → one line here, graduating when a result sharpens it.
- **Out of scope** — work ruled past the finish line. It never graduates; it returns only if the finish line is redrawn, as a fresh effort. When an existing step turns out to sit past the finish line, close it and leave one line here saying why, linking it.

Open steps are **not** listed in the brief — the scan finds them. **Ready** means open, unblocked, unclaimed.

## Steps

A step is one session-sized unit of the workflow — a decision, an investigation, or authorized build work — in its own file. Four kinds:

- **research** (AFK) — a fact outside the working tree that a decision waits on. Produces a linked asset.
- **prototype** (HITL) — the strongest alignment instrument: a cheap, concrete artifact the operator can touch, via the `prototype` skill. Reach for it early and often — prose agreement is cheap, and a touchable thing surfaces the misunderstandings prose hides.
- **grilling** (HITL, the default) — a live decision conversation via `grill-me` (add `grill-with-docs` when the effort should accrete ADRs), one question at a time, recommendation first. The heat is on the decision, never the human: a grilling is two parties negotiating toward a shared vision, not an interrogation of the operator. Challenge terms against the Vocabulary as they're used; stress-test decisions with concrete scenarios, including who maintains the result and how it fails over time.
- **task** (either) — execution the brief's Notes authorize, or groundwork a decision waits on: provisioning, access, moving data so its shape can be seen. States its done-condition up front ("Resolved when …") and records what was done plus the facts later steps depend on.

HITL means the human speaks for themselves; the session that answers its own grilling has broken the step — reopen it.

**Claim before any work**: stamp yourself as `assignee` per CONVENTIONS.md. The claim is the assignment; a claim older than 24 hours on a still-open step is presumed dead and may be taken over with a note. **One step per session** — a second step needs a second session (a worker, or a fresh invocation). Expect concurrent sessions on the same brief.

## Charter a brief

The user brings a loose idea — or a handoff, transcript, or artifact to plan from.

1. **Pin the finish line** with `grill-me`. Look up facts yourself; put decisions to the human one at a time, recommendation first. Terms settle as the finish line does — seed the Vocabulary with them. Done when the human confirms finish-line conditions they could test an outcome against.
2. **Fan out breadth-first** — grill across the whole space, not deep on any thread, surfacing decisions, build phases, and soft unknowns. Prefer the prototype kind wherever a reaction would beat a discussion, and charter the earliest touchable one the space allows. If everything fits in this one session, skip the brief and say so. Done when the human has nothing more to add at this altitude.
3. **Create the effort** per CONVENTIONS.md: brief, one file per step you can state precisely, blockers wired in a second pass. Done when the scan returns exactly the ready set you expect.
4. **Fire workers at the ready research steps** — one worker per step, each claiming before work: herdr pi panes (per `herdr-orchestration`) when herdr is available, Agent subagents otherwise, task file per CONVENTIONS.md. Done when every ready research step is claimed and running.
5. **Commit, push, stop.** The charter session takes no steps itself; report the brief by name with its ready steps.

## Work a brief

The user names a brief, or a brief plus a step.

1. **Read the brief** — the index only; open step files as needed. The Vocabulary binds this session: use its terms, challenge what's drifted.
2. **Choose the step**: the one the user named, else the first ready step from the scan. **Claim it** before any work.
3. **Resolve it by kind**, zooming into related closed steps on demand.
4. **Record it**: result section in the step file, status closed, one ledger line on the brief.
5. **Unfold**: re-read the whole brief against the result. Graduate sharpened unknowns into step files; close steps the result invalidated (out-of-scope line if they sit past the finish line); land settled terms in the Vocabulary; append mid-effort calls to Notes. Done when the brief reads true end to end — then commit and push.

## Register

A metaphor highlights and hides (Lakoff): explorer talk hid that the workflow is made by deciding, and cook talk would bury the thinking under garnish. So the working words are literal workflow words — step, ready, blocked, claim, finish line — legible to any agent that has never read this skill, and the flavor budget is two words: sessions **grill**, briefs **unfold**. Agents enact a metaphor's entailments mechanically — whatever this file's words imply, sessions will do — so the budget is a safety mechanism, not taste. One mark: 🔥 — the skill's title, and a herdr pane running a grill session. It never goes inside the files.
