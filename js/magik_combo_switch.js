import { app } from "/scripts/app.js";

const NODE_NAME = "MagikComboSwitch";
const MAX_PAIRS = 8;

const inName = (branch, i) => `${branch}_${i}`;
const outName = (i) => `out_${i}`;

function isTarget(node) {
  return node?.comfyClass === NODE_NAME || node?.type === NODE_NAME || node?.ComfyClass === NODE_NAME;
}

function getPairs(node) {
  const w = node.widgets?.find((w) => w.name === "pairs");
  const v = Number(w?.value);
  return Math.max(1, Math.min(MAX_PAIRS, Number.isFinite(v) ? Math.trunc(v) : 2));
}

function syncSockets(node) {
  const pairs = getPairs(node);

  for (let i = 1; i <= MAX_PAIRS; i++) {
    for (const branch of ["on_true", "on_false"]) {
      const name = inName(branch, i);
      const idx = node.inputs?.findIndex((inp) => inp.name === name) ?? -1;
      if (i <= pairs) {
        if (idx === -1) node.addInput(name, "*", { label: name });
      } else if (idx !== -1) {
        node.removeInput(idx);
      }
    }
  }

  for (let i = 1; i <= MAX_PAIRS; i++) {
    const name = outName(i);
    const idx = node.outputs?.findIndex((o) => o.name === name) ?? -1;
    if (i <= pairs) {
      if (idx === -1) node.addOutput(name, "*", { label: name });
    } else if (idx !== -1) {
      node.removeOutput(idx);
    }
  }

  if (typeof node.computeSize === "function" && typeof node.setSize === "function") {
    const size = node.computeSize();
    node.setSize([Math.max(size[0], node.size?.[0] ?? size[0]), size[1]]);
  }
  node.graph?.setDirtyCanvas?.(true, true);
}

function hookPairsWidget(node) {
  const w = node.widgets?.find((w) => w.name === "pairs");
  if (!w || w.__magikPairsHooked) return;
  w.__magikPairsHooked = true;
  const orig = w.callback;
  w.callback = function (value) {
    orig?.apply(this, arguments);
    syncSockets(node);
  };
}

function hookAndSync(node) {
  hookPairsWidget(node);
  syncSockets(node);
}

app.registerExtension({
  name: "magik.magikComboSwitch",

  async beforeRegisterNodeDef(nodeType, nodeData) {
    const matches =
      nodeType?.ComfyClass === NODE_NAME || nodeData?.name === NODE_NAME || nodeType?.name === NODE_NAME;
    if (!matches) return;
    const proto = (typeof nodeType === "function" ? nodeType : nodeData)?.prototype;
    if (!proto) return;
    const onNodeCreated = proto.onNodeCreated;
    proto.onNodeCreated = function () {
      onNodeCreated?.apply(this, arguments);
      const node = this;
      queueMicrotask(() => hookAndSync(node));
    };
  },

  async nodeCreated(node) {
    if (!isTarget(node)) return;
    const n = node;
    queueMicrotask(() => hookAndSync(n));
  },

  loadedGraphNode(node) {
    if (!isTarget(node)) return;
    hookAndSync(node);
  },

  async afterConfigureGraph() {
    const nodes = app.graph?._nodes ?? app.graph?.nodes ?? [];
    for (const node of nodes) {
      if (isTarget(node)) hookAndSync(node);
    }
  },
});
