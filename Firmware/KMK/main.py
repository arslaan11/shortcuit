import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmo.extension.media_keys import mediakeys
from kmk.extensions.encoder import EncoderHandler
from kmk.modules.layers import layers
from kb import Shortcuit
from kmk.keys import KC

# 1. Initialize Keybord 
keyboard = Shortcuit()
keyboard.modules.append(Layers())
keyboard.extension.append(MediaKeys())

# 2. add Modules (Media Keys for Volume, Layers for Multi-funcion)
keyboard.col_pins = (board.GP2, board.GP3, board.GP4)
keyboard.row_pins =  (board.GP5, board.GP6, board.GP7)
KEYBOARD.diode_orientation = DiodeOrientation.COL2ROW

# 3. Encoder Configuration (EC11)
encoder_Handler = EncoderHandler()
keyboard.modules.append(encoder_Handler)
encoder_Handler.pin = (
    (board.GP10, board.GP11, board.GP12, False)
)

# 4. Macro for apps/games
# Type Win+R -> URL/PATH -> Enter
OPEN_CANVA = KC.MACRO(KC.LGUI(KC.R), KC.MWET(500), "https://www.canva.com/", KC.ENTER)
# REPLACE THE PATH BELOW WITH YOUR FAVORITE GAME .EXE PATH OR WEBSITE URL OR WHATEVER YOU WANT TO OPEN WITH A MACRO(I WILL SET THOS TO STEAM)
OPEN_STEAM = KC.MACRO(KC.LGUI(KC.R), KC.MWET(500), "https://store.steampowered.com", KC.ENTER)
#add more same COMANDS AS ABOVE FOR OTHER GAMES/APPS/WEBSITES 

# 5. KEYMAP
# Layer 0: Standard keys
# Layer 1: app/game launcher(hold encoder button to access)
keyboard.keymap = [
    [
        KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.Z),  #ROW 1 copy,paste,undo
        KC.LWIN(KC.D), KC.UP, KC.ENTER,                  #ROW 2 Destop, up, enter
        KC.LEFT, KC.DOWN, KC.RIGHT,                      #ROW 3 left, down, right
    ],
    [
        OPEN_CANVA, OPEN_STEAM, KC.NO,                   # ROW 1 CANVA, STEAM, NO KEY
        KC.NO, KC.NO, KC.NO,                             # ROW 2 NO KEY
        KC.NO, KC.NO, KC.NO,                             # ROW 3 NO KEY
    ]
]

# 6. ENcoder mapping (volume control)
encoder_Handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),) #LAYER 0: VOL UP, VOL DOWN, MUTE
]

if __name__ == '__main__':
    keyboard.go()