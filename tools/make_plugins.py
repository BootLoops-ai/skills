#!/usr/bin/env python3
"""Generate the plugin packaging of the BootLoops skills inside this repository.

`skills/` at the repository root is the single source of truth. This script
copies the two plugin groups out of it and writes the manifests that Claude
Code and Codex read, all inside the same repository:

    plugins/<plugin>/skills/<skill>/SKILL.md      copies of skills/<skill>/
    plugins/<plugin>/.claude-plugin/plugin.json   Claude Code plugin manifest
    plugins/<plugin>/.codex-plugin/plugin.json    Codex plugin manifest
    plugins/<plugin>/plugin.json                  portable Agent Plugins manifest
    plugins/<plugin>/LICENSE, LICENSE-CONTENT, NOTICE
    plugins/README.md                             states that this tree is generated
    .claude-plugin/marketplace.json               Claude Code marketplace ("bootloops")
    .agents/plugins/marketplace.json              Codex marketplace ("bootloops")

Usage:
    python3 tools/make_plugins.py            # write the tree; refuse if it exists
    python3 tools/make_plugins.py --force    # remove the generated tree, rewrite it
    python3 tools/make_plugins.py --check    # exit 1 if the committed tree is stale
    python3 tools/make_plugins.py --out DIR  # write the same tree under DIR instead
    python3 tools/make_plugins.py --force --slug ORG/REPO
                                             # regenerate for a copy of this repository
                                             # published as github.com/ORG/REPO

The one host-specific constant is REPO_SLUG, the `ORG/REPO` slug that
`/plugin marketplace add` and the manifests' "repository" field need; it names
the organization currently hosting this repository. A copy published under
another organization regenerates its plugin tree with `--slug` (and checks it
with `--check --slug`). Everything written is a pure function of `skills/`, the
license files, the slug and the constants below, so "edit skills/, re-run with --force, commit" is the whole
release procedure for the plugin routes. The generated files are never edited
by hand. The Codex manifest and marketplace schemas move faster than Claude
Code's; validate both against the current documentation at release time
(`claude plugin validate .` checks the Claude Code side locally).
"""
import argparse
import filecmp
import io
import json
import os
import shutil
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_SLUG = "BootLoops-ai/skills"   # ORG/REPO of the current host; override with --slug
REPO_URL = "https://github.com/" + REPO_SLUG
HOMEPAGE = "https://www.bootloops.ai"
OWNER = {"name": "Matthew D. Schwartz", "url": HOMEPAGE}
VERSION = "1.0.0"
LICENSE_ID = "CC-BY-4.0 AND MIT"   # skill texts: CC BY 4.0; scripts and manifests: MIT
MARKETPLACE = "bootloops"
MARKETPLACE_BLURB = ("The BootLoops harness: working protocols for trustworthy "
                     "agent-driven science.")
KEYWORDS = ["science", "verification", "protocols", "agent-skills", "bootloops"]
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
LICENSE_FILES = ("LICENSE", "LICENSE-CONTENT", "NOTICE")

GROUPS = {
    "bootloops-protocols": {
        "title": "BootLoops protocols",
        "short": "Seven disciplines for trustworthy quantitative work with agents.",
        "description": ("The BootLoops protocol layer: seven disciplines for trustworthy "
                        "quantitative work with agents — acceptance gates, integer-relation "
                        "discipline, synthetic-truth controls, provenance bookkeeping, timing "
                        "discipline, sources-only reading, tool stewardship."),
        "skills": ["acceptance-gate", "constant-recognition", "planted-truth",
                   "independence-bookkeeping", "timing-discipline", "reading-contract",
                   "tool-stewardship"],
    },
    "bootloops-research": {
        "title": "BootLoops research skills",
        "short": ("Proving with agents, referee audit, literature review, "
                  "bibliography verification, prose linting."),
        "description": ("The BootLoops research skills: heavier machinery for specific tasks — "
                        "proving with agents (adversary-first pipelines), pre-circulation "
                        "referee audit, the literature review behind a novelty claim, "
                        "bibliography verification, and the scientific-prose linter."),
        "skills": ["prove-protocol", "referee-sim", "lit-review", "ref-check", "prose-lint"],
    },
}

