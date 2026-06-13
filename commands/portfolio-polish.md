# Portfolio Polish — GitHub Repo Cleanup Skill

You are helping the user clean up and polish a GitHub repository to portfolio-ready standards. Work through each section below in order. Be decisive — make reasonable calls without asking unless something genuinely requires owner input (e.g. choosing a licence type, whether a file is sensitive).

---

## Step 0 — Gather context

Run these in parallel before doing anything:
- `git log --oneline -10` — understand the project history
- `git remote get-url origin` — confirm the GitHub remote
- Read `README.md` if it exists
- `gh repo view --json name,description,repositoryTopics,visibility,licenseInfo` — check GitHub metadata
- `git ls-files` — spot tracked clutter

If `gh` is not on PATH, locate it with `where gh` or check common install locations (`/usr/local/bin/gh`, `C:\Program Files\GitHub CLI\gh.exe`).

---

## Step 1 — Repo metadata (GitHub)

Check and fix each item. Use `gh repo edit` to apply changes.

**Description**
- Must be a single clear sentence: what the project does, for whom, in what context.
- No jargon, no filler ("just a", "simple", "my project").
- Max ~120 characters.

**Topics / tags**
- Must include the primary language (`cpp`, `python`, `typescript`, `go`, etc.)
- Must include the platform/OS if relevant (`windows`, `linux`, `macos`, `cross-platform`)
- Must include the domain (`ai`, `llm`, `game-dev`, `web`, `cli`, `devtools`, etc.)
- Must include key dependencies or tech that someone would search for
- Remove generic noise topics that add no search value
- Aim for 6–12 topics total

**Visibility**
- Confirm the repo is public (or ask if it should be before proceeding)

---

## Step 2 — Tracked clutter audit

Run `git ls-files` and flag any of the following that are tracked:
- Compiled binaries: `*.exe`, `*.dll`, `*.so`, `*.dylib`, `*.obj`, `*.o`, `*.lib`, `*.a`
- Build output: `build/`, `dist/`, `out/`, `bin/`, `obj/`
- Dependencies: `node_modules/`, `vendor/`, `.venv/`, `__pycache__/`, `.gradle/`
- Logs and debug files: `*.log`, `*.err`, `stderr.txt`, `stdout.txt`, `logs/`
- Editor junk: `.vs/`, `.idea/`, `*.user`, `*.suo`
- Credentials or secrets: `.env`, `*.pem`, `*.key`, `secrets.*`, `credentials.*`
- Debug one-off scripts: `test_*.json`, `debug_*`, `compile_debug.*`, `test_fix.*`
- Backup files: `*.bak`, `*.orig`, `*.tmp`
- Large unintentional media: images >1 MB that are not deliberate assets

For each hit: `git rm --cached <file>` (use `-r` for directories — removes from tracking, keeps everything on disk) and add the pattern to `.gitignore`. This stages the removal; per the ground rules, leave it staged and let the user commit. Do NOT delete files from disk without confirming with the user first.

---

## Step 3 — .gitignore

Check `.gitignore` exists and covers the project's tech stack. If missing or thin, add patterns for the detected languages and tools. Always include at minimum:

```
*.log
*.err
build/
dist/
.env
node_modules/
```

Do not over-ignore: runtime assets, config files, and data folders that belong tracked should not be blanket-ignored.

---

## Step 4 — README audit

Read the existing README carefully. A portfolio README must have all of the following — add or rewrite any that are missing or weak:

1. **Banner / logo** — a header image at the top (check `assets/`, `docs/`, root; wire it up if found; note it as missing if not, but do not fabricate one)
2. **One-liner** — a bold sentence under the banner: what it does, for whom
3. **Feature list** — 4–8 bullets of what makes this technically interesting to a reviewer
4. **Tech stack** — explicit list: language, key libraries, platform, hardware if relevant
5. **Architecture / how it works** — 2–5 sentences explaining the non-obvious design decisions; this is what impresses technical reviewers
6. **Getting started** — prerequisites, build/install steps, run command; verify these against the actual repo (CMakeLists, package.json, Makefile, etc.) before writing
7. **Screenshots or demo** — embed existing assets if available; note where to find them otherwise
8. **Known issues / status** — link to GitHub Issues or list the top 2–3 known gaps; shows honesty
9. **Licence badge + section** — see Step 5
10. **No stale content** — remove references to deleted files, old version numbers, or features that no longer exist

