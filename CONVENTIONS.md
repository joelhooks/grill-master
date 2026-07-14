# grill-master conventions

The tracker is the filesystem: `.brain/projects/<effort>/` in whichever repo owns the effort. Files are `.svx` in my MDSvX-based setup. Frontmatter is the machine surface; the scan reads it, so follow it exactly.

## Layout

```
.brain/projects/<effort>/
├── <effort>-brief.svx          # the brief (one per effort)
├── <verb-slug>.svx             # one file per question
└── <asset-slug>.svx            # assets created by resolutions
```

## Brief frontmatter + body

```markdown
---
title: "<Human-Readable Effort Name>"
type: "brief"
status: "active"            # → "done" when the last question closes
created_at: "YYYY-MM-DD"
privacy: "private"
---

# <Title>

## Finish line
<observable conditions that end the effort, incl. how the result stays maintained>

## Vocabulary
- **<term>** — <the settled meaning, one line>

## Notes
<domain; skills to consult; mid-effort calls (attributed, dated); execution authorization if granted>

## Decision ledger
- [<closed question title>](./<file>.svx) — <one-line gist of the answer>

## Not yet specified
- <soft unknown, one line each>

## Out of scope
- <ruled-out work + why, linking any closed question>
```

## Question frontmatter + body

```markdown
---
title: "<The Question, As a Title>"
type: "question"
kind: "grilling"            # research | prototype | grilling | task
interaction: "HITL"         # HITL | AFK
status: "open"              # → "closed" (+ closed_at) on resolution
assignee: ""                # empty = unclaimed; see Claims
parent: "./<effort>-brief.svx"
blockers: []                # relative links to blocking question files
created_at: "YYYY-MM-DD"
---

# <Title>

## Question
<the decision or investigation, sized to one session>

## Answer (YYYY-MM-DD)          ← added at resolution
<the decision, its consequences, links to assets>
```

Assets: `type: "asset"`, `parent:` pointing at the question that produced them, plus `title`/`created_at`/`privacy`.

## Claims

Claim format: `assignee: "<agent> (<machine>, <surface>, YYYY-MM-DD)"` — e.g. `"claude (studio, herdr pane w1:p2, 2026-07-13)"`. Set it **before** any work on the question. A claim dated more than 24 hours ago on a still-open question is dead: overwrite it and add one body line noting the takeover.

## The ready scan

Ready = open + unclaimed (or stale-claimed) + every blocker closed. The scanner ships with this skill — run it, never re-type it:

```bash
python3 ~/.claude/skills/grill-master/scan.py <effort-dir>    # defaults to cwd; adjust to your install path
```

An empty result with open questions remaining means everything is blocked or claimed — read the brief to see what's in flight.

## Worker task files

When firing a worker at an AFK question, write its instructions to `.brain/tasks/<effort>-<question-slug>.svx`: point at the brief and the claimed question file, state the deliverables as file edits (answer section, status flip, ledger line, assets), and end with "work autonomously, do not commit, print a DONE summary." The steering session reviews and commits. This is a **task file** — never call or name it a brief; that word is reserved for the effort's working brief.

## Commit discipline

Durable edits commit and push the same session. Workers never commit — the steering session reviews, stages the effort's files explicitly (never `git add -A`), commits, pushes.
