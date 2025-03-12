import os
import sys

import version

_IS_BUNDLED = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")
_RESOURCE_PATH = os.path.join(
    os.path.dirname(__file__), "." if _IS_BUNDLED else "..", "resources"
)

DEBUG = not _IS_BUNDLED

GRID_SIZE = 15

SCREEN_WIDTH = 70 * GRID_SIZE
SCREEN_HEIGHT = 40 * GRID_SIZE
SCREEN_TITLE = f"Planning Garden (v{version.VERSION})"