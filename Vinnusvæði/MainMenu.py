import arcade
import Player
import Room
import os
from Levels import Levels
#from pick import pick

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

        self.options = [[0, 1]]
        self.current_option_x = 1
        self.current_option_y = 0


        SPRITE_SCALING = 3
        self.p1 = arcade.Sprite("Images/Character/p1_2.png", center_x=self.SCREEN_WIDTH // 4, center_y=self.SCREEN_HEIGHT // 5,
                              scale=SPRITE_SCALING)
        self.p2 = arcade.Sprite("Images/Character/p2_2.png", center_x=self.SCREEN_WIDTH // 1.3333, center_y=self.SCREEN_HEIGHT // 5,
                              scale=SPRITE_SCALING)
#        p2 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)
#        p3 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)
#        p4 = arcade.Sprite("Images/Character/P4.png", SPRITE_SCALING)

#        title = 'Choose a player'
#        options = ['p1', 'p2', 'p3', 'p4']
#        option, index = pick(options, title)
#        print(option)

    i = 0
    def on_draw(self):
    # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                 self.SCREEN_WIDTH, self.SCREEN_HEIGHT, arcade.load_texture("Images/Main/kastali5.jpg"))


        #Leikmaður 1
        if self.options == [[0, 1]]:
            self.i += 1
            if self.i < 20:
                self.p2.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.p2.draw()
            i = 0

        #Leikmaður 2
        if self.options == [[1, 0]]:
            self.i += 1
            if self.i < 20:
                self.p1.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.p1.draw()
            i = 0
        #arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT // 5,
        #                      self.SCREEN_WIDTH//13, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Character/p1_2.png"))

        #Leikmaður 2
        #arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 1.3333, self.SCREEN_HEIGHT // 5,
        #                      self.SCREEN_WIDTH//13, self.SCREEN_HEIGHT//10, arcade.load_texture("Images/Character/p2_2.png"))

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

    def update(self, delta_time):
        for i, list in enumerate(self.options):
            for j in list:
                self.options[i][j] = 0
        self.options[self.current_option_y][self.current_option_x] = 1



    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
        if key == arcade.key.LEFT:
            if self.current_option_x >0:
                self.current_option_x -= 1
        elif key == arcade.key.RIGHT:
            if self.current_option_x < len(self.options):
                self.current_option_x += 1
        elif key == arcade.key.UP:
            pass
        elif key == arcade.key.DOWN:
            pass
        elif key == arcade.key.ENTER:
            window = Levels(1200, 600, "Highburn Fortress", self.options)
            window.setup()
