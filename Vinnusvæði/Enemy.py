import arcade

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

        self.sword_DownRight = arcade.load_textures("Images/Weapon/Sword_DownRight.png",[[94,35,25,20],[158,34,25,20],[221,29,25,20],[285,29,25,20]], scale = 12)
        self.sword_UpLeft = arcade.load_textures("Images/Weapon/Sword_UpLeft.png",[[73,12,26,32],[138,12,26,32],[202,12,26,32],[266,12,26,32]], scale = 12)
        self.sword_UpRight = arcade.load_textures("Images/Weapon/Sword_UpRight.png",[[83,11,35,26],[148,11,35,26],[213,11,35,26],[278,11,35,26]], scale = 14)
        self.sword_DownLeft = arcade.load_textures("Images/Weapon/Sword_DownLeft.png",[[74,34,33,23],[137,34,33,23],[201,34,33,23],[266,34,33,23]], scale = 12)

        self.MOVEMENT_SPEED = 2

        self.SwordSprite = arcade.Sprite()
        self.SwordSprite.width, self.SwordSprite.height = 75, 60
        self.SwordSprite._texture = self.sword_DownRight[0]
        self.update_Sword_animation_counter = 0
        self.update_Sword_animation_frame_counter = 5
        self.sword_gate = 0

        self.hp = 100

    def SwordSwing(self):
        if self.update_Sword_animation_frame_counter == 5:            #update sverðið breytist á hverjum 5ta frame og byrja strax!
            if self.change_x > 0 or self.face_direction == "right":
                self.SwordSprite._texture = self.sword_DownRight[self.update_Sword_animation_counter]
            elif self.change_x < 0 or self.face_direction == "left":
                self.SwordSprite._texture = self.sword_UpLeft[self.update_Sword_animation_counter]
            elif self.change_y > 0 or self.face_direction == "up":
                self.SwordSprite._texture = self.sword_UpRight[self.update_Sword_animation_counter]
            elif self.change_y < 0 or self.face_direction == "down":
                self.SwordSprite._texture = self.sword_DownLeft[self.update_Sword_animation_counter]

            self.update_Sword_animation_counter == 0
            self.update_Sword_animation_frame_counter = 0

        if self.change_x > 0 or self.face_direction == "right": #uppfæra hvar sverðið er
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x + 20, self.center_y - 20
        elif self.change_x < 0 or self.face_direction == "left":
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x - 10, self.center_y
        elif self.change_y > 0 or self.face_direction == "up":
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x, self.center_y
        elif self.change_y < 0 or self.face_direction == "down":
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x - 4, self.center_y - 23

        self.update_Sword_animation_frame_counter += 1
        self.update_Sword_animation_counter += 1

        if self.update_Sword_animation_counter == 3:
            self.update_Sword_animation_counter = 0


    def Attack(self, player):
        distX = player.center_x - self.center_x
        distY = player.center_y - self.center_y
        #færa sig í átt að spilara (Bara lóðrétt og lárétt)
        try:
            if abs(distX) > abs(distY):
                self.center_x += distX/abs(distX) * self.MOVEMENT_SPEED
            else:
                self.center_y += distY/abs(distY) * self.MOVEMENT_SPEED
        except:
            pass

#Vondi kall
        self.walk_right_textures = arcade.load_textures("Images/Character/p3.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
        self.stand_right_textures = arcade.load_textures("Images/Character/p3.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
        self.walk_left_textures = arcade.load_textures("Images/Character/p3.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
        self.stand_left_textures = arcade.load_textures("Images/Character/p3.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
        self.walk_up_textures = arcade.load_textures("Images/Character/p3.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
        self.stand_up_textures = arcade.load_textures("Images/Character/p3.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
        self.walk_down_textures = arcade.load_textures("Images/Character/p3.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)
        self.stand_down_textures = arcade.load_textures("Images/Character/p3.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)
'''
    def update(self):

        # Move the Player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # See if the Player hit the edge of the screen. If so, change direction
        if self.center_x < 0:
            self.center_x = 0

        if self.center_x > SCREEN_WIDTH - 0:
            self.center_x = SCREEN_WIDTH - 0

        if self.center_y < 0:
            self.center_y = 0

        if self.center_y > SCREEN_HEIGHT - 0:
            self.center_y = SCREEN_HEIGHT -0
'''
