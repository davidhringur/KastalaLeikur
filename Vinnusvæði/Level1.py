import arcade
from Player import *

class Level_1(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our Player1
        self.Player1 = Player1(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.Player1.draw()

    def update(self, delta_time):
        self.Player1.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.Player1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.Player1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.Player1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.Player1.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Player1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Player1.change_y = 0
