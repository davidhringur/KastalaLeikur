import arcade
from Player import *
from PhysicsEngineHighburn import *
import os
import random
import timeit
import Room

class Level_1(arcade.Window):

    def __init__(self, width, height, title):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Notum smið yfirklasanns
        super().__init__(width, height, title)

        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        # Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        self.set_mouse_visible(False)

        # Búum til playerinn
        self.Player1 = None

        # Gimsteinar og teljari
        self.player_list = None
        self.coun_counter = 0

        # Upplýsingar sem Davíð vill sjá, eyða örgl
        self.processing_time = 0
        self.draw_time = 0
        #setja fps svo hann keyri betur
        self.set_update_rate(1 / 80)

        self.LEFT_RIGHT_UP_DOWN_key_is_down = [0,0,0,0]

    def setup(self):
        # Setjum upp playerinn
        self.Player1 = Player("Images/Kall.png", 0.2)
        #self.Player1.PlayerSetup()
        self.Player1.center_x, self.Player1.center_y = 150, 150
        self.Player1._set_collision_radius = 50


        # Sprite-listi
        self.player_list = arcade.SpriteList()

        self.player_list.append(self.Player1)

        self.rooms = []
        room = Room.setup_room_1(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.rooms.append(room)

        self.move_lenght = self.SCREEN_WIDTH - 40
        self.move_height = self.SCREEN_HEIGHT - 40



         # Create a physics engine for this room
        self.physics_engine = PhysicsEngineHighburn(self.Player1, self.rooms[0].wall_list)

    def move_everything(self, x, y):
        self.player_list.move(x, y)
        self.rooms[0].enemy_list.move(x, y)
        self.rooms[0].wall_list.move(x, y)
        self.rooms[0].coin_list.move(x, y)

        for player in self.player_list:
            player.change_x -= player.change_x
            player.change_y -= player.change_y

    def on_draw(self):
        # Timer
        draw_start_time = timeit.default_timer()

        # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                      self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.rooms[0].background)

        self.rooms[0].coin_list.draw()
        self.player_list.draw()
        self.rooms[0].enemy_list.draw()
        self.rooms[0].wall_list.draw()
        # Sýna timera
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, self.SCREEN_HEIGHT - 20, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, self.SCREEN_HEIGHT - 40, arcade.color.BLACK, 16)

        output = f"Coins hit: {self.coun_counter:3}"
        arcade.draw_text(output, 20, self.SCREEN_HEIGHT - 60, arcade.color.BLACK, 16)
        try:
            fps = 1 / (self.draw_time + self.processing_time)
            output = f"Max FPS: {fps:3.1f}"
            arcade.draw_text(output, 20, self.SCREEN_HEIGHT - 80, arcade.color.BLACK, 16)
        except:
            pass
        self.draw_time = timeit.default_timer() - draw_start_time

    move_gate = 0
    def update(self, delta_time):
        start_time = timeit.default_timer()

        self.Player1.update()
        self.rooms[0].enemy_list.update()
        for enemy in self.rooms[0].enemy_list:
            enemy.Attack(self.Player1)

        self.rooms[0].coin_list.update()


        if self.Player1.sword_gate == 1:
            self.Player1.SwordSwing(self.rooms[0].enemy_list)

        #Uppfæra kallinn að labba á hverjum 5-ta frame(fallið búið til að ofan)
        self.Player1.update_animation(5)

        # Gera lista með öllum sprite-um sem rekast í/ skarast við player
        coins_hit_list = arcade.check_for_collision_with_list(self.Player1, self.rooms[0].coin_list)
        coins_hit_list.extend(arcade.check_for_collision_with_list(self.Player1.SwordSprite, self.rooms[0].coin_list))

        self.physics_engine.update()

        # Loopum í gegnum sprite sem skarast á við og eyðum þeim og bætum við teljara
        for coin in coins_hit_list:
            coin.kill()
            self.coun_counter += 1

        # Vistum tímann sem þetta tekur
        self.processing_time = timeit.default_timer() - start_time

        #Færa alla hluti til þess að fara á næsta borð
        if self.Player1.right > self.SCREEN_WIDTH or self.Player1.center_x < 0 or self.Player1.top > self.SCREEN_HEIGHT or self.Player1.center_y < 0:
            self.move_gate = [self.Player1.center_x < 0, self.Player1.right > self.SCREEN_WIDTH, self.Player1.top > self.SCREEN_HEIGHT, self.Player1.center_y < 0]

        if self.move_lenght > 0 and self.move_gate and self.move_height > 0:
            if self.move_gate[0]:
                self.move_everything(20,0)
                self.move_lenght -= 20
            elif self.move_gate[1]:
                self.move_everything(-20,0)
                self.move_lenght -= 20
            elif self.move_gate[2]:
                self.move_everything(0,-20)
                self.move_height -= 20
            elif self.move_gate[3]:
                self.move_everything(0,20)
                self.move_height -= 20

        elif self.move_lenght <= 0 or self.move_height <= 0:
            self.move_gate = 0
            self.move_lenght = self.SCREEN_WIDTH - 40
            self.move_height = self.SCREEN_HEIGHT - 40
            if self.LEFT_RIGHT_UP_DOWN_key_is_down:
                self.Player1.change_x -= self.LEFT_RIGHT_UP_DOWN_key_is_down[0]*self.Player1.MOVEMENT_SPEED
                self.Player1.change_x += self.LEFT_RIGHT_UP_DOWN_key_is_down[1]*self.Player1.MOVEMENT_SPEED
                self.Player1.change_y += self.LEFT_RIGHT_UP_DOWN_key_is_down[2]*self.Player1.MOVEMENT_SPEED
                self.Player1.change_y -= self.LEFT_RIGHT_UP_DOWN_key_is_down[3]*self.Player1.MOVEMENT_SPEED


    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
        if key == arcade.key.LEFT:
            self.Player1.change_x += -self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[0] = 1
        elif key == arcade.key.RIGHT:
            self.Player1.change_x += self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[1] = 1
        elif key == arcade.key.UP:
            self.Player1.change_y += self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[2] = 1
        elif key == arcade.key.DOWN:
            self.Player1.change_y += -self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[3] = 1
        if key == arcade.key.SPACE:
            self.Player1.sword_gate = 1
            if self.Player1.face_direction == "up" or self.Player1.face_direction == "left": #setja sverð undir kallinn fyrir þessar áttir
                self.Player1.kill()
                self.player_list.append(self.Player1.SwordSprite)
                self.player_list.append(self.Player1)
            else:
                self.player_list.append(self.Player1.SwordSprite)

    def on_key_release(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi hættir að ýta á takka
        if key == arcade.key.LEFT:
            self.Player1.change_x += self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[0] = 0
        elif key == arcade.key.RIGHT:
            self.Player1.change_x += -self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[1] = 0
        elif key == arcade.key.UP:
            self.Player1.change_y += -self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[2] = 0
        elif key == arcade.key.DOWN:
            self.Player1.change_y += self.Player1.MOVEMENT_SPEED
            self.LEFT_RIGHT_UP_DOWN_key_is_down[3] = 0
        elif key == arcade.key.SPACE:
            self.Player1.sword_gate = 0
            self.Player1.SwordSprite.kill()
