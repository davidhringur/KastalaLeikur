import arcade
import Player
import Room
import pick
import os

class MainMenu(arcade.Window):

    def __init__(self, width, height, title=""):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #Notum smið yfirklasanns
        super().__init__(width, height, title)

        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        #Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        self.set_mouse_visible(False)


    def on_draw(self):
    #Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                  self.SCREEN_WIDTH, self.SCREEN_HEIGHT, arcade.load_texture("Images/ModelPack/MakingMap1.png"))
