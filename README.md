[![MIT License](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

# My-AI-Skills

Custom slash commands and agent files for AI coding agents (Claude Code, Cursor, Copilot, Zed). Drop them into your agent's commands directory and use them in any project.

Each command is a single `.md` file that tells an AI how to do something step by step: clean up repos, file issues, cut releases, automate tasks. You own the files. Edit them directly.

---

## Installation

**Commands (slash commands):**
```bash
# Clone the repo
git clone https://github.com/davidtaylor6130/My-AI-Skills.git

# Copy commands into your agent's commands directory
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

You may need to create the commands directory yourself. Check your agent's docs for the exact path.

All commands require the [GitHub CLI](https://cli.github.com/) (`gh`). Install it and run `gh auth login` before using anything that touches GitHub.

---

## Commands

### `/github-repo-cleanup`
Full audit and cleanup of a GitHub repo to portfolio-ready standards. It checks repo description, topics, tracked clutter, `.gitignore`, README completeness, licence file, release tags, issue hygiene, branch state, then gives you a checklist report so you know what was done and what still needs input.

Use it when preparing a repo to show employers or making a side project public.

---

### `/version-tag-release`
Walks you through tagging a release and writing proper release notes instead of just listing file changes. Finds the version number, confirms the target commit, writes notes from recent commits and open issues, then creates the git tag and GitHub release.

Use it when shipping a version and want release notes that actually say something useful.

---

### `/issue-sweep`
Scans your codebase for TODOs, FIXMEs, and deferred work, files them as GitHub Issues. Searches inline markers (`TODO`, `FIXME`, `HACK`, `XXX`), checks recent commits for hints of untracked debt, categorises findings by type, confirms the list with you, then files each one properly labelled.

Use it when you know there's debt in the codebase but it's not tracked anywhere.

---

## Agents

These are opencode agent definition files (`~/.config/opencode/agents/` or project-level). They define specialised AI assistant behaviour with specific tool access and constraints.

### `n8n.md`
N8N workflow automation specialist. The only agent in this repo with n8n tools (node search, templates, validation) and skills. Handles building, debugging, validating, and configuring n8n workflows, nodes, credentials, and MCP tool interactions.

Use it for node configuration, workflow architecture, validation errors, expression syntax, or Code node patterns.

---

### `read-only.md`
A strictly read-only agent that inspects, searches, and analyzes code but never writes or modifies any files. It will explain what needs changing and give you exact commands to handle yourself.

Use it when you need analysis or review but don't want the agent to touch any files.

---

### `web-research.md`
A web research agent that uses SearXNG MCP search plus Puppeteer screenshots. The usual place you'd open a browser, except done from the terminal.

Use it for researching documentation, checking API behaviour, or gathering information about tools and services without editing files.

---

## How custom commands work

Each `.md` file in your agent's commands directory becomes a slash command named after the file (without `.md`). When you type `/github-repo-cleanup` in your agent, it reads that file and follows the instructions for your current project.

They are plain markdown. Open any of them, edit the instructions, and they change immediately. No rebuild. No restart.

**Project-level commands** (only available in one repo) go in a `.commands/` or `.<agent>/commands/` folder inside that repo instead. Check your agent's documentation for where to put them.

---

## Contributing

PRs welcome. Keep each command self-contained in a single `.md` file. Commands should:
- State clearly what they do and don't do
- Confirm with the user before any destructive or irreversible action
- Work across different tech stacks without hardcoded assumptions
- Include a Ground rules section at the bottom

---

## Known issues / Status

- Commands are tested primarily with Claude Code; behaviour in Cursor and other agents may vary
- No automated tests. Commands are prompt files, so validation is manual

---

## Licence

MIT — David Taylor
ENDOFFILE && echo "README updated"