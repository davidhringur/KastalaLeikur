import arcade
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Dragon(arcade.Sprite):
    def __init__(self, wall_list,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0,
                 repeat_count_x=1, repeat_count_y=1):
        super(Dragon, self).__init__(filename=filename, scale=scale,
                 image_x=image_x, image_y=image_y,
                 image_width=image_width, image_height=image_height,
                 repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y,
                 center_x=center_x, center_y=center_y)

        self.MOVEMENT_SPEED = 4
        self.hp = 500

        self.hit_frames = 10
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0,0] #Hit_gate: left, right, up, down
        self.walk_right_textures = arcade.load_textures("Images/Enemy/dragon.png",[[2,67,60,60],[66,67,60,60],[130,67,60,60]], scale = 3)
        self.walk_left_textures = arcade.load_textures("Images/Enemy/dragon.png",[[2,2,60,60],[66,2,60,60],[130,2,60,60]], scale = 3)
        self.walk_up_textures = arcade.load_textures("Images/Enemy/dragon.png",[[2,195,60,60],[66,195,60,60],[130,195,60,60]], scale = 3)
        self.walk_down_textures = arcade.load_textures("Images/Enemy/dragon.png",[[2,131,60,60],[66,131,60,60],[130,131,60,60]], scale = 3)
        self.take_damage_Left_right_up_down = arcade.load_textures("Images/Enemy/dragonDamage.png",[[2,2,60,60],[2,67,60,60],[2,195,60,60],[2,131,60,60]], scale = 1)

        # Eldur
        self.fire_left = arcade.load_textures("Images/Enemy/fireball.png",[[2,23,56,19],[66,23,56,19],[130,23,56,19],[194,23,56,19],[258,23,56,19],[322,23,56,19],[385,23,56,19],[449,23,56,19]], scale = 3)
        self.fire_right = arcade.load_textures("Images/Enemy/fireball.png",[[2,280,60,19],[66,280,60,19],[130,280,60,19],[194,280,60,19],[258,280,56,19],[322,280,60,19],[385,280,60,19],[449,280,60,19]], scale = 3)
        self.fire_right_down = arcade.load_textures("Images/Enemy/fireball.png",[[13,341,46,27],[75,341,46,27],[142,341,46,27],[202,341,46,27],[272,341,46,27],[333,341,46,27],[397,341,46,27],[460,341,46,27]], scale = 3)
        self.fire_down = arcade.load_textures("Images/Enemy/fireball.png",[[23,402,19,36],[87,402,19,36],[150,402,19,36],[214,402,19,36],[280,402,19,36],[344,402,19,36],[408,402,19,36],[472,402,19,36]], scale = 3)
        self.fire_left_down = arcade.load_textures("Images/Enemy/fireball.png",[[9,469,46,30],[73,469,46,30],[137,469,46,30],[201,469,46,30],[264,469,46,30],[329,469,46,30],[392,469,46,30],[452,469,46,30]], scale = 3)
        self.fire_textures = None
        self.fireball = arcade.Sprite("Images/Enemy/fireball.png",image_x=23,image_y=402,image_width=19,image_height=36, scale=2)
        self.firebal_animation_counter = 0
        self.firebal_animation_frame_counter = 0

        # Fyrir animations
        self.update_animation_counter = 0
        self.update_animation_frame_counter = 0

        self.player_take_damage = 80

        # Fyrir move()
        self.wall_list = wall_list
        self.stage = 1
        self.stage_changer = 0


    #Fall sem ræðst á player
    def Attack(self, player, player_list):

        #Meiða ef við förum í drekann
        sign = lambda x: x and (1, -1)[x < 0]
        safezoneAdj = 55
        damage = 5
        if player.hp >= 0:
            try:
                if not arcade.check_for_collision(self, player) and self.hit_gate == [0,0,0,0,0]:
                    self.Move(player, player_list) # Færa drekann

                elif player.change_x > 0 or self.hit_gate == [1,0,0,0,0]:  #ýtir leikmanni til vinstri ef óvinur klessir á hann
                    self.hit_gate = [1,0,0,0,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        player._texture = player.take_damage_Left_right_up_down[1]
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_x -= 10 + player.change_x
                    else:
                        self.hit_gate = [0,0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        player.hp -= damage
                elif player.change_x < 0 or self.hit_gate == [0,1,0,0,0]:   #ýtir leikmanni til hægri ef óvinur klessir á hann
                    self.hit_gate = [0,1,0,0,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        player._texture = player.take_damage_Left_right_up_down[0]
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_x -= -10 + player.change_x
                    else:
                        self.hit_gate = [0,0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        player.hp -= damage
                elif player.change_y < 0 or self.hit_gate == [0,0,1,0,0]:   #ýtir leikmanni upp ef óvinur klessir á hann
                    self.hit_gate = [0,0,1,0,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        player._texture = player.take_damage_Left_right_up_down[3]
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_y -= -10 + player.change_y
                    else:
                        self.hit_gate = [0,0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        player.hp -= damage
                elif player.change_y > 0 or self.hit_gate == [0,0,0,1,0]:   #ýtir leikmanni niður ef óvinur klessir á hann
                    self.hit_gate = [0,0,0,1,0]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        player._texture = player.take_damage_Left_right_up_down[2]
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_y -= 10 + player.change_y
                    else:
                        self.hit_gate = [0,0,0,0,0]
                        self.hit_frames_counter = self.hit_frames
                        player.hp -= damage

                elif player.change_y == 0 or player.change_x == 0 or self.hit_gate == [0,0,0,0,1]:
                    self.hit_gate = [0,0,0,0,1]
                    if self.hit_frames_counter > 0:
                        self.hit_frames_counter -= 1
                        player._texture = player.take_damage_Left_right_up_down[2]
                        if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                            player.center_y += 10*sign(self.change_y)
                            player.center_x += 10*sign(self.change_x)
                        else:
                            self.hit_gate = [0,0,0,0,0]
                            self.hit_frames_counter = self.hit_frames
                            player.hp -= damage


                #if self.hit_gate != [0,0,0,0]:   #Lætur óvin stoppa meðan leykmaður ýtist frá
                #    self.change_y = 0
                #    self.change_x = 0

            except:
                pass



    def Move(self, player, player_list):
        if self.stage == 1:
            if arcade.check_for_collision_with_list(self, self.wall_list):
                if self.change_y < 0:
                    self. center_y -= self.change_y
                    self.change_x, self.change_y = -self.change_y, self.change_x
                elif self.change_x > 0:
                    self. center_x -= self.change_x
                    self.change_x, self.change_y = self.change_y, self.change_x
                elif self.change_y > 0:
                    self. center_y -= self.change_y
                    self.change_x, self.change_y = -self.change_y, self.change_x
                    self.stage_changer += 1
                    if self.stage_changer == 1:
                        self.stage = 2
                elif self.change_x < 0:
                    self. center_x -= self.change_x
                    self.change_x, self.change_y = self.change_y, self.change_x
        elif self.stage == 2:
            if self.center_x < SCREEN_WIDTH/2:
                self.change_x, self.change_y = 0, 0
                self.face_direction = "down"
                self.fireball_Shoot(player, player_list)

    def fireball_Shoot(self, player, player_list):
        sign = lambda x: x and (1, -1)[x < 0]
        delta_x = player.center_x - self.center_x
        delta_y = player.center_y - self.center_y
        angle = abs(math.atan(delta_x/delta_y))
        fireball_speed = 10
        fireball_speed_x, fireball_speed_y = int(math.sin(angle)*fireball_speed)*sign(delta_x), int(math.cos(angle)*fireball_speed)*sign(delta_y)
        if self.firebal_animation_frame_counter == 0:
            player_list.append(self.fireball)
            self.fireball.center_x, self.fireball.center_y = self.center_x, self.center_y
            self.fireball.change_x, self.fireball.change_y = fireball_speed_x, fireball_speed_y

            if math.atan(delta_x/delta_y) < 0.55 and -0.55 < math.atan(delta_x/delta_y):
                self.fire_textures = self.fire_down
                self.fireball.width,self.fireball.height = 19*2, 36*2
            elif math.atan(delta_x/delta_y) < 1.3 and 0.55 < math.atan(delta_x/delta_y):
                self.fire_textures = self.fire_left_down
                self.fireball.width,self.fireball.height = 46*2, 30*2
            elif math.atan(delta_x/delta_y) < -0.55 and -1.3 < math.atan(delta_x/delta_y):
                self.fire_textures = self.fire_right_down
                self.fireball.width,self.fireball.height = 46*2, 27*2
            elif math.atan(delta_x/abs(delta_y)) < 2 and 1.3 < math.atan(delta_x/abs(delta_y)):
                self.fire_textures = self.fire_right
                self.fireball.width,self.fireball.height = 56*2, 19*2
            elif math.atan(delta_x/abs(delta_y)) < -1.3 and -2 < math.atan(delta_x/abs(delta_y)):
                self.fire_textures = self.fire_left
                self.fireball.width,self.fireball.height = 56*2, 19*2

            self.fireball._texture = self.fire_textures[0]

        if self.firebal_animation_frame_counter % 6 == 0:
                self.fireball._texture = self.fire_textures[self.firebal_animation_counter % 8]
                self.firebal_animation_counter += 1

        self.fireball.update()
        self.firebal_animation_frame_counter += 1
        if self.firebal_animation_frame_counter == 150:
            self.firebal_animation_frame_counter = 0
            self.fireball.kill()

        if arcade.check_for_collision(self.fireball, player) or self.player_take_damage < 20:
            self.player_take_damage -= 1
            if self.player_take_damage == 0:
                self.player_take_damage = 20
            if player.face_direction == "right":
                player._texture = player.take_damage_Left_right_up_down[1]
            elif player.face_direction == "left":
                player._texture = player.take_damage_Left_right_up_down[0]
            elif player.face_direction == "up":
                player._texture = player.take_damage_Left_right_up_down[2]
            elif player.face_direction == "down":
                player._texture = player.take_damage_Left_right_up_down[3]
            player.hp -= 2

    def update_animation(self, frame):
        self.update_animation_frame_counter += 1
        if 0 == self.update_animation_frame_counter % frame:
            self.update_animation_counter += 1

            if  self.change_x > 0:
                self.face_direction = "right"
            elif  self.change_x < 0:
                self.face_direction = "left"
            elif  self.change_y > 0:
                self.face_direction = "up"
            elif  self.change_y < 0:
                self.face_direction = "down"


            if self.face_direction == "right":
                self._texture = self.walk_right_textures[self.update_animation_counter % 3]
            elif self.face_direction == "left":
                self._texture = self.walk_left_textures[self.update_animation_counter % 3]
            elif self.face_direction == "up":
                self._texture = self.walk_up_textures[self.update_animation_counter % 3]
            elif self.face_direction == "down":
                self._texture = self.walk_down_textures[self.update_animation_counter % 3]


    def update(self):
        #Færa óvin
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.update_animation(10)
