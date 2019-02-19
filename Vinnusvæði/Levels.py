import arcade
from Player import *
import os
import random
import timeit
import Room

class Level_1(arcade.Window):

    def __init__(self, width, height, title):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Köllum á yfirklasann
        super().__init__(width, height, title)

        # Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        self.set_mouse_visible(False)

        # Búum til playerinn
        self.Player1 = None

        # Gimsteinar og teljari
        self.player_list = None
        self.coin_list = None
        self.coun_counter = 0

        # Upplýsingar sem Davíð vill sjá, eyða örgl
        self.processing_time = 0
        self.draw_time = 0
        #set fps
        #self.set_update_rate(1 / 80)

    def setup(self):
        # Setjum upp playerinn
        self.Player1 = Player("Images/Kall.png", 0.2)
        self.Player1.PlayerSetup()
        self.Player1.center_x, self.Player1.center_y = 150, 150


        # Sprite-listi
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_list.append(self.Player1)

        #self.rooms = []
        self.room = Room.setup_room_1()
        #self.rooms.append(room)
        #self.player_list.append(self.Player1.SwordSprite)

        # Búum til gimsteinana
        for i in range(15):

            # Setjum inn myndina við gimsteinana
            coin = arcade.Sprite("Images/gem.png", 0.07)

            # Staðsetjum gimsteinana
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Bætum við gimsteinum við listann
            self.coin_list.append(coin)


    def on_draw(self):
        # Timer
        draw_start_time = timeit.default_timer()

        # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.room.background)

        self.coin_list.draw()
        self.player_list.draw()
        self.room.wall_list_vertical.draw()
        self.room.wall_list_horizontal.draw()
        # Sýna timera
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
            self.player_list.recalculate_spatial_hash(self.Player1.SwordSprite)
            self.Player1.SwordSwing()


        self.Player1.update_animation(5)

        # Gera lista með öllum sprite-um sem rekast í/ skarast við player
        coins_hit_list = arcade.check_for_collision_with_list(self.Player1, self.coin_list)

        if arcade.check_for_collision_with_list(self.Player1, self.room.wall_list_horizontal):
            self.Player1.change_y = 0
        if arcade.check_for_collision_with_list(self.Player1, self.room.wall_list_vertical):
            self.Player1.change_x = 0

        # Loopum í gegnum sprite sem skarast á við og eyðum þeim og bætum við teljara
        for coin in coins_hit_list:
            coin.kill()
            self.coun_counter += 1

        # Vistum tímann sem þetta tekur
        self.processing_time = timeit.default_timer() - start_time


    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
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
            if self.Player1.face_direction == "up"or"left": #setja sverð undir kallinn
                self.Player1.kill()
                self.player_list.append(self.Player1.SwordSprite)
                self.player_list.append(self.Player1)
            else:
                self.player_list.append(self.Player1.SwordSprite)

    def on_key_release(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi hættir að ýta á takka
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Player1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Player1.change_y = 0
        elif key == arcade.key.SPACE:
            self.Player1.sword_gate = 0
            self.Player1.SwordSprite.kill()
