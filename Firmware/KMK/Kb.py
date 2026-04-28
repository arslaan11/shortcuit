import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

class Shortcuit(KMKKeyboard):
    def __init__(self):
        # MATRIX PINS
        # Matches your KiCad trace layout
        self.row_pins = (board.GP2, board.GP3, board.GP4)
        self.col_pins = (board.GP5, board.GP6, board.GP7)

        #diode direction
        self. diode_orientation = DiodeOrientation.COL2ROW