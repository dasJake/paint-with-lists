import os
import sys
import arcade
import numpy
import math
from typing import List, Tuple

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "src")
sys.path.append(mymodule_dir)

import config
from listensprite import ListenSprite


class PlanningView(arcade.Window):
    def __init__(self):
        super().__init__(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SCREEN_TITLE)

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.karo_sprites = arcade.SpriteList()

        self.karo_koordinaten = numpy.empty(
            (config.SCREEN_WIDTH // config.GRID_SIZE,
                config.SCREEN_HEIGHT // config.GRID_SIZE),
            arcade.BasicSprite)

        self.gitternetz = arcade.shape_list.ShapeElementList()
        self.gridline_points = self.create_gridlines_points()
        self.gitternetz.append(arcade.shape_list.create_lines(self.gridline_points, arcade.color.AMARANTH_PINK))

        self.highlight_karo_x = 10
        self.highlight_karo_y = 10
        self.highlight_sichtbar = False

        self.listenfensters = arcade.SpriteList()

        self.c_gedrueckt = False

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
        self.gitternetz.draw()
        if self.highlight_sichtbar:
            arcade.draw_lbwh_rectangle_outline(
                self.highlight_karo_x,
                self.highlight_karo_y,
                config.GRID_SIZE, config.GRID_SIZE,
                arcade.color.AUREOLIN)

        self.listenfensters.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // config.GRID_SIZE)
        row = int(y // config.GRID_SIZE)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row})")
        print(f"highligh: {self.highlight_karo_x} | {self.highlight_karo_y}")

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

            print(f"spritelist:\n{len(self.karo_sprites)}")

            if self.c_gedrueckt:
                listenfenster = ListenSprite(x, y)
                self.listenfensters.append(listenfenster)

                print(f"listenfenster:\n{len(self.listenfensters)}")

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        prev_x, prev_y = x - dx, y - dy

        # Number of interpolation steps (adjust factor to tweak sampling rate)
        steps = max(abs(dx), abs(dy)) // (config.GRID_SIZE // 2)  # Sample every half-grid step
        steps = max(1, math.ceil(steps))  # Avoid zero division

        for i in range(steps + 1):
            # Linearly interpolate between previous and current position
            sample_x = prev_x + (x - prev_x) * (i / steps)
            sample_y = prev_y + (y - prev_y) * (i / steps)

            column = int(sample_x // config.GRID_SIZE)
            row = int(sample_y // config.GRID_SIZE)

            if not self.karo_koordinaten[column][row]:  # Avoid duplicates
                karo = arcade.SpriteSolidColor(
                    config.GRID_SIZE,
                    config.GRID_SIZE,
                    self.karomitte_berechnen(column),
                    self.karomitte_berechnen(row),
                    arcade.color.WHITE
                )
                self.karo_sprites.append(karo)
                self.karo_koordinaten[column][row] = karo

                print(f"spritelist:\n{len(self.karo_sprites)}")

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        column = int(x // config.GRID_SIZE)
        row = int(y // config.GRID_SIZE)
        self.highlight_karo_x = column * config.GRID_SIZE
        self.highlight_karo_y = row * config.GRID_SIZE
        self.highlight_sichtbar = True

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.C:
            self.c_gedrueckt = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.C:
            self.c_gedrueckt = False

    def karomitte_berechnen(self, i):
        return i * config.GRID_SIZE + config.GRID_SIZE / 2


def main():
    window = PlanningView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
