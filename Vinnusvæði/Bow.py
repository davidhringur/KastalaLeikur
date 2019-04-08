import arcade

class Bow:
    def __init__(self):
        #Setja inn myndir af boganum
        self.Bow_Right = arcade.load_textures("Images/Weapon/greatbow.png",[[54,297,47,56],[167,297,47,56],[296,297,44,56],[416,297,47,56],[540,297,47,56],[672,297,47,56],[801,297,47,56],[928,297,47,56],[1058,297,47,56],[1183,297,47,56],[1316,297,47,56],[1439,297,47,56],[1568,297,47,56]], scale = 12)
        self.Bow_left = arcade.load_textures("Images/Weapon/greatbow.png",[[54,168,47,56],[167,168,47,56],[296,168,44,56],[416,168,47,56],[540,168,47,56],[672,168,47,56],[801,168,47,56],[928,168,47,56],[1058,168,47,56],[1183,168,47,56],[1316,168,47,56],[1439,168,47,56],[1568,168,47,56]], scale = 12)
        self.Bow_Up = arcade.load_textures("Images/Weapon/greatbow2.png",[[291,20,47,56],[291,151,47,56],[291,273,44,56],[291,293,47,56],[291,530,47,56],[291,654,47,56],[291,784,47,56],[291,911,47,56],[291,1043,47,56],[291,1166,47,56],[291,1295,47,56],[291,1422,47,56],[291,1548,47,56]], scale = 12)
        self.Bow_Down = arcade.load_textures("Images/Weapon/greatbow2.png",[[30,30,47,56],[30,154,47,56],[30,288,44,56],[30,416,47,56],[30,544,47,56],[30,674,47,56],[30,804,47,56],[30,927,47,56],[30,1054,47,56],[30,1187,47,56],[30,1315,47,56],[30,1441,47,56],[30,1566,47,56]], scale = 12)


        self.Arrow = arcade.Sprite("Images/Weapon/WEAPON_arrow.png", 2, image_x=150, image_y=229, image_width=36, image_height=18)
        self.ArrowSound = arcade.load_sound("Music/Bow10.mp3")

        #Notað í BowShoot
        self.BowSprite = arcade.Sprite()
        self.BowSprite.width, self.BowSprite.height = 75, 60
        self.BowSprite._texture = self.Bow_Right[0]
        self.BowSprite._texture = self.Bow_left[0]
        self.BowSprite._texture = self.Bow_Up[0]
        self.BowSprite._texture = self.Bow_Down[0]
        self.update_Bow_animation_counter = 0
        self.update_Bow_animation_frame_counter = 5
        self.Bow_gate = 0


        #Notað í Arrow_go
        self.update_Arrow_animation_counter = 0
        self.update_Arrow_animation_frame_counter = 5
        self.Arrow_gate = 0

        #Notað í hit_enemy
        self.hit_frames = 10
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0] #Hit_gate: left, right, up, down
        self.enemys = []

    def BowShoot(self, Player1, player_list):
        if self.update_Bow_animation_counter == 13:
            self.BowSprite.kill()
            self.Bow_gate = 0
            self.update_Bow_animation_counter = 0
        elif self.Bow_gate and self.update_Bow_animation_counter<13:
            if self.update_Bow_animation_counter == 7 and self.update_Bow_animation_frame_counter == 1:
                arcade.play_sound(self.ArrowSound)
            if Player1.face_direction == "up" or Player1.face_direction == "left": #setja sverð undir kallinn fyrir þessar áttir
                Player1.kill()
                player_list.append(Player1.Bow.BowSprite)
                player_list.append(Player1)
            else:
                player_list.append(Player1.Bow.BowSprite)

            if self.update_Bow_animation_frame_counter == 5 or self.update_Bow_animation_counter == 0:  #update sverðið breytist á hverjum 5ta frame
                if Player1.change_x > 0 or Player1.face_direction == "right":
                    self.BowSprite._texture = self.Bow_Right[self.update_Bow_animation_counter]
                elif Player1.change_x < 0 or Player1.face_direction  == "left":
                    self.BowSprite._texture = self.Bow_left[self.update_Bow_animation_counter]
                elif Player1.change_y > 0 or Player1.face_direction  == "up":
                    self.BowSprite._texture = self.Bow_Up[self.update_Bow_animation_counter]
                elif Player1.change_y < 0 or Player1.face_direction  == "down":
                    self.BowSprite._texture = self.Bow_Down[self.update_Bow_animation_counter]

                self.update_Bow_animation_counter += 1


                #self.update_Bow_animation_counter == 0
                self.update_Bow_animation_frame_counter = 0

            if Player1.change_x > 0 or Player1.face_direction == "right": #uppfæra hvar sverðið er
                self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x, Player1.center_y -15
            elif Player1.change_x < 0 or Player1.face_direction == "left": #uppfæra hvar sverðið er
                self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x-20, Player1.center_y -17
            elif Player1.change_y > 0 or Player1.face_direction == "up": #uppfæra hvar sverðið er
                self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x-15, Player1.center_y +5
            elif Player1.change_y < 0 or Player1.face_direction == "down": #uppfæra hvar sverðið er
                self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x-20, Player1.center_y -17

            self.update_Bow_animation_frame_counter += 1

