from .magik_combo_2x_switch import MagikCombo2xSwitch
from .magik_combo_3x_switch import MagikCombo3xSwitch
from .magik_combo_4x_switch import MagikCombo4xSwitch

NODE_CLASS_MAPPINGS = {
    "MagikCombo2xSwitch": MagikCombo2xSwitch,
    "MagikCombo3xSwitch": MagikCombo3xSwitch,
    "MagikCombo4xSwitch": MagikCombo4xSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagikCombo2xSwitch": "Magik Combo 2xSwitch",
    "MagikCombo3xSwitch": "Magik Combo 3xSwitch",
    "MagikCombo4xSwitch": "Magik Combo 4xSwitch",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']