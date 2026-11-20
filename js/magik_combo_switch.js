import { app } from "/scripts/app.js";

const NODE_NAME = "MagikComboSwitch";
const MAX_PAIRS = 8;

const inName = (branch, i) => `${branch}_${i}`;
const outName = (i) => `out_${i}`;

function syncSockets(node) {
  const pairsWidget = node.widgets?.find((w) => w.name === "pairs");
  const raw = Number(pairsWidget?.value);
  const pairs = Math.max(1, Math.min(MAX_PAIRS, Number.isFinite(raw) ? raw : 1));

  for (let i = 1; i <= MAX_PAIRS; i++) {
    for (const branch of ["on_true", "on_false"]) {
      const name = inName(branch, i);
      const idx = node.inputs.findIndex((inp) => inp.name === name);
      if (i <= pairs) {
        if (idx === -1) node.addInput(name, "*", { label: name });
      } else if (idx !== -1) {
        node.removeInput(idx);
      }
    }
  }

  for (let i = 1; i <= MAX_PAIRS; i++) {
    const name = outName(i);
    const idx = node.outputs.findIndex((o) => o.name === name);
    if (i <= pairs) {
      if (idx === -1) node.addOutput(name, "*", { label: name });
    } else if (idx !== -1) {
      node.removeOutput(idx);
    }
  }

  const size = node.computeSize();
  node.setSize([Math.max(size[0], node.size[0]), size[1]]);
  node.graph?.setDirtyCanvas?.(true, true);
}

app.registerExtension({
  name: "magik.magikComboSwitch",
  async beforeRegisterNodeDef(nodeData) {
    if (nodeData.name !== NODE_NAME) return;
    const proto = nodeData.prototype;

    const onNodeCreated = proto.onNodeCreated;
    proto.onNodeCreated = function () {
      onNodeCreated?.apply(this, arguments);
      const node = this;
      const pairsWidget = node.widgets?.find((w) => w.name === "pairs");
      if (pairsWidget) {
        const origCallback = pairsWidget.callback;
        pairsWidget.callback = function (value) {
          origCallback?.call(this, value);
          syncSockets(node);
        };
      }
      syncSockets(node);
    };

    const onConfigure = proto.onConfigure;
    proto.onConfigure = function () {
      onConfigure?.apply(this, arguments);
      syncSockets(this);
    };
  },
});
