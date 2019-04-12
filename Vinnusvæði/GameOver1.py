import arcade
import Player
import Room
import os
from Levels import Levels
from MainMenu import *
import pyglet

class GameOver(arcade.Window):

    def __init__(self, width, height, title=""):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #Notum smið yfirklasanns
        super().__init__(width, height, title)

        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        #Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        self.set_mouse_visible(False)

        self.options = [[1, 0]]
        self.current_option_x = 1
        self.current_option_y = 0


        SPRITE_SCALING = 0.3

        #Play Again
        self.PA = arcade.Sprite("Images/GameOver/PlayAgain.png", center_x=self.SCREEN_WIDTH // 5, center_y=self.SCREEN_HEIGHT // 5,
                              scale=SPRITE_SCALING)
        #Exit Game
        self.EG = arcade.Sprite("Images/GameOver/ExitGame.png", center_x=self.SCREEN_WIDTH // 1.25, center_y=self.SCREEN_HEIGHT // 5,
                              scale=SPRITE_SCALING)



        self.player = pyglet.media.Player()
        self.FantasySound = pyglet.media.load("Music/Tales_of_Phantasia.wav",  streaming=False)

        self.player.queue(self.FantasySound)


        self.player.play()


    i = 0
    def on_draw(self):
    # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                 self.SCREEN_WIDTH, self.SCREEN_HEIGHT, arcade.load_texture("Images\ModelPack\MakingMap1.png"))

        #Leikmaður 1
        if self.options == [[1, 0]]:
            self.i += 1
            if self.i < 20:
                self.PA.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.PA.draw()
            i = 0

        #Leikmaður 2
        if self.options == [[0, 1]]:
            self.i += 1
            if self.i < 20:
                self.EG.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.EG.draw()
            i = 0



        #GameOver
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                              self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//3, arcade.load_texture("Images/GameOver/GameOver.png"))

    def update(self, delta_time):
        for i, list in enumerate(self.options):
            for j in (0,1):
                self.options[i][j] = 0
        self.options[self.current_option_y][self.current_option_x] = 1

    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
        if key == arcade.key.LEFT:
            if self.current_option_x >0:
                self.current_option_x -= 1
        elif key == arcade.key.RIGHT:
            if self.current_option_x < len(self.options[self.current_option_y])-1:
                self.current_option_x += 1
        elif key == arcade.key.UP:
            pass
        elif key == arcade.key.DOWN:
            pass

        if key == arcade.key.ENTER:
            if self.options == [[1, 0]]:
                window = MainMenu(1200, 600, "Main Menu")

                arcade.window_commands.set_window(self)
                #window.setup()
                arcade.window_commands.close_window()

                self.player.pause()

            elif self.options == [[0, 1]]:
                arcade.window_commands.close_window()
