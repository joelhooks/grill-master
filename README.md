# 🌭 grill-master

An agent skill for efforts too big for one session. Those fail by drift: the outcome slides away from the intent, one unshared assumption at a time. grill-master turns a loose idea into a **working brief** — the operator's intent made checkable: finish line, shared vocabulary, open questions, decision ledger — then works it **one question per session** until nothing is left to decide.

The governing move is **the unfolding rule**: answer one question, then re-read the brief as a whole and record what the answer changed. The shape of the work unfolds out of decisions; it isn't territory waiting to be discovered.

## Files

- [`SKILL.md`](SKILL.md) — the skill: the brief, question kinds (research / prototype / grilling / task), claim discipline, charter mode, work mode.
- [`CONVENTIONS.md`](CONVENTIONS.md) — the tracker contract: file layout, frontmatter, the 24-hour claim staleness rule, a deterministic ready-question scan, worker task-file recipe.

The tracker is just files in the repo — no issue tracker, no service. Questions are frontmatter; the frontier is a scan.

## Install

Symlink into wherever your harness reads skills:

```bash
git clone https://github.com/joelhooks/grill-master ~/Code/grill-master
ln -s ~/Code/grill-master ~/.claude/skills/grill-master   # Claude Code
ln -s ~/Code/grill-master ~/.agents/skills/grill-master   # codex / pi / anything reading ~/.agents/skills
```

Then hand it a loose idea: "grill-master this."

## Credit

This is a fork-in-spirit of **[Matt Pocock](https://github.com/mattpocock)'s [wayfinder](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)** ([mattpocock/skills](https://github.com/mattpocock/skills), MIT). The mechanics are wayfinder's — the shared planning artifact, session-sized decision units, blocking and the frontier, claim-by-assign, fog vs. ticket, out-of-scope discipline, one resolution per session. If you want the original explorer-flavored version, use his; it's excellent and actively maintained.

What changed here, and why:

- **The metaphor.** Wayfinder frames planning as exploration — maps, destinations, fog of war. Charming, but the explorer frame hides the central fact of planning: the territory doesn't exist until you decide it. Following the method of Lakoff & Johnson's *Metaphors We Live By* (pick the metaphor whose entailments cause the behavior you need), the central artifact became a plain **brief** governed by one rule borrowed from Christopher Alexander's *The Nature of Order*: the work **unfolds**, one structure-preserving step at a time. The metaphor budget is two words — sessions *grill*, briefs *unfold* — and every mechanical term stays boring on purpose.
- **The unit is a question**, not a ticket — tickets read as implementation work; questions read as decisions.
- **Alignment is the job.** The brief carries a shared **vocabulary** (terms challenged and settled between operator and agent), the finish line includes how the result stays maintained, and the prototype question kind is the favored instrument — something touchable surfaces the misunderstandings prose hides.
- **The tracker is baked in** as plain files with a frontmatter contract and a deterministic scan, instead of delegating to a per-repo tracker doc.
- It pairs with Matt's [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) / grilling skills as the human-in-the-loop engine, and it was written following his [writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) reference.

The design conversation that produced this — five candidate metaphor systems mapped term-for-term onto the mechanics, a highlight/hide analysis of each — was itself run as a brief under these mechanics, questions resolved one session at a time. It dogfoods.

## License

MIT — see [LICENSE](LICENSE). Portions derived from mattpocock/skills, © Matt Pocock, also MIT.
