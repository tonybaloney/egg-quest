import arcade
from rooms import Room


def setup_room(gamesettings):
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()
    room.wall_sprite = arcade.Sprite("graphics/trees/Flowered_Tree.png", gamesettings.sprite_scaling * 2)
    """ Set up the game and initialize the variables. """


    room.draw_top_wall(gamesettings, [])
    room.draw_bottom_wall(gamesettings, [])
    room.draw_left_wall(gamesettings, [2,3])
    room.draw_right_wall(gamesettings, [1,2])

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", gamesettings.sprite_scaling)
    wall.left = 7 * gamesettings.sprite_size
    wall.bottom = 5 * gamesettings.sprite_size
    room.wall_list.append(wall)

    # Load the background image for this level.
    room.background = arcade.load_texture("graphics/rooms/home.png")

    return room