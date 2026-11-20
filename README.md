# ComfyUI Magik Combo Switch

A ComfyUI custom node pack with a single dynamic switch node.

## Nodes

**Magik Combo Switch** (`MagikComboSwitch`, category `Magik/switch`)

One boolean `switch` controls any number of parallel switches:

- `pairs` (INT, 1-8, default 2) sets how many input/output pairs are shown. The frontend adds/removes the `on_true_i` / `on_false_i` inputs and `out_i` outputs dynamically when this widget changes.
- For each pair `i`, `out_i` returns `on_true_i` when `switch` is true, otherwise `on_false_i`.
- All pair inputs are `*` (any type) and **lazy**: only the branch selected by `switch` is evaluated, so the unselected branch never runs.

This replaces the previous fixed `MagikCombo2xSwitch` / `MagikCombo3xSwitch` / `MagikCombo4xSwitch` nodes with one node whose input/output count is configurable.

## Install

Clone into `ComfyUI/custom_nodes/` and restart ComfyUI:

```bash
git clone https://github.com/IA-gyz/comfyui-magik-combo-switch.git
```

or install via ComfyUI-Manager / the Comfy Registry (publisher `IA-gyz`, pack `comfyui-magik-combo-switch`).

## Compatibility

- Dynamic socket counts are implemented by a small frontend extension (`js/magik_combo_switch.js`), which requires a ComfyUI frontend that supports custom node extensions (any current release).
- The backend imports `comfy.comfy_types.node_typing.IO` when available and falls back to the plain `"*"` wildcard type on older ComfyUI versions, so the node itself also loads on older backends.

## License

MIT
