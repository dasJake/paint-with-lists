import os
import sys
import arcade

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "src")
sys.path.append(mymodule_dir)

import config




class PlanningView(arcade.Window):
    def __init__(self):
        super().__init__(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SCREEN_TITLE)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # One dimensional list of all sprites in the two-dimensional sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        # Create a list of solid-color sprites to represent each grid location
        for row in range(config.ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(config.COLUMN_COUNT):
                x = column * (config.WIDTH + config.MARGIN) + (config.WIDTH / 2 + config.MARGIN)
                y = row * (config.HEIGHT + config.MARGIN) + (config.HEIGHT / 2 + config.MARGIN)
                sprite = arcade.SpriteSolidColor(config.WIDTH, config.HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

        self.shapelist = arcade.shape_list.ShapeElementList()
        self.shapelist.append(arcade.shape_list.create_lines([(1, 2), (40, 50), (100, 200), (300, 350)], arcade.color.AMARANTH_PINK))

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

        #self.grid_sprite_list.draw()
        self.shapelist.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        row = int(y // (config.HEIGHT + config.MARGIN))
        column = int(x // (config.WIDTH + config.MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if self.grid_sprites[row][column].color == arcade.color.WHITE:
            self.grid_sprites[row][column].color = arcade.color.ALABAMA_CRIMSON

        else:
            self.grid_sprites[row][column].color = arcade.color.AIR_FORCE_BLUE

def main():
    window = PlanningView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
