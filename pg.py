import os
import sys
import arcade
import numpy
from typing import List, Tuple

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "src")
sys.path.append(mymodule_dir)

import config


class PlanningView(arcade.Window):
    def __init__(self):
        super().__init__(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SCREEN_TITLE)

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.karo_sprites = arcade.SpriteList()

        self.karo_koordinaten = numpy.empty(
            (config.SCREEN_WIDTH // config.GRID_SIZE,
                config.SCREEN_HEIGHT // config.GRID_SIZE),
            arcade.BasicSprite)

        self.shapelist = arcade.shape_list.ShapeElementList()
        self.gridline_points = self.create_gridlines_points()
        self.shapelist.append(arcade.shape_list.create_lines(self.gridline_points, arcade.color.AMARANTH_PINK))

    def create_gridlines_points(self) -> List[Tuple[int | float, int | float]]:
        gridline_points: List[Tuple[int | float, int | float]] = []

        # Generate vertical grid lines
        for i in range(0, config.SCREEN_WIDTH + 1, config.GRID_SIZE):
            gridline_points.append((i, 0))  # Start point of vertical line
            gridline_points.append((i, config.SCREEN_HEIGHT))  # End point of vertical line

        # Generate horizontal grid lines
        for j in range(0, config.SCREEN_HEIGHT + 1, config.GRID_SIZE):
            gridline_points.append((0, j))  # Start point of horizontal line
            gridline_points.append((config.SCREEN_WIDTH, j))  # End point of horizontal line

        return gridline_points

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        self.karo_sprites.draw()
        self.shapelist.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // config.GRID_SIZE)
        row = int(y // config.GRID_SIZE)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row})")
        print(f"koordinateninhalt: {self.karo_koordinaten[column][row]}")

        karo_unter_maus = self.karo_koordinaten[column][row]
        if karo_unter_maus:
            karo_unter_maus.kill()
            self.karo_koordinaten[column][row] = None

        else:
            karo = arcade.SpriteSolidColor(
                config.GRID_SIZE,
                config.GRID_SIZE,
                self.karomitte_berechnen(column),
                self.karomitte_berechnen(row),
                arcade.color.WHITE)
            self.karo_sprites.append(karo)
            self.karo_koordinaten[column][row] = karo

    def karomitte_berechnen(self, i):
        return i * config.GRID_SIZE + config.GRID_SIZE / 2


def main():
    window = PlanningView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
