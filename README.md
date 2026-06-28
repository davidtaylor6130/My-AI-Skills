[![MIT License](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

# My-AI-Skills

A collection of custom slash commands and agent files for AI coding agents (Claude Code, Cursor, Copilot, Zed, etc.) — drop them into your agent's commands directory or opencode config and use them across any project.

These are prompt-driven tools that guide an AI through multi-step workflows: cleaning up repos, filing issues, cutting releases, and automating specialised tasks. Each one is a single `.md` file you own and can edit.

---

## Installation

**Commands (slash commands):**
```bash
# Clone the repo
git clone https://github.com/davidtaylor6130/My-AI-Skills.git

# Copy commands into your agent's commands directory
# Claude Code: ~/.claude/commands/
# Cursor: ~/.cursor/commands/
# VS Code Copilot: ~/.vscode/copilot/commands/
# Zed: ~/.config/zed/commands/
cp My-AI-Skills/commands/*.md <your-agent-commands-dir>/
```

**Single command:**
```bash
curl -o <your-agent-commands-dir>/github-repo-cleanup.md \
  https://raw.githubusercontent.com/davidtaylor6130/My-AI-Skills/main/commands/github-repo-cleanup.md
```

**Agents (opencode):** Copy files into `~/.config/opencode/agents/` or a project's agent config.

**Windows (PowerShell):**
```powershell
Copy-Item "My-AI-Skills\commands\*.md" "<your-agent-commands-dir>\"
```

> Create the commands directory manually if it doesn't exist. Check your agent's documentation for the exact path.

**Prerequisites:** all commands use the [GitHub CLI](https://cli.github.com/) (`gh`) for issues, releases, and repo metadata. Install it and run `gh auth login` once before using them.

---

## Commands

### `/github-repo-cleanup`
Full audit and cleanup of a GitHub repo to portfolio-ready standards.

Checks and fixes: repo description, topics/tags, tracked clutter, `.gitignore`, README completeness (banner, features, tech stack, architecture, getting started, licence), licence file, release tags, issue hygiene, branch state. Ends with a checklist report of what was done and what needs your input.

**Use when:** preparing a repo to show to employers or making a side project public.

---

### `/version-tag-release`
Guides you through tagging a release and writing proper release notes.

Determines the version number, confirms the target commit, writes release notes from recent commits and open issues, then creates the git tag and GitHub release.

**Use when:** shipping a version and want release notes that actually say something useful.

---

### `/issue-sweep`
Scans the codebase for TODOs, FIXMEs, and deferred work then files them as GitHub Issues.

Searches inline markers (`TODO`, `FIXME`, `HACK`, `XXX`), reviews recent commits for hints of untracked debt, categorises findings by type, confirms the list with you, then files each as a properly labelled issue.

**Use when:** you know there's debt in the codebase but it's not tracked anywhere.

---

## Agents

These are opencode agent definition files (`~/.config/opencode/agents/` or project-level). They define specialised AI assistant behaviour with specific tool access and constraints.

### `n8n.md`
N8N workflow automation specialist. The only agent with access to n8n tools (node search, templates, validation) and skills. Handles building, debugging, validating, and configuring n8n workflows, nodes, credentials, and MCP tool interactions.

**Use when:** working on n8n automations — node configuration, workflow architecture, validation errors, expression syntax, or Code node patterns.

---

### `read-only.md`
A strictly read-only agent that can inspect, search, and analyze code but can never write or modify any files. Use for reviewing, debugging, or gathering information without making changes.

**Use when:** you need analysis or review but don't want the agent to touch any files — it will explain what needs changing and provide exact commands or file contents for you to handle.

---

### `web-research.md`
A web research agent that uses SearXNG MCP search plus Puppeteer screenshots. Use when you need to look up anything on the internet without editing files.

**Use when:** researching documentation, checking API behaviour, gathering information about tools or services — anywhere you'd normally open a browser but want it done from the terminal.

---

## How custom commands work

Each `.md` file in your agent's commands directory becomes a slash command named after the file (without `.md`). When you type `/github-repo-cleanup` in your agent, it reads that file and follows the instructions in the context of your current project.

They are plain markdown — open any of them, edit the instructions, and they change immediately. No rebuild, no restart.

**Project-level commands** (only available in one repo) go in a `.commands/` or `.<agent>/commands/` folder inside that repo instead (check your agent's documentation).

---

## Contributing

PRs welcome. Keep each command self-contained in a single `.md` file. Commands should:
- State clearly what they do and don't do
- Confirm with the user before any destructive or irreversible action
- Work across different tech stacks without hardcoded assumptions
- Include a **Ground rules** section at the bottom

---

## Known issues / Status

- Commands are tested primarily with Claude Code; behaviour in Cursor and other agents may vary
- No automated tests — commands are prompt files, so validation is manual

---

## Licence

MIT — David Taylor
ENDOFFILE && echo "README updated"