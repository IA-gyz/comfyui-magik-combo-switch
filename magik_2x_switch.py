# magik_2x_switch.py
from comfy.comfy_types.node_typing import IO


class Magik2xSwitch:
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
            },
        }

    RETURN_TYPES = (IO.ANY, IO.ANY)
    RETURN_NAMES = ("out_A", "out_B")
    FUNCTION = "switch"
    CATEGORY = "KJNodes/misc"
    DESCRIPTION = "Two lazy switches controlled by a single boolean. out_A and out_B each select their true/false input based on the switch value."

    def check_lazy_status(self, switch, on_true_A=None, on_false_A=None, on_true_B=None, on_false_B=None):
        needed = []
        if switch:
            if on_true_A is None:
                needed.append("on_true_A")
            if on_true_B is None:
                needed.append("on_true_B")
        else:
            if on_false_A is None:
                needed.append("on_false_A")
            if on_false_B is None:
                needed.append("on_false_B")
        return needed if needed else None

    def switch(self, switch, on_true_A=None, on_false_A=None, on_true_B=None, on_false_B=None):
        out_A = on_true_A if switch else on_false_A
        out_B = on_true_B if switch else on_false_B
        return (out_A, out_B)


NODE_CLASS_MAPPINGS = {
    "Magik2xSwitch": Magik2xSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Magik2xSwitch": "Magik 2xSwitch",
}