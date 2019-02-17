import arcade
from Player import *
import os
import random
import timeit

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
        self.Player1 = None

        #Coin and counter
        self.player_list = None
        self.coin_list = None
        self.coun_counter = 0

        self.processing_time = 0
        self.draw_time = 0
        #set fps
        #self.set_update_rate(1 / 80)

    def setup(self):
        # Set up Player1
        self.Player1 = Player("Images/Kall.png", 0.2)
        self.Player1.PlayerSetup()
        self.Player1.center_x, self.Player1.center_y = 50, 50


        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_list.append(self.Player1)
        self.player_list.append(self.Player1.SwordSprite)

        # Create the coins
        for i in range(15):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Images/gem.png", 0.07)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)


    def on_draw(self):
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 20, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.BLACK, 16)

        output = f"Coins hit: {self.coun_counter:3}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.BLACK, 16)
        try:
            fps = 1 / (self.draw_time + self.processing_time)
            output = f"Max FPS: {fps:3.1f}"
            arcade.draw_text(output, 20, SCREEN_HEIGHT - 80, arcade.color.BLACK, 16)
        except:
            pass
        self.draw_time = timeit.default_timer() - draw_start_time



    def update(self, delta_time):
        start_time = timeit.default_timer()

        self.Player1.update()

        self.coin_list.update()

        if self.Player1.sword_gate == 1:
            self.Player1.SwordSwing()

        self.Player1.update_animation(5)


        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.Player1, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.kill()
            self.coun_counter += 1

        # Save the time it took to do this.
        self.processing_time = timeit.default_timer() - start_time


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key"""
        if key == arcade.key.LEFT:
            self.Player1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.Player1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.Player1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.Player1.change_y = -MOVEMENT_SPEED
        if key == arcade.key.SPACE:
            self.Player1.sword_gate = 1

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Player1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Player1.change_y = 0
        if key == arcade.key.SPACE:
            self.Player1.sword_gate = 0
