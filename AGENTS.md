# AGENTS.md

## Repo scope
This repo tracks a single utility: `strip_timestamps.py` (strip timestamps from transcript lines).
Transcript text files (`*conjecture*.txt`, `openchip*.txt`, `*.md` notes) are local-only and must
not be tracked. They are ignored via `.git/info/exclude` — keep them out of git history.

## Commits and pushes
- The assistant commits changes to this repo when asked.
- The user pushes manually. Do not run `git push` or `push` for this repo unless explicitly asked.
