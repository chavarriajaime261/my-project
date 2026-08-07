# RESTORE-NOTES.md — my-project (frontend harness) restore (2026-08-06)

This folder is the restored frontend-design harness project, recovered from
https://github.com/chavarriajaime261/my-project onto this machine.

> Correction: the actual **JaimeClaude** (personal TypeScript AI coding agent) turned out
> to be a separate **private** repo — `chavarriajaime261/JaimeClaude` — restored alongside
> this folder at `..\JaimeClaude\`. This folder is the frontend harness + stbc-mod toolkit.

## What this project is
A Claude Code **frontend-design harness**: `AGENTS.md`/`CLAUDE.md` rules + `serve.mjs`
local server + Puppeteer screenshot scripts (`screenshot.mjs`, `screenshot-vp.mjs`),
used to build websites with a screenshot-compare loop. It also hosts the **stbc-mod/**
toolkit: Star Trek: Bridge Commander ship modding via Claude Code + Blender MCP.

## Branch map (all 5 restored locally)
| Branch | Contents | Status |
|---|---|---|
| `main` | Original harness + IPC band site | untouched |
| `restore-2026-08` | **Consolidated working branch** (see below) | current |
| `claude/ide-workflow-exploration-n28og8` | AGENTS.md refactor (fixes dead `nateh` paths) | merged into restore |
| `add-claude-github-actions-1776722575580` | `.github/workflows/` Claude CI | merged into restore |
| `claude/stbc-ship-design-tutorials-KfGkG` | `stbc-mod/` toolkit | merged into restore |
| `claude/cage-match-review-site-pcmahy` | PR #1: wrestling review site (replaces index.html) | **NOT merged — your call** (open PR #1 on GitHub) |

## Restored & verified on this machine (2026-08-06)
- Installed: git 2.55, gh 2.97, uv 0.12 (via winget)
- `npm install` done; Puppeteer 23.11.1 + Chrome 131 downloaded
- Smoke test PASSED: `node serve.mjs` + `node screenshot.mjs http://localhost:3000` → IPC site renders
- `frontend-design` skill: was never in the repo (lived on the old machine). Now provided by the
  official plugin: `frontend-design@claude-plugins-official`, installed at user scope
- `.mcp.json` created (from `stbc-mod/mcp/mcp.json.example`): registers `blender` MCP server via `uvx blender-mcp`
- `uvx blender-mcp` verified: launches fine; cannot connect to Blender until Blender runs the add-on (expected)
- `brand_assets/` recreated (was referenced by rules but never committed; contents lost)

## Still manual / pending
1. **GitHub auth**: run `gh auth login` to push branches and manage PR #1
2. **Blender toolchain** (only when resuming stbc-mod work — see `stbc-mod/docs/01` + `02`):
   Blender + BlenderMCP `addon.py` (N-panel → Start MCP Server, port 9876), NifTools addon,
   NifSkope, STBC SDK v1.1 (Model Property Editor), the game itself
3. **GitHub Actions secrets**: workflows need `CLAUDE_CODE_OAUTH_TOKEN` repo secret
   (`claude setup-token`) before `@claude` mentions / auto-review work — see `setup.md`
4. **PR #1 decision**: merge the cage-match site (replaces the band site) or close it

## Lost in the fire (not recoverable from git)
- All binary art assets (`.nif`, `.tga`, `.blend`, …) were gitignored — `stbc-mod` Phase A
  (sourcing ship models) never produced committed assets
- `temporary screenshots/` history (gitignored)
- Original `brand_assets/` contents

## Known quirks
- stbc-mod ship/hardpoint `.py` scripts target STBC''s ancient embedded Python (~1.5/2.0)
  and its `App.*` SDK — they cannot be validated with modern Python; diff against a stock
  ship on a real game install before trusting (`stbc-mod/docs/04`)
- `stbc-mod/tools/check_stats.py` IS modern Python: run with `py -3.10 stbc-mod\tools\check_stats.py`
- `screenshot-vp.mjs` lacks the `--no-sandbox` flags `screenshot.mjs` has (harmless on Windows)
- `package.json` is still named `ipc-landing` from the band-site era
