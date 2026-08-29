# My AI Skills

**Reusable AI skills and agent definitions for software development work.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-31-brightgreen)](skills/)
[![Agents](https://img.shields.io/badge/agents-4-blue)](agents/)

## What's included

- Focused skills for coding, design, GitHub workflows, reviews, and technical writing
- Specialist agents for general development, n8n, read-only analysis, and web research
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

- Markdown with YAML frontmatter for agent and skill definitions
- UAM files for Universal Agent Manager
- Python 3 standard library for format synchronisation

## Install

Clone the repository, then copy the skills or agents you want into the matching directory for your AI tool.

```bash
git clone https://github.com/davidtaylor6130/My-AI-Skills.git
```

For Universal Agent Manager, import the `skills/` directory. For standard skill agents, use the directories containing `SKILL.md` and ignore the `.uam` files.

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

## Status

The collection is maintained on the `main` branch. Report stale instructions or broken workflows through [GitHub Issues](https://github.com/davidtaylor6130/My-AI-Skills/issues).

## License

[MIT](LICENSE) © 2026 David Taylor
