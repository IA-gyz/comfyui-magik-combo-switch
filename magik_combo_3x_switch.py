# magik_combo_3x_switch.py
from comfy.comfy_types.node_typing import IO


class MagikCombo3xSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "switch": ("BOOLEAN",),
            },
            "optional": {
                "on_true_A": (IO.ANY, {"lazy": True}),
                "on_false_A": (IO.ANY, {"lazy": True}),
                "on_true_B": (IO.ANY, {"lazy": True}),
                "on_false_B": (IO.ANY, {"lazy": True}),
                "on_true_C": (IO.ANY, {"lazy": True}),
                "on_false_C": (IO.ANY, {"lazy": True}),
            },
        }

    RETURN_TYPES = (IO.ANY, IO.ANY, IO.ANY)
    RETURN_NAMES = ("out_A", "out_B", "out_C")
    FUNCTION = "switch"
    CATEGORY = "KJNodes/misc"
    DESCRIPTION = "Three lazy switches controlled by a single boolean."

    def check_lazy_status(self, switch, on_true_A=None, on_false_A=None, on_true_B=None, on_false_B=None, on_true_C=None, on_false_C=None):
        needed = []
        if switch:
            if on_true_A is None: needed.append("on_true_A")
            if on_true_B is None: needed.append("on_true_B")
            if on_true_C is None: needed.append("on_true_C")
        else:
            if on_false_A is None: needed.append("on_false_A")
            if on_false_B is None: needed.append("on_false_B")
            if on_false_C is None: needed.append("on_false_C")
        return needed if needed else None

    def switch(self, switch, on_true_A=None, on_false_A=None, on_true_B=None, on_false_B=None, on_true_C=None, on_false_C=None):
        out_A = on_true_A if switch else on_false_A
        out_B = on_true_B if switch else on_false_B
        out_C = on_true_C if switch else on_false_C
        return (out_A, out_B, out_C)


NODE_CLASS_MAPPINGS = {
    "MagikCombo3xSwitch": MagikCombo3xSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagikCombo3xSwitch": "Magik Combo 3xSwitch",
}