#            self.Arrow_go(Player1.face_direction)

    #def Arrow_go(self, face_direction):
        if self.update_Bow_animation_counter == 10 or self.Arrow_gate:
            self.Arrow.update()
            if self.update_Arrow_animation_frame_counter == 0:
                self.Arrow.center_x, self.Arrow.center_y = self.BowSprite.center_x, self.BowSprite.center_y
                player_list.append(self.Arrow)

                self.Arrow_gate = 1
                if Player1.face_direction == "right":
                    self.Arrow.change_x = 20
                elif Player1.face_direction == "left":
                    self.Arrow.change_x = -20
                elif Player1.face_direction == "up":
                    self.Arrow.change_y = 20
                elif Player1.face_direction == "down":
                    self.Arrow.change_y = -20

            self.update_Arrow_animation_frame_counter += 1


            if self.update_Arrow_animation_frame_counter == 55:
                self.Arrow_gate = 0
                self.Arrow.change_x, self.Arrow.change_y = 0, 0
        else:
            self.Arrow.center_x, self.Arrow.center_y = self.BowSprite.center_x, self.BowSprite.center_y
            self.Arrow.kill()
            self.update_Arrow_animation_frame_counter = 0

    def hit_enemy(self, enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        hit_list = arcade.check_for_collision_with_list(self.Arrow, enemy_sprite_list)
        enemys = []
        if hit_list and self.Arrow_gate == 1:
            for enemy in hit_list:
                enemys.append(enemy)
                enemy.hp -= 50
                if enemy.hp <= 0:
                    enemy.kill()
                    try:
                        enemy.Bow.BowSprite.kill()
                        enemy.Bow.Arrow.kill()
                    except:
                        pass

        self.hit_recoil(enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT)

    def hit_recoil(self, enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.Bow_gate and self.Arrow_gate == 1:
            hit_list = arcade.check_for_collision_with_list(self.Arrow, enemy_sprite_list)
            if hit_list:
                self.Arrow.kill()
                self.Arrow_gate = 0
                self.enemys = hit_list

        safezoneAdj = 50

        for enemy in self.enemys:
            if face_direction == "left" or self.hit_gate == [1,0,0,0]:  #ýtir óvin til vinstri
                self.hit_gate = [1,0,0,0]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1

                    enemy._texture = enemy.take_damage_Left_right_up_down[0]
                    if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                        enemy.center_x -= 10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
                    self.enemys = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
            elif face_direction == "right" or self.hit_gate == [0,1,0,0]:   #ýtir óvin til hægri
                self.hit_gate = [0,1,0,0]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    enemy._texture = enemy.take_damage_Left_right_up_down[1]
                    if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                        enemy.center_x -= -10
                        enemy.change_x = 0
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
                    self.enemys = arcade.SpriteList()
            elif face_direction == "up" or self.hit_gate == [0,0,1,0]:   #ýtir óvin upp
                self.hit_gate = [0,0,1,0]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    enemy._texture = enemy.take_damage_Left_right_up_down[2]
                    if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                        enemy.center_y -= -10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
                    self.enemys = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
            elif face_direction == "down" or self.hit_gate == [0,0,0,1]:   #ýtir óvin niður
                self.hit_gate = [0,0,0,1]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    enemy._texture = enemy.take_damage_Left_right_up_down[3]
                    if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                        enemy.center_y -= 10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
                    self.enemys = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)

            if enemy.__class__.__name__ == "Dragon":      # Lætur dreka meiða sig í sína átt því hann ýtist ekki aftur á bak
                if enemy.face_direction == "left":
                    enemy._texture = enemy.take_damage_Left_right_up_down[0]
                elif enemy.face_direction == "right":
                    enemy._texture = enemy.take_damage_Left_right_up_down[1]
                elif enemy.face_direction == "up":
                    enemy._texture = enemy.take_damage_Left_right_up_down[2]
                elif enemy.face_direction == "down":
                    enemy._texture = enemy.take_damage_Left_right_up_down[3]
