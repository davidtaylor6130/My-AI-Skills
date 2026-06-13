# claude-commands

A collection of custom slash commands for [Claude Code](https://claude.ai/code) — drop them into `~/.claude/commands/` and use them across any project.

These are prompt-driven commands that guide Claude through multi-step workflows: cleaning up repos, filing issues, cutting releases. Each one is a single `.md` file you own and can edit.

---

## Installation

**Global (available in every project):**
```bash
# Clone the repo
git clone https://github.com/davidtaylor6130/claude-commands.git

# Copy commands into your Claude user directory
cp claude-commands/commands/*.md ~/.claude/commands/
```

**Single command:**
```bash
curl -o ~/.claude/commands/portfolio-polish.md \
  https://raw.githubusercontent.com/davidtaylor6130/claude-commands/main/commands/portfolio-polish.md
```

**Windows:**
```powershell
Copy-Item "claude-commands\commands\*.md" "$env:USERPROFILE\.claude\commands\"
```

> `~/.claude/commands/` is created automatically by Claude Code. If it doesn't exist yet, create it manually.

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

Each file in `~/.claude/commands/` becomes a slash command named after the file (without `.md`). When you type `/portfolio-polish` in Claude Code, it reads that file and follows the instructions in the context of your current project.

They are plain markdown — open any of them, edit the instructions, and they change immediately. No rebuild, no restart.

**Project-level commands** (only available in one repo) go in `.claude/commands/` inside that repo instead.

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
