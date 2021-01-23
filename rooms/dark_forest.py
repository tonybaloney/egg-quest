import arcade
from rooms import Room

def setup_room(screen_height, screen_width, sprite_scaling, sprite_size):
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, screen_height - sprite_size):
        # Loop for each box going across
        for x in range(0, screen_width, sprite_size):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", sprite_scaling)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, screen_width - sprite_size):
        # Loop for each box going across
        for y in range(sprite_size, screen_height - sprite_size, sprite_size):
            # Skip making a block 4 and 5 blocks up
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", sprite_scaling)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", sprite_scaling)
    wall.left = 5 * sprite_size
    wall.bottom = 6 * sprite_size
    room.wall_list.append(wall)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")

    return room
