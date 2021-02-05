"""
Sprite move between different rooms.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""

import arcade
import os
from dataclasses import dataclass

import player
import rooms.home
import rooms.dark_forest


@dataclass
class GameSettings:
    SPRITE_SCALING = 0.5
    SPRITE_NATIVE_SIZE = 128
    SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

    SCREEN_WIDTH = SPRITE_SIZE * 14
    SCREEN_HEIGHT = SPRITE_SIZE * 10
    SCREEN_TITLE = "Sprite Rooms Example"

    MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    settings: GameSettings

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.settings = GameSettings()

        # Set up the player
        self.player_sprite = player.MainPlayerSprite(self.settings.SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        self.rooms.append(rooms.home.setup_room(self.settings))
        self.rooms.append(rooms.dark_forest.setup_room(self.settings))

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.rooms[self.current_room].wall_list
        )

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(
            0,
            0,
            self.settings.SCREEN_WIDTH,
            self.settings.SCREEN_HEIGHT,
            self.rooms[self.current_room].background,
        )

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = self.settings.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -self.settings.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.settings.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.settings.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if (
            self.player_sprite.center_x > self.settings.SCREEN_WIDTH
            and self.current_room == 0
        ):
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(
                self.player_sprite, self.rooms[self.current_room].wall_list
            )
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(
                self.player_sprite, self.rooms[self.current_room].wall_list
            )
            self.player_sprite.center_x = self.settings.SCREEN_WIDTH


def main():
    """ Main method """
    window = MyGame(
        GameSettings.SCREEN_WIDTH, GameSettings.SCREEN_HEIGHT, GameSettings.SCREEN_TITLE
    )
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()