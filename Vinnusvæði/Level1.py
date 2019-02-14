import arcade
from Player import *
import os
import random

class Level_1(arcade.Window):

    def __init__(self, width, height, title):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our Player1
        self.Player1 = Player1(50, 50, 0, 0, 15, arcade.color.AUBURN)

        #Coin and counter
        self.coin_list = None
        self.coun_counter = 0

    def setup(self):
        self.coin_list = arcade.SpriteList()

        # Create the coins
        for i in range(100):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Images/gem.png", 0.07)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.coin_list.draw()
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
