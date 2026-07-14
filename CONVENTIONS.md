# grill-master conventions

The tracker is the filesystem: `.brain/projects/<effort>/` in whichever repo owns the effort. Files are `.svx` in my MDSvX-based setup. Frontmatter is the machine surface; the scan below reads it, so follow it exactly.

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
<observable conditions that end the effort, incl. how the result stays maintained — one or two lines>

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
assignee: ""                # empty = unclaimed; see claim rules
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

Ready = open + unclaimed (or stale-claimed) + every blocker closed. Deterministic, no tooling dependency:

```bash
python3 - "$PWD" <<'EOF'
import os, re, sys, datetime
d = sys.argv[1] if len(sys.argv) > 1 else '.'
today = datetime.date.today()
def fmatter(p):
    t = open(p).read().split('---')
    return t[1] if len(t) > 2 else ''
def field(fm, k):
    m = re.search(rf'^{k}:\s*"?([^"\n]*)"?\s*$', fm, re.M)
    return m.group(1).strip() if m else ''
def deps(fm):
    m = re.search(r'^blockers:\n((?:\s+-\s+.*\n)*)', fm, re.M)
    return re.findall(r'([\w-]+\.svx)', m.group(1)) if m else []
files = {f: fmatter(os.path.join(d, f)) for f in os.listdir(d) if f.endswith('.svx')}
closed = {f for f, fm in files.items() if field(fm, 'status') == 'closed'}
def live(a):
    m = re.search(r'(\d{4}-\d{2}-\d{2})', a)
    return bool(m) and (today - datetime.date.fromisoformat(m.group(1))).days < 1
for f, fm in sorted(files.items()):
    if field(fm, 'type') != 'question' or field(fm, 'status') != 'open': continue
    if live(field(fm, 'assignee')): continue
    if all(b in closed for b in deps(fm)):
        print(f, '—', field(fm, 'title'))
EOF
```

Run it from the effort directory; it prints the ready questions. An empty result with open questions remaining means everything is blocked or claimed — read the brief to see what's in flight.

## Worker task files

When firing a worker at an AFK question, write its brief to `.brain/tasks/<effort>-<question-slug>.svx`: point at the brief and the claimed question file, state the deliverables as file edits (answer section, status flip, ledger line, assets), and end with "work autonomously, do not commit, print a DONE summary." The steering session reviews and commits.

## Commit discipline

Durable edits commit and push the same session. Workers never commit — the steering session reviews, stages the effort's files explicitly (never `git add -A`), commits, pushes.
