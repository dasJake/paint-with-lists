import arcade

import config


class ListenSprite(arcade.SpriteSolidColor):

    def __init__(self, x, y):
        super().__init__(
            config.GRID_SIZE * 5,
            config.GRID_SIZE * 5,
        )

        self.width = config.GRID_SIZE * 5
        self.height = config.GRID_SIZE * 5
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.CHERRY_BLOSSOM_PINK


