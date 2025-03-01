import os
import sys

import version

_IS_BUNDLED = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")
_RESOURCE_PATH = os.path.join(
    os.path.dirname(__file__), "." if _IS_BUNDLED else "..", "resources"
)

DEBUG = not _IS_BUNDLED

SCREEN_WIDTH = 810
SCREEN_HEIGHT = 600
SCREEN_TITLE = f"Planning Garden (v{version.VERSION})"

GRID_SIZE = 30
