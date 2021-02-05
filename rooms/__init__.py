import arcade
from arcade.sprite import Sprite


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    background: Sprite
    wall_sprite: Sprite

    def __init__(self, gamesettings):
        self.gamesettings = gamesettings

        self.wall_list = arcade.SpriteList()

    def draw_top_wall(self, gaps: list = None) -> None:
        y = 0
        for x in range(
            0, self.gamesettings.SCREEN_WIDTH, self.gamesettings.SPRITE_SIZE
        ):
            if x * self.gamesettings.SPRITE_SIZE not in gaps:
                wall = self.wall_sprite
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_left_wall(self, gaps: list = None) -> None:
        x = 0  # left wall
        for y in range(
            self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SPRITE_SIZE,
        ):
            if y * self.gamesettings.SPRITE_SIZE not in gaps:
                wall = self.wall_sprite
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_right_wall(self, gaps: list = None) -> None:
        x = 0  # left wall
        for y in range(
            self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SPRITE_SIZE,
        ):
            if y * self.gamesettings.SPRITE_SIZE not in gaps:
                wall = self.wall_sprite
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_bottom_wall(self, gaps: list = None) -> None:
        x = self.gamesettings.SCREEN_WIDTH - self.gamesettings.SPRITE_SIZE
        for y in range(
            self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE,
            self.gamesettings.SPRITE_SIZE,
        ):
            if (
                y != self.gamesettings.SPRITE_SIZE * 1
                and y != self.gamesettings.SPRITE_SIZE * 2
            ):
                wall = self.wall_sprite
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)
