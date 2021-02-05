import arcade
from rooms import Room


def setup_room(gamesettings):
    room = Room(gamesettings)
    room.wall_sprite = arcade.Sprite(
        "graphics/trees/Flowered_Tree.png", gamesettings.SPRITE_SCALING * 2
    )
    """ Set up the game and initialize the variables. """

    room.draw_top_wall([])
    room.draw_bottom_wall([])
    room.draw_left_wall([2, 3])
    room.draw_right_wall([1, 2])

    wall = arcade.Sprite(
        ":resources:images/tiles/boxCrate_double.png", gamesettings.SPRITE_SCALING
    )
    wall.left = 7 * gamesettings.SPRITE_SIZE
    wall.bottom = 5 * gamesettings.SPRITE_SIZE
    room.wall_list.append(wall)

    # Load the background image for this level.
    room.background = arcade.load_texture("graphics/rooms/home.png")
    return room
