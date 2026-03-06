import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
layers_ext = Layers()
tapdance = TapDance()

keyboard.modules.append(layers_ext)
keyboard.modules.append(tapdance)

keyboard.col_pins = (board.GP0, board.GP7, board.GP6, board.GP29)
keyboard.row_pins = (board.GP1, board.GP2, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Double-tap to toggle between layer 0 and layer 1
TD_LAYER = tapdance.register(
    KC.ENT,           # single tap = Enter (layer 0) or F12 (layer 1)
    KC.TG(1),         # double tap = toggle layer
)

keyboard.keymap = [
    # Layer 0 - Numpad
    [
        KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_0,
        KC.KP_4, KC.KP_5, KC.KP_6, KC.BSPC,
        KC.KP_1, KC.KP_2, KC.KP_3, TD_LAYER,
    ],
    # Layer 1 - Function keys
    [
        KC.F1,  KC.F2,  KC.F3,  KC.F4,
        KC.F5,  KC.F6,  KC.F7,  KC.F8,
        KC.F9,  KC.F10, KC.F11, TD_LAYER,
    ],
]

if __name__ == '__main__':
    keyboard.go()