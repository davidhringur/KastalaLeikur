import arcade

class Sword:
    def __init__(self):
        self.sword_DownRight = arcade.load_textures("Images/Weapon/Sword_DownRight.png",[[94,35,25,20],[158,34,25,20],[221,29,25,20],[285,29,25,20]], scale = 12)
        self.sword_UpLeft = arcade.load_textures("Images/Weapon/Sword_UpLeft.png",[[73,12,26,32],[138,12,26,32],[202,12,26,32],[266,12,26,32]], scale = 12)
        self.sword_UpRight = arcade.load_textures("Images/Weapon/Sword_UpRight.png",[[83,11,35,26],[148,11,35,26],[213,11,35,26],[278,11,35,26]], scale = 14)
        self.sword_DownLeft = arcade.load_textures("Images/Weapon/Sword_DownLeft.png",[[74,34,33,23],[137,34,33,23],[201,34,33,23],[266,34,33,23]], scale = 12)
        #Hljóðfile
        self.SwordSound = arcade.load_sound("Music/Sword.mp3")

        #Notað í SwordSwing
        self.SwordSprite = arcade.Sprite()
        self.SwordSprite.width, self.SwordSprite.height = 75, 60
        self.SwordSprite._texture = self.sword_DownRight[0]
        self.update_Sword_animation_counter = 0
        self.update_Sword_animation_frame_counter = 0
        self.sword_gate = 0
        #self.sword_gate_que = 0
        self.face_direction_placeholder = None

        #Notað í hit_enemy
        self.hit_frames = 16
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0] #Hit_gate: left, right, up, down
        self.enemys = []

    def SwordSwing(self, Player1, player_list, frame):
        if self.sword_gate and self.update_Sword_animation_counter<4:

            if Player1.face_direction == "up" or Player1.face_direction == "left": #setja sverð undir kallinn fyrir þessar áttir
                Player1.kill()
                player_list.append(Player1.Sword.SwordSprite)
                player_list.append(Player1)
                if self.update_Sword_animation_counter == 0:
                    arcade.play_sound(self.SwordSound)
            else:
                player_list.append(Player1.Sword.SwordSprite)
                if self.update_Sword_animation_counter == 0:
                    arcade.play_sound(self.SwordSound)

            if self.update_Sword_animation_frame_counter == frame or self.update_Sword_animation_counter == 0:            #update sverðið breytist á hverjum 5ta frame

                if Player1.change_x > 0 or Player1.face_direction == "right":
                    self.SwordSprite._texture = self.sword_DownRight[self.update_Sword_animation_counter]
                elif Player1.change_x < 0 or Player1.face_direction == "left":
                    self.SwordSprite._texture = self.sword_UpLeft[self.update_Sword_animation_counter]
                elif Player1.change_y > 0 or Player1.face_direction == "up":
                    self.SwordSprite._texture = self.sword_UpRight[self.update_Sword_animation_counter]
                elif Player1.change_y < 0 or Player1.face_direction == "down":
                    self.SwordSprite._texture = self.sword_DownLeft[self.update_Sword_animation_counter]


                self.update_Sword_animation_counter += 1

                #self.update_Sword_animation_counter == 0
                self.update_Sword_animation_frame_counter = 0


            self.update_Sword_animation_frame_counter += 1

        elif self.update_Sword_animation_counter == 4:
            self.SwordSprite.kill()
            self.sword_gate = 0
            self.update_Sword_animation_counter = 0

        if Player1.face_direction == "right": #uppfæra hvar sverðið er
            self.SwordSprite.center_x, self.SwordSprite.center_y = Player1.center_x + 20, Player1.center_y - 20
        elif Player1.face_direction == "left":
            self.SwordSprite.center_x, self.SwordSprite.center_y = Player1.center_x - 10, Player1.center_y
        elif Player1.face_direction == "up":
            self.SwordSprite.center_x, self.SwordSprite.center_y = Player1.center_x, Player1.center_y
        elif Player1.face_direction == "down":
            self.SwordSprite.center_x, self.SwordSprite.center_y = Player1.center_x - 4, Player1.center_y - 23


    def hit_enemy(self, enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        hit_list = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)

        if hit_list and self.sword_gate == 1:

            for enemy in hit_list:
                if not enemy in self.enemys: #Bara hitta einusinni i hverri sveiflu
                    enemy.hp -= 20
                    if enemy.hp <= 0:
                        enemy.kill()
                        try:
                            enemy.Bow.BowSprite.kill()
                            enemy.Bow.Arrow.kill()
                        except:
                            pass
                self.enemys.append(enemy)

        self.hit_recoil(enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT)

    def hit_recoil(self, enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.sword_gate:
            hit_list = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)
            if hit_list:
                self.enemys = hit_list
                if self.hit_frames_counter == self.hit_frames:
                    self.face_direction_placeholder = face_direction
                    print(face_direction)

        safezoneAdj = 50
        try:
            for enemy in self.enemys:
                if self.face_direction_placeholder == "left" or self.hit_gate == [1,0,0,0]:  #ýtir óvin til vinstri
                    self.hit_gate = [1,0,0,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        enemy._texture = enemy.take_damage_Left_right_up_down[0]
                        if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                            enemy.center_x -= 10
                    else:
                        self.hit_gate = [0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        self.enemys = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)
                elif self.face_direction_placeholder == "right" or self.hit_gate == [0,1,0,0]:   #ýtir óvin til hægri
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
                        self.enemys = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)
                elif self.face_direction_placeholder == "up" or self.hit_gate == [0,0,1,0]:   #ýtir óvin upp
                    self.hit_gate = [0,0,1,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        enemy._texture = enemy.take_damage_Left_right_up_down[2]
                        if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                            enemy.center_y -= -10
                    else:
                        self.hit_gate = [0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        self.enemys = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)
                elif self.face_direction_placeholder == "down" or self.hit_gate == [0,0,0,1]:   #ýtir óvin niður
                    self.hit_gate = [0,0,0,1]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        enemy._texture = enemy.take_damage_Left_right_up_down[3]
                        if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                            enemy.center_y -= 10
                    else:
                        self.hit_gate = [0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        self.enemys = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)

                if enemy.__class__.__name__ == "Dragon":      # Lætur dreka meiða sig í sína átt því hann ýtist ekki aftur á bak
                    if enemy.face_direction == "left":
                        enemy._texture = enemy.take_damage_Left_right_up_down[0]
                    elif enemy.face_direction == "right":
                        enemy._texture = enemy.take_damage_Left_right_up_down[1]
                    elif enemy.face_direction == "up":
                        enemy._texture = enemy.take_damage_Left_right_up_down[2]
                    elif enemy.face_direction == "down":
                        enemy._texture = enemy.take_damage_Left_right_up_down[3]
        except:
            pass
