# 02 — Blender MCP + Claude Code Setup (your PC)

This lets **Claude Code (in VS Code) drive Blender** through natural language: import a
model, scale/rotate it, clean up geometry, and trigger the NifTools export — all via
Blender's Python (`bpy`) API over a local socket.

## How it works (architecture)
```
Claude Code (VS Code)  ──MCP──>  blender-mcp server  ──socket──>  Blender add-on (running)
                                                                   executes bpy commands
```
- The **blender-mcp server** is a local process (run via `uvx blender-mcp`).
- A small **Blender add-on** listens inside a running Blender session.
- Claude sends intents → server → add-on → `bpy` calls execute live in Blender.

Repo: https://github.com/ahujasid/blender-mcp

## Install steps

### 1. Install `uv` (Python runner)
Blender MCP is distributed to run via `uvx`. Install `uv`:
- Windows (PowerShell):
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### 2. Install the Blender add-on side
- Download `addon.py` from the blender-mcp repo.
- Blender: *Edit → Preferences → Add-ons → Install…* → select `addon.py` → enable
  **"Interface: Blender MCP"**.
- In Blender's 3D view, open the **N-panel** → **BlenderMCP** tab → **Start MCP Server**
  (default port 9876). Leave Blender open while you work.

### 3. Register the MCP server with Claude Code
Add the server to your Claude Code MCP config. A ready-to-merge block is in
[`../mcp/mcp.json.example`](../mcp/mcp.json.example). The entry is:

```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

Easiest path with the CLI:
```bash
claude mcp add blender -- uvx blender-mcp
```
(or paste the block into your project `.mcp.json` / user settings — see the example file).

### 4. Verify the link
1. Blender open, MCP server **Started** (N-panel).
2. In Claude Code, run `/mcp` (or check the MCP status) — `blender` should be **connected**.
3. Ask Claude: *"In Blender, add a cube named TEST."* A cube should appear in your scene.

## Working tips
- **Keep Blender open** with the server running for the whole session; if the socket drops,
  re-click *Start MCP Server*.
- Blender MCP is great for **import, transform, cleanup, and export operators** — i.e. the
  exact mechanical steps in our pipeline. It's weaker at fine artistic modeling, which is
  fine because we **import existing models** rather than sculpt from scratch.
- You can combine MCP-driven steps with manual Blender work freely.

## What Claude will actually do via MCP (preview of the pipeline)
- `import_scene` the sourced model (obj/fbx/gltf/etc.)
- Recenter to origin, set correct scale (BC units) and orientation (BC's forward/up axes)
- Merge/weld the mesh, apply transforms, strip unused data
- Trigger **NifTools export** to `<name>.nif`

Full step list → `03-pipeline.md`.
