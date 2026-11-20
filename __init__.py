from .magik_combo_switch import MagikComboSwitch

NODE_CLASS_MAPPINGS = {
    "MagikComboSwitch": MagikComboSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagikComboSwitch": "Magik Combo Switch",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
