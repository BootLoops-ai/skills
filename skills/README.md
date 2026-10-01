# skills/ — the harness beyond the code

These are the working protocols of the BootLoops program, written as standalone
instruction files an LLM agent can load and follow. They are as much a part of
the harness as the packages: the code supplies capability, these supply the
discipline that makes its output trustworthy. Each file carries frontmatter
(name, when to use) and a self-contained body; none depends on any private
infrastructure.

**The protocol layer** (general-purpose — load these for any quantitative work):

| skill | what it governs |
|---|---|
| [acceptance-gate](acceptance-gate/SKILL.md) | what "done" means: never-fit digits vs an independent route, positive controls, two-precision stability |
| [constant-recognition](constant-recognition/SKILL.md) | integer-relation discipline: declared candidate rings, height bounds, refusal over invention |
| [planted-truth](planted-truth/SKILL.md) | synthetic-truth controls before real data; corrupted inputs must be caught |
| [independence-bookkeeping](independence-bookkeeping/SKILL.md) | provenance of reference values; no oracle that fed a fit certifies the result |
| [timing-discipline](timing-discipline/SKILL.md) | measure a small run first; a multi-hour projection means restructure, not scale |
| [reading-contract](reading-contract/SKILL.md) | sources-only assertion for document-reading instruments |
| [tool-stewardship](tool-stewardship/SKILL.md) | consult the toolkit first, write code last, document every tool for the next agent |

**The research skills** (heavier machinery for specific kinds of work):

| skill | what it governs |
|---|---|
| [prove-protocol](prove-protocol/SKILL.md) | proving with agents: adversary-first pipelines, skeptic loops, forced diversity — and theory-finding when the statement itself is unknown |
| [referee-sim](referee-sim/SKILL.md) | pre-circulation audit of an outward-facing document: the strongest standard objection from every audience it claims |
| [lit-review](lit-review/SKILL.md) | the literature audit behind a novelty claim: papers read in full text, thoroughness made falsifiable, citation chains both directions |
| [ref-check](ref-check/SKILL.md) | bibliography verification against authoritative sources; the folklore-error traps |
| [prose-lint](prose-lint/SKILL.md) | scientific-prose linter: hype vocabulary, empty structures, agentless prose, honesty and number checks |

To use one, point your agent at the file ("read skills/acceptance-gate/SKILL.md
and hold my result to it") or install the set into your agent framework's skill
mechanism. They are plain markdown; any model can follow them.

Nothing here is active by default — this directory is a library. To choose
which skills to activate, run the shipped installer: in Claude Code, invoke
`/bootloops-setup` (the one skill in `.claude/skills/`), which shows this
roster, asks which skills you want and at what scope, and copies only your
selection into place. Deactivate any skill later by deleting its directory
from the install location.