# paths (relative to the output root) that this script owns outright
GENERATED = ("plugins",
             os.path.join(".claude-plugin", "marketplace.json"),
             os.path.join(".agents", "plugins", "marketplace.json"))


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def write_json(path, obj):
    write_text(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def skill_summary(skill_dir):
    """Return the frontmatter `name` of skills/<dir>/SKILL.md (checked against the dir)."""
    path = os.path.join(REPO, "skills", skill_dir, "SKILL.md")
    if not os.path.isfile(path):
        sys.exit(f"missing skill: skills/{skill_dir}/SKILL.md")
    with io.open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if not lines or lines[0].strip() != "---":
        sys.exit(f"skills/{skill_dir}/SKILL.md has no frontmatter")
    name = None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
    if name != skill_dir:
        sys.exit(f"skills/{skill_dir}/SKILL.md: frontmatter name {name!r} != directory name")
    return name


def plugin_readme():
    rows = "\n".join(f"| `{plug}` | {', '.join(spec['skills'])} |"
                     for plug, spec in GROUPS.items())
    return f"""# plugins/ (generated; do not edit)

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
{rows}

Each plugin directory carries a Claude Code manifest (`.claude-plugin/plugin.json`),
a Codex manifest (`.codex-plugin/plugin.json`), a portable Agent Plugins
manifest (`plugin.json`), copies of its skills under `skills/`, and the
license files.

Claude Code:

    /plugin marketplace add {REPO_SLUG}
    /plugin install bootloops-protocols@{MARKETPLACE}
    /plugin install bootloops-research@{MARKETPLACE}

Codex:

    codex plugin marketplace add {REPO_SLUG}

then open `/plugins` in the Codex CLI (or the Plugins tab of the app) and
install from the `{MARKETPLACE}` marketplace. Every route is described in the
repository [README](../README.md).
"""


def generate(out):
    for plug, spec in GROUPS.items():
        pdir = os.path.join(out, "plugins", plug)
        for s in spec["skills"]:
            skill_summary(s)
            shutil.copytree(os.path.join(REPO, "skills", s), os.path.join(pdir, "skills", s))
        common = {
            "name": plug,
            "version": VERSION,
            "description": spec["description"],
            "author": OWNER,
            "homepage": HOMEPAGE,
            "repository": REPO_URL,
            "license": LICENSE_ID,
            "keywords": KEYWORDS,
        }
        # Claude Code plugin manifest; skills/ at the plugin root is auto-discovered
        write_json(os.path.join(pdir, ".claude-plugin", "plugin.json"), dict(common))
        # Codex plugin manifest (read on its own, or as the OpenAI overlay of plugin.json)
        codex = dict(common)
        codex["skills"] = "./skills/"
        codex["interface"] = {
            "displayName": spec["title"],
            "shortDescription": spec["short"],
            "longDescription": spec["description"],
            "developerName": OWNER["name"],
            "category": "Productivity",
            "websiteURL": HOMEPAGE,
        }
        write_json(os.path.join(pdir, ".codex-plugin", "plugin.json"), codex)
        # portable Agent Plugins manifest (vendor-neutral; skills/ auto-discovered)
        portable = {"$schema": PORTABLE_SCHEMA}
        portable.update(common)
        write_json(os.path.join(pdir, "plugin.json"), portable)
        for lic in LICENSE_FILES:
            src = os.path.join(REPO, lic)
            if os.path.isfile(src):
                shutil.copy2(src, os.path.join(pdir, lic))

    # Claude Code marketplace: `/plugin marketplace add <owner>/<repo>` reads this file
    write_json(os.path.join(out, ".claude-plugin", "marketplace.json"), {
        "name": MARKETPLACE,
        "owner": OWNER,
        "metadata": {"description": MARKETPLACE_BLURB, "version": VERSION},
        "plugins": [
            {
                "name": plug,
                "source": f"./plugins/{plug}",
                "description": spec["description"],
                "version": VERSION,
                "author": OWNER,
                "homepage": HOMEPAGE,
                "repository": REPO_URL,
                "license": LICENSE_ID,
                "keywords": KEYWORDS,
                "category": "productivity",
            }
            for plug, spec in GROUPS.items()
        ],
    })
    # Codex marketplace: `codex plugin marketplace add <owner>/<repo>` reads this file
    write_json(os.path.join(out, ".agents", "plugins", "marketplace.json"), {
        "name": MARKETPLACE,
        "interface": {"displayName": "BootLoops skills"},
        "plugins": [
            {
                "name": plug,
                "source": {"source": "local", "path": f"./plugins/{plug}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Productivity",
            }
            for plug in GROUPS
        ],
    })
    write_text(os.path.join(out, "plugins", "README.md"), plugin_readme())


def set_slug(slug):
    """Point the generated manifests and plugins/README.md at github.com/<slug>."""
    global REPO_SLUG, REPO_URL
    org, sep, repo = slug.partition("/")
    if not sep or not org or not repo or "/" in repo or " " in slug:
        sys.exit(f"--slug must be ORG/REPO, got {slug!r}")
    REPO_SLUG = slug
    REPO_URL = "https://github.com/" + slug


def existing(out):
    return [p for p in GENERATED if os.path.lexists(os.path.join(out, p))]


def remove_generated(out):
    for p in GENERATED:
        full = os.path.join(out, p)
        if os.path.isdir(full) and not os.path.islink(full):
            shutil.rmtree(full)
        elif os.path.lexists(full):
            os.remove(full)


def trees_equal(a, b):
    """True if directory trees a and b hold the same files with the same bytes."""
    if os.path.isdir(a) != os.path.isdir(b):
        return False
    if not os.path.isdir(a):
        return os.path.isfile(a) and os.path.isfile(b) and filecmp.cmp(a, b, shallow=False)
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(trees_equal(os.path.join(a, d), os.path.join(b, d)) for d in cmp.common_dirs)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default=REPO,
                    help="output root (default: the repository root)")
    ap.add_argument("--force", action="store_true",
                    help="remove the existing generated tree first")
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if the tree under --out is stale")
    ap.add_argument("--slug", default=REPO_SLUG, metavar="ORG/REPO",
                    help="GitHub slug of the repository the tree is generated for "
                         f"(default: {REPO_SLUG}, the current host); a copy published "
                         "under another organization regenerates with its own slug")
    args = ap.parse_args(argv)
    set_slug(args.slug)
    out = os.path.abspath(args.out)
    n = sum(len(s["skills"]) for s in GROUPS.values())

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            generate(tmp)
            stale = [p for p in GENERATED
                     if not trees_equal(os.path.join(tmp, p), os.path.join(out, p))]
        if stale:
            hint = "" if args.slug == ap.get_default("slug") else f" --slug {args.slug}"
            print("stale: " + ", ".join(stale) + f" (run: python3 tools/make_plugins.py --force{hint})")
            return 1
        print(f"up to date: {len(GROUPS)} plugins, {n} skills")
        return 0

    found = existing(out)
    if found and not args.force:
        print("refusing to overwrite existing " + ", ".join(found) +
              f" under {out} (re-run with --force)", file=sys.stderr)
        return 2
    if found:
        remove_generated(out)
    generate(out)
    print(f"generated under {out}: {len(GROUPS)} plugins, {n} skills (slug {REPO_SLUG})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
