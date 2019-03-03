import arcade
import Player
import Room
import os
from pick import pick

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

#        p1 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)
#        p2 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)
#        p3 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)
#        p4 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)

#        title = 'Choose a player'
#        options = ['p1', 'p2', 'p3', 'p4']
#        option, index = pick(options, title)
#        print(option)

        self.LEFT_RIGHT_UP_DOWN_key_is_down = [0,0,0,0]

    def on_draw(self):
    # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                 self.SCREEN_WIDTH, self.SCREEN_HEIGHT, arcade.load_texture("Images/Main/kastali5.jpg"))


        #Leikmaður 1
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT // 5,
                              self.SCREEN_WIDTH//13, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Character/P1_2.png"))

        #Leikmaður 2
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 1.3333, self.SCREEN_HEIGHT // 5,
                              self.SCREEN_WIDTH//13, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Character/P2_2.png"))

        #Highburn
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 1.2,
                              self.SCREEN_WIDTH//3, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Main/Highburn.png"))

        #Fortress
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 1.5,
                              self.SCREEN_WIDTH//3, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Main/Fortress.png"))

        #Lovísa
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 9, self.SCREEN_HEIGHT // 25,
                              self.SCREEN_WIDTH//5, self.SCREEN_HEIGHT//30, arcade.load_texture("Images/Main/Lovisa.png"))

        #Jessý
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 25,
                              self.SCREEN_WIDTH//5, self.SCREEN_HEIGHT//30, arcade.load_texture("Images/Main/Jessy.png"))

        #Davíð
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 1.125, self.SCREEN_HEIGHT // 25,
                              self.SCREEN_WIDTH//5, self.SCREEN_HEIGHT//30, arcade.load_texture("Images/Main/David.png"))

        #Veldu leikmann
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                              self.SCREEN_WIDTH//5, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Main/Choose.png"))

        #Main menue
#        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 10, self.SCREEN_HEIGHT // 10,
#                              self.SCREEN_WIDTH//10, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Main/Main.png"))
