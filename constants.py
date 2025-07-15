# constants.py

from kivy.metrics import sp
from kivy.core.window import Window

# Global font scaling factor (tweak this to adjust all fonts easily)
FONT_SCALE = 1.0

# Responsive spacing & padding
PADDING_HORIZONTAL = Window.width * 0.05
PADDING_VERTICAL = Window.height * 0.1
SPACING_VERTICAL = Window.height * 0.03

# Button dimensions
BUTTON_HEIGHT_RATIO = 0.12
BUTTON_FONT_RATIO = 0.25  # Relative to button base size
