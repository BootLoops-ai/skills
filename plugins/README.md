# plugins/ (generated; do not edit)

Everything under `plugins/`, together with `.claude-plugin/marketplace.json`
and `.agents/plugins/marketplace.json` at the repository root, is written by
[`tools/make_plugins.py`](../tools/make_plugins.py) from the
[`skills/`](../skills/README.md) library. Never edit these files by hand:
edit `skills/<name>/SKILL.md`, then regenerate with

    python3 tools/make_plugins.py --force

and commit the result. `python3 tools/make_plugins.py --check` reports
whether the committed tree is up to date.

The two plugins are the opt-in granularity for plugin users (plugin systems
enable whole plugins, not single skills); clone users choose per skill with
`/bootloops-setup`.

| plugin | skills |
|---|---|
| `bootloops-protocols` | acceptance-gate, constant-recognition, planted-truth, independence-bookkeeping, timing-discipline, reading-contract, tool-stewardship |
| `bootloops-research` | prove-protocol, referee-sim, lit-review, ref-check, prose-lint |

Each plugin directory carries a Claude Code manifest (`.claude-plugin/plugin.json`),
a Codex manifest (`.codex-plugin/plugin.json`), a portable Agent Plugins
manifest (`plugin.json`), copies of its skills under `skills/`, and the
license files.

Claude Code:

    /plugin marketplace add BootLoops-ai/skills
    /plugin install bootloops-protocols@bootloops
    /plugin install bootloops-research@bootloops

Codex:

    codex plugin marketplace add BootLoops-ai/skills

then open `/plugins` in the Codex CLI (or the Plugins tab of the app) and
install from the `bootloops` marketplace. Every route is described in the
repository [README](../README.md).