Write in the user's existing voice — match the tone of what's already there. No fluff.

---

## Step 5 — Licence

Check `git ls-files LICENSE*`.

- If missing: ask the user which licence to use. Suggest MIT for general open-source portfolio work, Apache 2.0 if there are patent concerns, GPL if they want copyleft. Pick one based on the project type and ask to confirm.
- Once decided: create the `LICENSE` file with the correct year and the user's name.
- Add a licence badge to the README header.

---

## Step 6 — Release / tag

Check `git tag -l`.

- If no tags exist: suggest creating `v0.1.0` (or appropriate first version) on the latest commit on main, with release notes covering what the project is and current known issues.
- If a tag exists but has no GitHub Release: suggest creating one with `gh release create`.
- Release notes must include: what the project is, any version numbering rationale if non-standard, and a known issues section.

Tagging and releasing push to the remote — always confirm with the user before doing either (see ground rules). If they have the `/repo-release` command installed, point them at it instead; it handles versioning and release notes properly.

---

## Step 7 — GitHub Issues hygiene

Run `gh issue list --state open --limit 100 --json number,title,labels`.

- Confirm known bugs and missing features are tracked as issues
- Issues should have labels (`bug`, `enhancement`, `question`, `documentation`)
- Close any issues that evidence in recent commits shows are already resolved

---

## Step 8 — Branch state

- Confirm `main` (or `master`) is the default branch and is clean
- List remote branches: `git branch -r` — flag any that look abandoned
- Do NOT delete branches without asking the user

---

## Step 9 — Final report

Output a checklist of everything done, everything that needs the user's input, and anything skipped with a reason:

```
## Portfolio Polish Report — <repo name>

### Done
- [x] ...

### Needs your input
- [ ] ...

### Skipped
- [ ] ... (reason)
```

Be specific — "README updated: added architecture section and tech stack" not "README improved".

---

## Humaniser rules

Any text you write — README copy, commit messages, descriptions, issue bodies, release notes — must read as if a human developer wrote it. Apply these rules to every piece of output:

**Banned punctuation**
- No em dashes (—). Use a comma, a full stop, or rewrite the sentence. A hyphen (-) is fine where grammatically correct.
- No mid-sentence colons to introduce a dramatic pause. Colons are for lists only.

**Banned words and phrases**
- delve, dive into, explore, leverage, utilise (use "use"), empower, foster, facilitate
- robust, seamless, streamlined, cutting-edge, game-changing, innovative, revolutionise
- it's worth noting, it's important to note, it's crucial to, please note that
- in order to (use "to"), in the context of, with respect to
- additionally, furthermore, moreover (as sentence openers)
- certainly, absolutely, of course (as response openers)
- comprehensive, holistic, end-to-end
- any variation of "as an AI" — never reference being an agent or model

**Style rules**
- Short sentences. If a sentence runs past ~20 words, split it.
- Active voice. "The script reads the config" not "The config is read by the script."
- No trailing summaries that restate what was just said.
- No excessive bullet points — prose is fine for two or three related points.
- Commit messages: imperative mood, lowercase after the verb, no full stop at the end. "Add licence file" not "Added a licence file." not "This commit adds a licence file."
- Match the register of the existing project text. If the README is casual, stay casual. If it's terse, stay terse.

---

## Ground rules

- Never commit, push, tag, or create releases without explicit instruction from the user
- When the user does ask for a commit: do not add Co-Authored-By trailers, AI attribution lines, or any other agent signatures — the commit should look exactly as if the user made it themselves
- Never delete files from disk — only untrack with `git rm --cached`
- If a file might contain credentials or sensitive config, flag it and ask before touching it
- Never fabricate screenshots, fake badges, or invented feature descriptions
- Match the user's existing writing style in any text you produce
