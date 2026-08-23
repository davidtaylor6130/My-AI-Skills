# My AI Skills

> A curated collection of reusable skills and specialist agent definitions for AI-assisted development workflows.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-20%2B-brightgreen)](skills/)
[![Agents](https://img.shields.io/badge/agents-5-blue)](agents/)
[![Maintained](https://img.shields.io/badge/maintained-yes-success)](https://github.com/davidtaylor6130/My-AI-Skills/commits/main)

---

## Why this exists

I build tools that solve problems I encounter, then release the useful parts in case they help others. This repository applies that same philosophy to AI agents: a growing library of focused, composable skills and specialist roles I use daily across coding, design, repository management, Obsidian, and product releases.

Each skill gives an agent a focused workflow without bloating every conversation with a massive permanent prompt. Models route normal requests automatically from each skill's frontmatter `description`: a narrow specialist wins over a domain skill, then the generic engineering router. Slash commands are optional, and skill selection never grants permission for external or irreversible actions.

---

## Repository Structure

```text
My-AI-Skills/
├── agents/
│   ├── Agent.md              # Base agent definition
│   ├── n8n.md                # n8n workflow specialist
│   ├── obsidian-agent.md     # Obsidian vault operations
│   ├── read-only.md          # Non-mutating code review
│   └── web-research.md       # Web search & synthesis
├── skills/
│   ├── AI/
│   │   └── optimise-model-prompt/         # Test prompt changes against a named model
│   ├── Coding/
│   │   ├── analyse-logs/                  # Classify noisy logs; issue evidence-based verdict
│   │   ├── bug-find-swarm/                # Discover, reproduce, fix, verify bugs repo-wide
│   │   ├── engineering-workflow/          # Route non-trivial engineering work
│   │   ├── application-security-review/   # Review application trust boundaries
│   │   ├── secret-and-credential-audit/   # Detect credential exposure
│   │   └── public-release-privacy-audit/  # Check public artifacts for private data
│   ├── Design/
│   │   └── de-vibe-design/                # Task-first UI design, review, and polish
│   ├── Github/
│   │   ├── github-fix-issue/              # Issue → investigation → approved PR
│   │   ├── github-issue-creator/          # Deduplicate & create labelled issues
│   │   ├── github-issue-sweep/            # Find codebase debt → actionable issues
│   │   ├── github-repo-cleanup/           # Portfolio-ready repo polish
│   │   └── github-version-tag-release/    # Version, tag, publish releases
│   └── Obsidian/
│       ├── obsidian-save/                 # Save & cross-link notes using PARA
│       └── quick-read/                    # Search & read focused Obsidian notes
├── scripts/
│   └── pair_skill_formats.py             # Sync SKILL.md ↔ .uam formats
├── LICENSE
└── README.md
```

---

## Quick Start

### For Codex / Standard Skill Agents

```bash
# Install skills from this repository
# In your agent config or instructions:
Install the standard skills from https://github.com/davidtaylor6130/My-AI-Skills.
Use the folders containing SKILL.md and ignore every .uam file.
```

### For Universal Agent Manager (UAM)

```bash
# Import the skills/ folder directly in UAM
# It uses .uam files and preserves category structure
# Imports are snapshots — use "Replace" when updating
```

---

## Skill Format

| File | Purpose |
|------|---------|
| `SKILL.md` | Canonical source — works with Codex, OpenCode, and compatible agents |
| `<skill-name>.uam` | Native UAM format — generated from `SKILL.md` via pairing script |

**`SKILL.md` is the single source of truth.** The pairing script copies its instructions into the UAM file while preserving UAM metadata, so both formats stay in sync without manual duplication.

---

## Keeping Formats in Sync

After editing a `SKILL.md` or adding a new skill:

```bash
# Create/update UAM counterparts
python3 scripts/pair_skill_formats.py --write

# Verify every standard skill has a matching UAM file with identical content
python3 scripts/pair_skill_formats.py
```

- Uses Python standard library only — no dependencies to install
- Validates names, descriptions, paths, and instruction bodies match

---

## Using Skills & Agents

**Agents** define a working role (e.g., "n8n specialist", "read-only reviewer").  
**Skills** give that agent a specific workflow (e.g., "security audit", "bug find swarm").

Use either independently, or combine them when the task calls for it:

```text
# Example: Security audit with read-only enforcement
Agent: read-only.md
Skills: skills/Coding/secret-and-credential-audit/ and skills/Coding/public-release-privacy-audit/
```

---

## Contributing

1. **Keep skills self-contained** in the category that best describes them
2. **Use lowercase folder names** matching the skill's `name` field
3. **Keep supporting files inside the skill folder** — no scattered assets
4. **No private paths, credentials, or machine-specific config** in public instructions
5. **Agent definitions** belong in `agents/`
6. **If a change affects both formats**, edit `SKILL.md` and run the pairing script — don't edit `.uam` files directly

---

## Support & Issues

- **Stale instructions, broken workflows, missing provider support** → [GitHub Issues](https://github.com/davidtaylor6130/My-AI-Skills/issues)
- **Questions about a specific skill** → Open an issue with the skill name in the title

---

## License

[MIT License](LICENSE) — David Taylor

---

*Built for developers who want their AI tools to be as composable and version-controlled as their code.*
