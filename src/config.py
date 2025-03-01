import os
import sys

import version

_IS_BUNDLED = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")
_RESOURCE_PATH = os.path.join(
    os.path.dirname(__file__), "." if _IS_BUNDLED else "..", "resources"
)

DEBUG = not _IS_BUNDLED

# Set how many rows and columns the grid will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid square
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = f"Planning Garden (v{version.VERSION})"
