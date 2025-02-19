import arcade

width = 860
height = 480
title = "planninggarden"


class PlanningView(arcade.Window):
    def __init__(self):
        super().__init__(width, height, title)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    def setup(self):
        pass

    def on_draw(self):
        self.clear()


def main():
    window = PlanningView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
