try:
    from comfy.comfy_types.node_typing import IO
except ImportError:
    class IO:
        ANY = "*"


MAX_PAIRS = 8


class MagikComboSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        optional = {}
        for i in range(1, MAX_PAIRS + 1):
            optional[f"on_true_{i}"] = (IO.ANY, {"lazy": True, "tooltip": f"Value for out_{i} when switch is true"})
            optional[f"on_false_{i}"] = (IO.ANY, {"lazy": True, "tooltip": f"Value for out_{i} when switch is false"})
        return {
            "required": {
                "switch": ("BOOLEAN", {"default": False, "label_on": "true", "label_off": "false"}),
                "pairs": ("INT", {"default": 2, "min": 1, "max": MAX_PAIRS, "step": 1, "tooltip": "Number of input/output pairs shown"}),
            },
            "optional": optional,
        }

    RETURN_TYPES = (IO.ANY,) * MAX_PAIRS
    RETURN_NAMES = tuple(f"out_{i}" for i in range(1, MAX_PAIRS + 1))
    FUNCTION = "switch"
    CATEGORY = "Magik/switch"
    DESCRIPTION = "Single dynamic lazy switch. The 'pairs' widget controls how many on_true/on_false input pairs and out_i outputs are shown (1-8). Each output selects its true/false input based on 'switch'; only the selected branch is evaluated."

    def check_lazy_status(self, switch, pairs, **kwargs):
        needed = []
        for i in range(1, min(int(pairs), MAX_PAIRS) + 1):
            name = f"on_true_{i}" if switch else f"on_false_{i}"
            if kwargs.get(name) is None:
                needed.append(name)
        return needed

    def switch(self, switch, pairs, **kwargs):
        pairs = max(1, min(int(pairs), MAX_PAIRS))
        out = []
        for i in range(1, MAX_PAIRS + 1):
            if i <= pairs:
                out.append(kwargs.get(f"on_true_{i}" if switch else f"on_false_{i}"))
            else:
                out.append(None)
        return tuple(out)


NODE_CLASS_MAPPINGS = {
    "MagikComboSwitch": MagikComboSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagikComboSwitch": "Magik Combo Switch",
}
