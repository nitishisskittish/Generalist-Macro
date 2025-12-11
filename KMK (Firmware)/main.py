# To-Do List:
# Make it so that holding down the encoder and turning adjusts RGB Brightness.
# Make it so that holding down rightmost key and turning encoder adjusts RGB Color.
# Make it so that OLED Displays Brightness level when being adjusted 

import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.extensions.rgb import RGB, RGBModes
from kmk.extensions.display.volume import VolumeDisplay
from kmk.extensions.display import Display
from kmk.modules.encoder import Encoder
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

# RGB LEDs:
rgb = RGB(
    pixel_pin=board.D7,
    num_pixels=16,
    hue=0,
    sat=0, 
    val=255, 
    mode=RGBModes.STATIC_COLOR,
    val_default=72
)
keyboard.extensions.append(rgb)

# OLED Volume Display
display_ext = Display(
    i2c_port=board.I2C(),
    display=VolumeDisplay(),
)
keyboard.extensions.append(display_ext)

# Layers (Right now I only have one, but I may add more later)
keyboard.modules.append(Layers())

# Rotary Encoder
keyboard.modules.append(Encoder(
    pins=((board.D9, board.D10, None),),
    tap_max=1000, 
    on_clockwise=KC.VOLU, 
    on_ccwise=KC.VOLD, 
))


# Key Matrix
keyboard.row_pins = (board.D6, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Keymap
KEYMAP = [
    [
        KC.MPRV, KC.W,    KC.MNXT, KC.MUTE,
        KC.A,    KC.S,    KC.D,    KC.LGUI(KC.S) # Custom shortcut key for opening spotify on my system
    ]
]
keyboard.keymaps = KEYMAP

if __name__ == '__main__':
    keyboard.go()