import arcade


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self, gamesettings):
        self.gamesettings = gamesettings

        self.wall_list = arcade.SpriteList()

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None

        self.wall_sprite = None

    def draw_top_wall(self, gaps=None):
        y = 0
        for x in range(0, self.gamesettings.SCREEN_WIDTH, self.gamesettings.SPRITE_SIZE):
            if (x * self.gamesettings.SPRITE_SIZE not in gaps):
                wall = arcade.Sprite("graphics/trees/Flowered_Tree.png", self.gamesettings.SPRITE_SCALING * 2)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_left_wall(self, gaps=None):
        x = 0  # left wall
        for y in range(self.gamesettings.SPRITE_SIZE, self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE, self.gamesettings.SPRITE_SIZE):
            if (y * self.gamesettings.SPRITE_SIZE not in gaps):
                wall = arcade.Sprite("graphics/trees/Flowered_Tree.png", self.gamesettings.SPRITE_SCALING * 2)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_right_wall(self, gaps):
        x = 0  # left wall
        for y in range(self.gamesettings.SPRITE_SIZE, self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE, self.gamesettings.SPRITE_SIZE):
            if (y * self.gamesettings.SPRITE_SIZE not in gaps):
                wall = arcade.Sprite("graphics/trees/Flowered_Tree.png", self.gamesettings.SPRITE_SCALING * 2)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)

    def draw_bottom_wall(self, gaps):
        x = self.gamesettings.SCREEN_WIDTH - self.gamesettings.SPRITE_SIZE
        for y in range(self.gamesettings.SPRITE_SIZE, self.gamesettings.SCREEN_HEIGHT - self.gamesettings.SPRITE_SIZE, self.gamesettings.SPRITE_SIZE):
            if (y != self.gamesettings.SPRITE_SIZE * 1 and y != self.gamesettings.SPRITE_SIZE * 2):
                wall = arcade.Sprite("graphics/trees/Flowered_Tree.png", self.gamesettings.SPRITE_SCALING * 2)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)
