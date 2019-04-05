import arcade
from Bow import Bow

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Enemy(arcade.Sprite):
    def __init__(self,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0,
                 repeat_count_x=1, repeat_count_y=1):
        super(Enemy, self).__init__(filename=filename, scale=scale,
                 image_x=image_x, image_y=image_y,
                 image_width=image_width, image_height=image_height,
                 repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y,
                 center_x=center_x, center_y=center_y)

        self.MOVEMENT_SPEED = 2
        self.hp = 100

        self.hit_frames = 10
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0] #Hit_gate: left, right, up, down
        self.walk_right_textures = arcade.load_textures("Images/Enemy/p3.png",[[3,65,24,31],[35,65,24,31],[67,65,24,31]], scale = 1)
        self.walk_left_textures = arcade.load_textures("Images/Enemy/p3.png",[[5,33,24,31],[37,33,24,31],[69,33,24,31]], scale = 1)
        self.walk_up_textures = arcade.load_textures("Images/Enemy/p3.png",[[1,97,31,31],[33,97,31,31],[65,97,31,31]], scale = 1)
        self.walk_down_textures = arcade.load_textures("Images/Enemy/p3.png",[[1,1,31,31],[33,1,31,32],[65,1,31,31]], scale = 1)
        self.take_damage_Left_right_up_down = arcade.load_textures("Images/Enemy/p33.png",[[3,65,24,31],[5,33,24,31],[1,97,31,31],[1,1,31,31]], scale = 1)

        self.update_animation_counter = 0
        self.update_animation_frame_counter = 0

        self.enemyIsArcher = 0
        self.isTop = 0
        self.Bow = Bow()
        self.place_x, self.place_y = int(), int()



    #Fall sem ræðst á player
    def Attack(self, player, player_list):
        if not self.enemyIsArcher:
            distX = player.center_x - self.center_x
            distY = player.center_y - self.center_y
            sign = lambda x: (1, -1)[x < 0]
            safezoneAdj = 55
            damage = 5
            #færa sig í átt að spilara (Bara lóðrétt og lárétt)
            if player.hp >= 0:
                try:
                    if not arcade.check_for_collision(self, player) and self.hit_gate == [0,0,0,0]:
                        if abs(distX) > abs(distY):
                            self.change_x = sign(distX) * self.MOVEMENT_SPEED
                            self.change_y = 0
                        else:
                            self.change_x = 0
                            self.change_y = sign(distY) * self.MOVEMENT_SPEED

                    elif self.change_x < 0 or self.hit_gate == [1,0,0,0]:  #ýtir leikmanni til vinstri ef óvinur klessir á hann
                        self.hit_gate = [1,0,0,0]
                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[1]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_x -= 10 + player.change_x
                        else:
                            self.hit_gate = [0,0,0,0]
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage
                    elif self.change_x > 0 or self.hit_gate == [0,1,0,0]:   #ýtir leikmanni til hægri ef óvinur klessir á hann
                        self.hit_gate = [0,1,0,0]
                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[0]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_x -= -10 + player.change_x
                        else:
                            self.hit_gate = [0,0,0,0]
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage
                    elif self.change_y > 0 or self.hit_gate == [0,0,1,0]:   #ýtir leikmanni upp ef óvinur klessir á hann
                        self.hit_gate = [0,0,1,0]
                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[3]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_y -= -10 + player.change_y
                        else:
                            self.hit_gate = [0,0,0,0]
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage
                    elif self.change_y < 0 or self.hit_gate == [0,0,0,1]:   #ýtir leikmanni niður ef óvinur klessir á hann
                        self.hit_gate = [0,0,0,1]
                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[2]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_y -= 10 + player.change_y
                        else:
                            self.hit_gate = [0,0,0,0]
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage
                    else:
                        player.hp -= damage
                        self.change_y = 0
                        self.change_x = 0
                        self.center_x -= sign(self.change_x)*4
                        self.center_y -= sign(self.change_y)*4
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_x -= sign(player.change_x)*4
                            player.center_y -= sign(player.change_y)*4

                    if self.hit_gate != [0,0,0,0]:   #Lætur óvin stoppa meðan leykmaður ýtist frá
                        self.change_y = 0
                        self.change_x = 0

                except:
                    pass
            else:
                self.change_y = 0
                self.change_x = 0
        else:
            self.Archer(self.isTop, player, player_list)

    def update_animation(self, frame):
        self.update_animation_frame_counter += 1
        if 0 == self.update_animation_frame_counter % frame:
            self.update_animation_counter += 1

            if  self.change_x > 0:
                self._texture = self.walk_right_textures[self.update_animation_counter % 3]
                self.face_direction = "right"
            elif  self.change_x < 0:
                self._texture = self.walk_left_textures[self.update_animation_counter % 3]
                self.face_direction = "left"
            elif  self.change_y > 0:
                self._texture = self.walk_up_textures[self.update_animation_counter % 3]
                self.face_direction = "up"
            elif  self.change_y < 0:
                self._texture = self.walk_down_textures[self.update_animation_counter % 3]
                self.face_direction = "down"


        if  self.change_x == 0 and self.change_y == 0:
            if self.face_direction == "right":
                self._texture = self.walk_right_textures[0]
            if self.face_direction == "left":
                self._texture = self.walk_left_textures[0]
            if self.face_direction == "up":
                self._texture = self.walk_up_textures[0]
            if self.face_direction == "down":
                self._texture = self.walk_down_textures[0]

    def Archer(self, isTop, player, player_list):
        if player.hp >= 0:
            distX = player.center_x - self.center_x
            distY = player.center_y - self.center_y
            sign = lambda x: (1, -1)[x < 0]

            #try:
            if not arcade.check_for_collision(self, player) and self.hit_gate == [0,0,0,0]:
                colitions = arcade.check_for_collision(self.Bow.Arrow, player)
                safezoneAdj = 55
                damage = 10
                if isTop:
                    self.change_x = sign(distX) * self.MOVEMENT_SPEED
                    self.change_y = 0
                    if colitions:

                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[2]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_y -= 10 + player.change_y
                        else:
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage

                    self.face_direction = "down"
                    self.Bow.BowShoot(self, player_list)
                    #self.change_x, self.change_y = self.place_x, self.place_y
                    self.Bow.Bow_gate = 1


                else:
                    self.change_x = 0
                    self.change_y = sign(distY) * self.MOVEMENT_SPEED

                    if colitions:
                        if self.hit_frames_counter > 0:
                            self.hit_frames_counter -= 1
                            player._texture = player.take_damage_Left_right_up_down[0]
                            if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                                player.center_x -= -10 + player.change_x
                        else:
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage

                    self.face_direction = "right"
                    self.Bow.BowShoot(self, player_list)
                    #self.change_x, self.change_y = self.place_x, self.place_y
                    self.Bow.Bow_gate = 1



                #except:
                #    print("Error in Archer()")

    def update(self):
        #Færa óvin
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.update_animation(10)
