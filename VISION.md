# Vision

grill-master today is a skill and a file contract. That's deliberate — the mechanics had to prove themselves as plain text before anything got built on top. This is where it goes from here.

## Workflow design, all the way down

The skill's real subject is workflow design: understand the problem, explore the context, settle the language, grow a pattern language for the domain, design the system — and use all of that to build robust workflows for execution. Which means the endgame is designing state machines. A brief's steps already are one being discovered: `status`, `blockers`, and `kind` define states and transitions, charter sketches the machine, each session fires one transition, and the unfolding rule re-derives what's reachable after every firing. The Vocabulary section is the pattern-language layer — the terms the machine's states get named in. As the tooling matures, a finished brief should compile toward an executable workflow definition, not just a prose plan.

## The brief outlives the session

A brief is a durable artifact, not a chat transcript. Every step, result, and scope call lives in files that survive the agent that wrote them, sync across machines, and stay legible to a human with a text editor. Everything below builds on that property; nothing is allowed to break it.

## A CLI for the mechanical parts

The deterministic operations — the ready scan, claiming, closing, appending ledger lines, checking the frontmatter contract — belong in a small CLI so agents stop hand-rolling frontmatter edits and humans can ask "what's ready?" from any shell. The skill stays the brain; the CLI is hands. A charter for this already exists in my private setup; the contract in [CONVENTIONS.md](CONVENTIONS.md) is written so the CLI can arrive without changing a single file already on disk.

## Many workers, one brief

One step per session composes: a steering session charters the brief and fires a worker per ready AFK step, each claiming before work, each unfolding the brief when it lands. The claim discipline and the 24-hour staleness rule exist precisely so concurrent sessions — human-driven and autonomous — can share a brief without stepping on each other. The ceiling here is a brief being worked by a fleet while you sleep, with the grilling questions queued up waiting for you at breakfast.

## Grilling by voice

The HITL steps are conversations, and conversations don't need a keyboard. The open design question in my setup: when a phone call runs a grilling session, which layer drives — a fast voice loop with tracker-writing tools, or the engine session relaying through voice? Either way the brief is the shared state, and a decision made while walking the dog lands in the same ledger as one made at the desk.

## Briefs as rendered pages

Briefs are structured markdown with frontmatter — which means they render. A brief page that shows the finish line, the live ready steps, and the ledger as it grows turns planning state into something you read over coffee rather than something you query. In my setup that's the MDSvX wiki; the format carries it anywhere.

## Upstream, both directions

This repo tracks its ancestor. Matt Pocock's [wayfinder](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md) keeps evolving — the day this fork shipped, upstream landed subagent research burn-down (adopted) and renamed its unit to "decision ticket" (declined at the time; real usage later pushed ours from "question" to "step" — same wall, hit from the other side). The `basis:` line in SKILL.md exists so every future edit starts by checking what moved upstream. Mechanics that get better there get stolen here; if something here proves out, it's MIT — steal it back.

## What won't change

- Mechanics keep boring names. Status, blockers, assignee, finish line — legible to any agent that never read the lore.
- One step per session. The unfolding rule needs a settled brief between moves.
- Decide, don't implement — by default. Execution is a granted authorization on the brief, never an assumption.
- The metaphor budget stays two words: sessions grill, briefs unfold.
