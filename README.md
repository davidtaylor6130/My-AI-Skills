# My AI Skills

**Reusable AI skills and agent definitions for software development work.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-31-brightgreen)](skills/)
[![Agents](https://img.shields.io/badge/agents-5-blue)](agents/)

## What's included

- Focused skills for coding, design, GitHub workflows, reviews, and technical writing
- Specialist agents for general development, n8n, read-only analysis, code and product review, and web research
- Matching `SKILL.md` and `.uam` files for standard skill agents and Universal Agent Manager
- A Python standard-library script that checks and synchronises both skill formats

## Repository structure

Public content lives in `agents/` and `skills/`. The `scripts/` directory contains only the format pairing tool.

```text
My-AI-Skills/
├── agents/
├── skills/
│   ├── Coding/
│   ├── Design/
│   ├── Generic/
│   ├── Github/
│   └── Review/
├── scripts/
│   └── pair_skill_formats.py
├── LICENSE
└── README.md
```

## Formats

Each skill directory contains:

| File | Used by |
| --- | --- |
| `SKILL.md` | Codex and compatible standard skill agents |
| `<skill-name>.uam` | Universal Agent Manager |

`SKILL.md` is the source of truth. The pairing script copies its instructions into the UAM file while preserving UAM metadata.

## Tech stack

- Markdown with UAM-native frontmatter for agents and standard skill frontmatter for skills
- UAM files for Universal Agent Manager
- Python 3 standard library for format synchronisation

## Install

Clone the repository, then copy the skills or agents you want into the matching directory for your AI tool.

```bash
git clone https://github.com/davidtaylor6130/My-AI-Skills.git
```

For Universal Agent Manager, import the `skills/` directory. For standard skill agents, use the directories containing `SKILL.md` and ignore the `.uam` files.

### UAM agents

The five files in `agents/` use UAM's native agent schema: `version`, `name`, `description`, `mode`, `workspaceAccess`, `skills`, and `delegates`. They are not OpenCode agent configuration files.

- [Agent.md](agents/Agent.md), agent ID `agent`: general development, implementation, and verification; write access.
- [read-only.md](agents/read-only.md): investigate and explain local behaviour without changing files or application state; read access.
- [web-research.md](agents/web-research.md): research external evidence with available search and browser tools; read access.
- [review.md](agents/review.md): one independent review worker, launched by the parent orchestrator in a fresh chat; read access and no delegates.
- [n8n.md](agents/n8n.md): build, debug, and validate n8n workflows within the authorised scope; write access.

Copy the set into the `agents/` directory under UAM's configured data root for global use, or into a project's `.uam/agents/` directory for workspace use. Keep the filenames as supplied. Declared delegates must be present in UAM's catalog; remove references to agents you choose not to install. Read-only, web research, and n8n use `mode: both` so they can be selected directly or called as delegates. The Review Agent is `subagent` only; the general agent is `primary`.

The `skills` lists are allowlists for UAM-control, not just installation hints. Each skill or delegate list accepts at most 16 IDs; swap entries rather than appending beyond that limit. The general agent includes the five GitHub workflows, and the Review Agent includes release-exposure audits. Other specialised skills must be approved in the relevant role before using them through UAM-control. Install listed skills through UAM's Library or Central Setup; the instruction text selects which to use. The n8n agent's eight specialist skills and n8n connection are separate prerequisites and are not included in this repository.

Specialists do not automatically inherit `Agent.md`. To share David's preferences across roles, supply its Markdown instruction body through UAM's central instructions as well as installing the agent. Its shared-guidance clause preserves each selected specialist's narrower role and access boundary. The skills-sync script also copies only that body into global Codex instructions.

## Maintain paired formats

The script uses Python 3 and has no third-party dependencies.

```bash
# Check every pair
python3 scripts/pair_skill_formats.py

# Create missing pairs and sync changed SKILL.md files
python3 scripts/pair_skill_formats.py --write
```

## How it works

Agents define a working role. Skills provide narrower instructions that tools can select from their frontmatter descriptions. Keeping both formats beside each other makes each skill portable without maintaining two instruction bodies by hand.

Every completed change passes the parent-owned [independent review gate](skills/Coding/adversarial-review/SKILL.md). Its default coverage is two reviewers minimum, three for substantial behaviour or instruction changes, and four for high-consequence work. The parent discovers available models and launches fresh [Review Agent](agents/review.md) chats, preferring different models of comparable capability. Each worker uses the relevant review or design skills, returns findings, and cannot delegate further.

The parent verifies and adjudicates findings, makes authorised corrections, and obtains independent follow-up reviews of the affected scope. Its own checks never substitute for independent review. Missing reviewer coverage produces `INCOMPLETE`, unresolved material defects produce `NEEDS_WORK`, and `PASSED` requires coverage of the final candidate. Model diversity limits are reported explicitly. Discussion and investigation without changes do not trigger the completion gate.

## Status

The collection is maintained on the `main` branch. Report stale instructions or broken workflows through [GitHub Issues](https://github.com/davidtaylor6130/My-AI-Skills/issues).

## License

[MIT](LICENSE) © 2026 David Taylor
