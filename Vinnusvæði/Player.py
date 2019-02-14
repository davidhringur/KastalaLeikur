

"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Player:

    Hp = 100
    Gender = 0
    Clothes = [1,2,3,4,5]
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the Players with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the Player
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the Player hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our Player
        self.Player = Player(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.Player.draw()

    def update(self, delta_time):
        self.Player.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.Player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.Player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.Player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.Player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Player.change_y = 0


def main():
    window = MyGame(1200, 600, "Highburn Fortress")
    arcade.run()


if __name__ == "__main__":
    main()
