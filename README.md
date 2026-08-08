[![MIT License](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

# My AI Skills

Reusable AI skills and specialist agent definitions. Skills follow the standard
`skills/<name>/SKILL.md` layout; agent definitions live in `agents/`.

## Install

Clone the repository:

```bash
git clone https://github.com/davidtaylor6130/My-AI-Skills.git
```

Install one skill for Codex:

```bash
cp -R My-AI-Skills/skills/<skill-name> ~/.codex/skills/
```

Install every skill:

```bash
cp -R My-AI-Skills/skills/* ~/.codex/skills/
```

Agent definitions are separate. Copy the required file from `agents/` into the
agent directory supported by your tool, such as `~/.config/opencode/agents/`.

GitHub skills require the [GitHub CLI](https://cli.github.com/) and an
authenticated session:

```bash
gh auth login
```

## Skills

### GitHub

- `github-fix-issue` — take an issue from investigation to an approved pull request
- `github-issue-creator` — deduplicate and create labelled issues
- `github-issue-sweep` — find codebase debt and turn approved findings into issues
- `github-repo-cleanup` — prepare a repository for a public or portfolio release
- `github-version-tag-release` — update versions, tag, and publish a release

### Notes and analysis

- `analyse-logs` — classify noisy logs and issue an evidence-based verdict
- `quick-read` — search and read focused Obsidian notes
- `obsidian-save` — save and cross-link notes using PARA
- `optimise-model-prompt` — test prompt changes against a named model
- `security-audit` — audit a repository before public release

### Design

- `design` — general UI review and polish rules
- `de-vibe-design` — remove generic AI styling and rebuild task-first interfaces

## Agents

- `n8n.md` — n8n workflow specialist
- `obsidian-agent.md` — multi-folder Obsidian research
- `read-only.md` — inspection without file changes
- `web-research.md` — web research without editing the working tree

## Repository layout

```text
agents/
  <agent>.md
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml    # optional UI metadata
    references/           # optional supporting material
    scripts/              # optional reusable automation
```

## Contributing

Keep each skill self-contained. Every skill requires valid YAML frontmatter
with only `name` and `description`, followed by concise operational
instructions. Keep standalone agent definitions in `agents/`.

## Licence

MIT — David Taylor
