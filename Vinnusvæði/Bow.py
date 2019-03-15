import arcade

class Bow:
    def __init__(self):
        self.Bow_Right = arcade.load_textures("Images/Weapon/greatbow.png",[[54,297,47,56],[167,297,47,56],[296,297,44,56],[416,297,47,56],[540,297,47,56],[672,297,47,56],[801,297,47,56],[928,297,47,56],[1058,297,47,56],[1183,297,47,56],[1316,297,47,56],[1439,297,47,56],[1568,297,47,56]], scale = 12)
        #self.Bow_UpLeft = arcade.load_textures("Images/Weapon/Bow_UpLeft.png",[[73,12,26,32],[138,12,26,32],[202,12,26,32],[266,12,26,32]], scale = 12)
        #self.Bow_UpRight = arcade.load_textures("Images/Weapon/Bow_UpRight.png",[[83,11,35,26],[148,11,35,26],[213,11,35,26],[278,11,35,26]], scale = 14)
        #self.Bow_DownLeft = arcade.load_textures("Images/Weapon/Bow_DownLeft.png",[[74,34,33,23],[137,34,33,23],[201,34,33,23],[266,34,33,23]], scale = 12)

        #Notað í BowShoot
        self.BowSprite = arcade.Sprite()
        self.BowSprite.width, self.BowSprite.height = 75, 60
        self.BowSprite._texture = self.Bow_Right[0]
        self.update_Bow_animation_counter = 0
        self.update_Bow_animation_frame_counter = 5
        self.Bow_gate = 0

        #Notað í hit_enemy
        self.hit_frames = 10
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0] #Hit_gate: left, right, up, down
        self.enemys = []

    def BowShoot(self, Player1, player_list):
        if self.Bow_gate and self.update_Bow_animation_counter<13:
            if Player1.face_direction == "up" or Player1.face_direction == "left": #setja sverð undir kallinn fyrir þessar áttir
                Player1.kill()
                player_list.append(Player1.Bow.BowSprite)
                player_list.append(Player1)
            else:
                player_list.append(Player1.Bow.BowSprite)

            if self.update_Bow_animation_frame_counter == 5:            #update sverðið breytist á hverjum 5ta frame
                if Player1.change_x > 0 or Player1.face_direction == "right":
                    self.BowSprite._texture = self.Bow_Right[self.update_Bow_animation_counter]
            #    elif Player1.change_x < 0 or Player1.face_direction == "left":
            #        self.BowSprite._texture = self.Bow_UpLeft[self.update_Bow_animation_counter]
            #    elif Player1.change_y > 0 or Player1.face_direction == "up":
            #        self.BowSprite._texture = self.Bow_UpRight[self.update_Bow_animation_counter]
            #    elif Player1.change_y < 0 or Player1.face_direction == "down":
            #        self.BowSprite._texture = self.Bow_DownLeft[self.update_Bow_animation_counter]
                self.update_Bow_animation_counter += 1


                self.update_Bow_animation_counter == 0
                self.update_Bow_animation_frame_counter = 0

            if Player1.change_x > 0 or Player1.face_direction == "right": #uppfæra hvar sverðið er
                self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x, Player1.center_y -15
            #elif Player1.change_x < 0 or Player1.face_direction == "left":
            #    self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x - 10, Player1.center_y
            #elif Player1.change_y > 0 or Player1.face_direction == "up":
            #    self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x, Player1.center_y
            #elif Player1.change_y < 0 or Player1.face_direction == "down":
            #    self.BowSprite.center_x, self.BowSprite.center_y = Player1.center_x - 4, Player1.center_y - 23

            self.update_Bow_animation_frame_counter += 1

        elif self.update_Bow_animation_counter == 13:
            self.BowSprite.kill()
            self.Bow_gate = 0
            self.update_Bow_animation_counter = 0

    def hit_enemy(self, enemy_sprite_list, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        hit_list = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
        enemys = []
        if hit_list:

            for enemy in hit_list:
                enemys.append(enemy)
                enemy.hp -= 10
                enemy._set_color=(124, 10, 2)
                if enemy.hp <= 0:
                    enemy.kill()

    def hit_recoil(self, enemy_sprite_list, Bow_gate, face_direction, SCREEN_WIDTH, SCREEN_HEIGHT):
        if Bow_gate:
            hit_list = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
            if hit_list:
                self.enemys = hit_list

        safezoneAdj = 50
        try:
            for enemy in self.enemys:
                if face_direction == "left" or self.hit_gate == [1,0,0,0]:  #ýtir óvin til vinstri
                    self.hit_gate = [1,0,0,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
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
                        if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                            enemy.center_x -= -10
                            enemy.change_x = 0
                    else:
                        self.hit_gate = [0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        self.enemys = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
                elif face_direction == "up" or self.hit_gate == [0,0,1,0]:   #ýtir óvin upp
                    self.hit_gate = [0,0,1,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
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
                        if enemy.bottom > safezoneAdj and enemy.top < SCREEN_HEIGHT-safezoneAdj and enemy.left > safezoneAdj and enemy.right < SCREEN_WIDTH-safezoneAdj:
                            enemy.center_y -= 10
                    else:
                        self.hit_gate = [0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        self.enemys = arcade.check_for_collision_with_list(self.BowSprite, enemy_sprite_list)
        except:
            pass
