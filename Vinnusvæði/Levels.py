import arcade
from Player import *
from PhysicsEngineHighburn import *
import os
import random
import timeit
import Room
from HUD import HP_meter
import pyglet
from GameOver import *

class Levels(arcade.Window):

    def __init__(self, width, height, title, MainMenuOptions):

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Notum smið yfirklasanns
        super().__init__(width, height, title)

        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        # Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        self.set_mouse_visible(False)


        self.MainMenuOptions = MainMenuOptions

        #Level insex sem við erum á
        self.Level_idx = 1

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

        self.draw_end = 0




    def setup(self):
        #Fylki sem segir okkur havða takki er niðri
        self.LEFT_RIGHT_UP_DOWN_key_is_down = [0,0,0,0]

        # Líf leikmanns í síðasta frame
        self.lastHP = None

        #Hljóðfile og tónlistarplayer (pyglet player því arcade létu hann ekki inn í sitt library...)
        self.FireSound = arcade.load_sound("Music/Fireball.wav")

        self.player = pyglet.media.Player()
        self.player.queue(pyglet.media.load("Music/Illusion_of_Gaia.wav",  streaming=False))
        self.player.queue(pyglet.media.load("Music/Wizardry_8.wav",  streaming=False))
        self.player.volume = 0.1
        self.player.play()

        #game over
        self.game_over = 0

        # Setjum upp playerinn
        self.Player1 = Player(self.MainMenuOptions,"Images/Character/p1_2.png", scale=2)
        self.Player1.center_x, self.Player1.center_y = 100, 100
        self.Player1._set_collision_radius = 50
        self.Player1.points = ((-30.0, -32.0), (30.0, -32.0), (30.0, 0), (-30.0, 0))


        # Sprite-listi
        self.player_list = arcade.SpriteList()

        self.player_list.append(self.Player1)

        self.rooms = []
        room1 = Room.setup_room_1(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.rooms.append(room1) #room2 er bætt við þegar leikmaður fer á næsta borð

        self.HP_meter = HP_meter()

        self.GameOver = EndGame(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.move_lenght = self.SCREEN_WIDTH - 40
        self.move_height = self.SCREEN_HEIGHT - 40
        self.door_move_dist = 42



        #Búa til physics engine fyrir þetta herbergi
        self.physics_engine = []
        self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[0].wall_list))
        self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[0].door))
        for enemy in self.rooms[0].enemy_list:
            self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[0].wall_list))

        self.move_gate = 0 #Notað til að færa allt þegar skipt er um borð
        self.door_move_count = [0, 0, 1, 1]
        self.Level_idxBoss = 0

        #Texti
        self.text1_countdown, self.text2_countdown = 300, 800
        self.help_dragon_text = arcade.Sprite("Images/GameOver/help-dragon-text.png", scale= 0.4)
        self.help_dragon_text.center_x, self.help_dragon_text.center_y = self.SCREEN_WIDTH/2, 570
        self.thank_you_text = arcade.Sprite("Images/GameOver/thank-you-text.png", scale= 0.4)
        self.thank_you_text.center_x, self.thank_you_text.center_y = self.SCREEN_WIDTH/2, 470
        self.save_charactrer = arcade.Sprite("Images\Character\save_caracter.png",image_x=4,image_y=0,image_width=25,image_height=32, scale=2)


    def move_everything(self, x, y):
        self.player_list.move(x, y)
        for i in range(self.Level_idx):
            self.rooms[i].enemy_list.move(x, y)
            self.rooms[i].wall_list.move(x, y)
            self.rooms[i].coin_list.move(x, y)
            self.rooms[i].prop_list.move(x, y)
            self.rooms[i].door.move(x, y)

        for player in self.player_list:
            player.center_x -= player.change_x
            player.center_y -= player.change_y

    def on_draw(self):
        # Timer
        draw_start_time = timeit.default_timer()

        # Köllum á þetta í hvert sinn sem glugginn er opnaður
        arcade.start_render()

        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2,
                                      self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.rooms[0].background)

        for i in range(self.Level_idx):
            self.rooms[i].coin_list.draw()
            self.rooms[i].enemy_list.draw()
            self.rooms[i].wall_list.draw()
            self.rooms[i].prop_list.draw()
            self.rooms[i].pillars.draw()
            self.rooms[i].fire.draw()
            self.rooms[i].door.draw()

        self.player_list.draw()

        # Setjum líf inn
        self.HP_meter.bars.draw()

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

        if self.game_over == 1:
            self.GameOver.update(self.Player1)

        if self.Level_idx == 1 and self.text1_countdown > 0:
            self.text1_countdown -= 1
            self.help_dragon_text.draw()
        if self.draw_end == 1 and self.text2_countdown > 0:
            if self.text2_countdown == 800:
                self.player.queue(pyglet.media.load("Music/Overwatch_8-Bit.wav",  streaming=False))
                self.player.next_source()
                #self.savelist = arcade.SpriteList(); self.savelist.append(self.save_charactrer)
                #self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.savelist))
            self.text2_countdown -= 1
            self.save_charactrer.draw()
            self.Player1.kill()
            self.player_list.append(self.Player1)
            self.thank_you_text.draw()
            if self.text2_countdown == 0:
                self.game_over = 1
                self.Player1.change_x, self.Player1.change_y = 0, 0

    def update(self, delta_time):


        start_time = timeit.default_timer()

        self.lastHP = self.Player1.hp
        self.Player1.update()
        for i in range(self.Level_idx):
            self.rooms[i].enemy_list.update()
            for enemy in self.rooms[i].enemy_list:
                enemy.Attack(self.Player1, self.player_list)

            self.rooms[i].coin_list.update()
            self.rooms[i].prop_list.update()
            if self.Player1.Sword.sword_gate == 1 or self.Player1.Sword.hit_frames_counter > 0:
                self.Player1.Sword.hit_enemy(self.rooms[i].enemy_list, self.Player1.face_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

            if self.Player1.Bow.Arrow_gate == 1 or self.Player1.Bow.hit_gate != [0,0,0,0]:
                self.Player1.Bow.hit_enemy(self.rooms[i].enemy_list, self.Player1.face_direction, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)


        # Sveifla sverði
        self.Player1.Sword.SwordSwing(self.Player1, self.player_list, 5)

        # Skjóta boga
        self.Player1.Bow.BowShoot(self.Player1, self.player_list)

        # Gera lista með öllum sprite-um sem rekast í/ skarast við player
        coins_hit_list = arcade.check_for_collision_with_list(self.Player1, self.rooms[0].coin_list)

        # Láta leikmann rekast á veggi o.s.f..
        for engine in self.physics_engine:
            engine.update()

        # Loopum í gegnum sprite sem skarast á við og eyðum þeim og bætum við teljara
        for coin in coins_hit_list:
            coin.kill()
            self.coun_counter += 1

        # Uppfærum líf
        if self.lastHP > self.Player1.hp:
            self.HP_meter.update(self.Player1)
        if self.Level_idx == 4:
            self.rooms[3].DragonHP.updateHP(self.rooms[3].dragon, self.rooms[3].prop_list)

        # Vistum tímann sem þetta tekur
        self.processing_time = timeit.default_timer() - start_time

        #Uppfæra eld á borði 2
        if self.Level_idx == 2:
            for pillar in self.rooms[1].pillars:
                pillar.updateFire(self.Player1.Sword, self.rooms[1].fire)

    #Færa alla hluti til þess að fara á næsta borð
        if self.Player1.right > self.SCREEN_WIDTH or self.Player1.center_x < 0 or self.Player1.top > self.SCREEN_HEIGHT or self.Player1.center_y < 0:
            self.move_gate = [self.Player1.center_x < 0, self.Player1.right > self.SCREEN_WIDTH, self.Player1.top > self.SCREEN_HEIGHT, self.Player1.center_y < 0]

        if self.move_lenght > 0 and self.move_gate and self.move_height > 0:
            if self.move_gate[0]:
                if self.Level_idx == 3:
                    room4 = Room.setup_room_4(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.rooms[0].wall_list, self.rooms[2].wall_list)
                    self.rooms[0].wall_list, self.rooms[2].wall_list = arcade.SpriteList(), arcade.SpriteList()
                    self.rooms.append(room4)
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[3].wall_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[3].prop_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[3].door))
                    for enemy in self.rooms[3].enemy_list:
                        self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[3].prop_list))
                        self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[3].wall_list))
                    self.player.next_source()
                    self.Level_idx += 1
                self.move_everything(20,0)
                self.move_lenght -= 20
                if self.move_lenght == 0 and self.Level_idx == 4: # þegar allt er buið að  hreyfast eftir borð 3 setjum við þetta ferli i gang
                    self.Level_idxBoss = 1
                    self.rooms[2].door.move(0, -800)


            elif self.move_gate[1]:

                if self.Level_idx == 1:
                    room2 = Room.setup_room_2(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                    self.rooms.append(room2)
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[1].wall_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[1].prop_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[1].door))
                    for enemy in self.rooms[1].enemy_list:
                       self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[1].prop_list))
                       self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[1].wall_list))
                    self.Level_idx += 1
                self.move_everything(-20,0)
                self.move_lenght -= 20

            elif self.move_gate[2]:
                if self.Level_idx == 2:
                    room3 = Room.setup_room_3(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                    self.rooms.append(room3)
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[2].wall_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[2].prop_list))
                    self.physics_engine.append(PhysicsEngineHighburn(self.Player1, self.rooms[2].door))
                    for enemy in self.rooms[2].enemy_list:
                        if not enemy.enemyIsArcher:
                            self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[2].prop_list))
                            self.physics_engine.append(PhysicsEngineHighburn(enemy, self.rooms[2].wall_list))
                    self.Level_idx += 1
                self.move_everything(0,-20)
                self.move_height -= 20
            elif self.move_gate[3]:
                self.move_everything(0,20)
                self.move_height -= 20

        elif self.move_lenght <= 0 or self.move_height <= 0:
            self.move_gate = 0
            self.move_lenght = self.SCREEN_WIDTH - 40
            self.move_height = self.SCREEN_HEIGHT - 40
            #if self.LEFT_RIGHT_UP_DOWN_key_is_down:
            #    self.Player1.change_x -= self.LEFT_RIGHT_UP_DOWN_key_is_down[0]*self.Player1.MOVEMENT_SPEED
            #    self.Player1.change_x += self.LEFT_RIGHT_UP_DOWN_key_is_down[1]*self.Player1.MOVEMENT_SPEED
            #    self.Player1.change_y += self.LEFT_RIGHT_UP_DOWN_key_is_down[2]*self.Player1.MOVEMENT_SPEED
            #    self.Player1.change_y -= self.LEFT_RIGHT_UP_DOWN_key_is_down[3]*self.Player1.MOVEMENT_SPEED

        #Open doors for next Levels
        if self.coun_counter >= 15 and self.door_move_count[0] < self.door_move_dist:
            self.door_move_count[0] += 1
            self.rooms[0].door.move(1, 0)
        elif self.door_move_count[0] == self.door_move_dist:
            self.door_move_count[0] += 1
            self.rooms[0].door = arcade.SpriteList()

        elif self.Level_idx == 2:
            if self.rooms[1].fire.lever_count == 4 and self.door_move_count[1] < self.door_move_dist:
                if self.door_move_count[1] == 0:
                    arcade.play_sound(self.FireSound)
                self.door_move_count[1] += 1
                self.rooms[1].door.move(0, 1)
            elif self.door_move_count[1] == self.door_move_dist:
                self.door_move_count[1] += 1
                self.rooms[1].door = arcade.SpriteList()

        elif self.Level_idx == 3:
            if not self.rooms[2].enemy_list and self.door_move_count[2] < self.door_move_dist:
                self.door_move_count[2] += 1
                self.rooms[2].door.move(-1, 0)
            elif self.door_move_count[2] == self.door_move_dist:
                self.door_move_count[2] += 1
                self.rooms[2].door.move(2*self.door_move_dist, 800)

        elif self.Level_idxBoss == 1:
            if self.door_move_count[3] < self.door_move_dist and self.Player1.center_x < self.SCREEN_WIDTH - 160:
                self.door_move_count[3] += 1
                self.rooms[2].door.move(-1, 0)
            elif self.door_move_count[3] == self.door_move_dist:
                if self.rooms[3].dragon.hp <= 0:
                    self.save_charactrer.center_x, self.save_charactrer.center_y = self.rooms[3].dragon.center_x, self.rooms[3].dragon.center_y
                    self.thank_you_text.center_x, self.thank_you_text.center_y = self.save_charactrer.center_x - 100, self.save_charactrer.center_y + 25
                    self.draw_end = 1



        if self.Player1.hp <= 0:
            self.game_over = 1



    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
        if self.Player1.hp >= 0 and self.game_over == 0:
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
                self.Player1.Sword.sword_gate = 1
            if key == arcade.key.Z:
                self.Player1.Bow.Bow_gate = 1

        elif self.game_over == 1:
            if key == arcade.key.LEFT:
                pass
            elif key == arcade.key.RIGHT:
                pass
            elif key == arcade.key.UP and self.GameOver.options > 0:
                self.GameOver.options -= 1
            elif key == arcade.key.DOWN and self.GameOver.options < 1:
                self.GameOver.options += 1
            elif key == arcade.key.ENTER:
                if self.GameOver.options == 0:
                    self.GameOver.newGame()
                    arcade.window_commands.set_window(self)
                    self.player.pause()
                    arcade.window_commands.close_window()

                elif self.GameOver.options == 1:
                    arcade.window_commands.set_window(self)
                    arcade.window_commands.close_window()




    def on_key_release(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi hættir að ýta á takka
        if self.Player1.hp >= 0 and self.game_over == 0:
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
                pass
                #self.Player1.Sword.sword_gate_que = 1
                #self.Player1.Sword.SwordSprite.kill()
