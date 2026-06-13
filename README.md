# agent-commands

A collection of custom slash commands / prompt files for AI coding agents (Claude Code, Cursor, Copilot, Zed, etc.) — drop them into your agent's commands directory and use them across any project.

These are prompt-driven commands that guide an AI agent through multi-step workflows: cleaning up repos, filing issues, cutting releases. Each one is a single `.md` file you own and can edit.

---

## Installation

**Global (available in every project):**
```bash
# Clone the repo
git clone https://github.com/davidtaylor6130/agent-commands.git

# Copy commands into your agent's commands directory
# Claude Code: ~/.claude/commands/
# Cursor: ~/.cursor/commands/
# VS Code Copilot: ~/.vscode/copilot/commands/
# Zed: ~/.config/zed/commands/
cp agent-commands/commands/*.md <your-agent-commands-dir>/
```

**Single command:**
```bash
curl -o <your-agent-commands-dir>/portfolio-polish.md \
  https://raw.githubusercontent.com/davidtaylor6130/agent-commands/main/commands/portfolio-polish.md
```

**Windows (PowerShell):**
```powershell
Copy-Item "agent-commands\commands\*.md" "<your-agent-commands-dir>\"
```

> Create the commands directory manually if it doesn't exist. Check your agent's documentation for the exact path.

**Prerequisites:** all three commands use the [GitHub CLI](https://cli.github.com/) (`gh`) for issues, releases, and repo metadata. Install it and run `gh auth login` once before using them.

---

## Commands

### `/portfolio-polish`
Full audit and cleanup of a GitHub repo to portfolio-ready standards.

Checks and fixes: repo description, topics/tags, tracked clutter, `.gitignore`, README completeness (banner, features, tech stack, architecture, getting started, licence), licence file, release tags, issue hygiene, branch state. Ends with a checklist report of what was done and what needs your input.

**Use when:** preparing a repo to show to employers or making a side project public.

---

### `/repo-release`
Guides you through tagging a release and writing proper release notes.

Determines the version number, confirms the target commit, writes release notes from recent commits and open issues, then creates the git tag and GitHub release.

**Use when:** shipping a version and want release notes that actually say something useful.

---

### `/issue-sweep`
Scans the codebase for TODOs, FIXMEs, and deferred work then files them as GitHub Issues.

Searches inline markers, reviews recent commits for hints, categorises findings by type, confirms the list with you, then files each as a properly labelled issue.

**Use when:** you know there's debt in the codebase but it's not tracked anywhere.

---

## How custom commands work

Each file in your agent's commands directory becomes a slash command named after the file (without `.md`). When you type `/portfolio-polish` in your agent, it reads that file and follows the instructions in the context of your current project.

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

## Licence

MIT — David Taylor
