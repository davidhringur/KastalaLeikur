import arcade

def update_animation(self, frame):
    self.update_animation_frame_counter += 1
    if frame == self.update_animation_frame_counter:
        self.update_animation_counter += 1
        self.update_animation_frame_counter = 0

        if  self.change_x > 0:
            self._texture = self.walk_right_textures[self.update_animation_counter]
            self.face_direction = "right"
        elif  self.change_x < 0:
            self._texture = self.walk_left_textures[self.update_animation_counter]
            self.face_direction = "left"
        elif  self.change_y > 0:
            self._texture = self.walk_up_textures[self.update_animation_counter]
            self.face_direction = "up"
        elif  self.change_y < 0:
            self._texture = self.walk_down_textures[self.update_animation_counter]
            self.face_direction = "down"

        if self.update_animation_counter == 3:
            self.update_animation_counter = 0

    if  self.change_x == 0 and self.change_y == 0:
        if self.face_direction == "right":
            self._texture = self.walk_right_textures[0]
        if self.face_direction == "left":
            self._texture = self.walk_left_textures[0]
        if self.face_direction == "up":
            self._texture = self.walk_up_textures[0]
        if self.face_direction == "down":
            self._texture = self.walk_down_textures[0]


setattr(arcade.Sprite, "update_animation", update_animation)   #Breyta update_animation fallinu fyrir arcade.Sprite (fallið var gert til þess að verða breytt.)
setattr(arcade.Sprite, "update_animation_counter", 0)
setattr(arcade.Sprite, "face_direction", "right")
setattr(arcade.Sprite, "update_animation_frame_counter", 0)


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 6


class Player(arcade.Sprite):

    Hp = 100
    Gender = 0
    Clothes = [1,2,3,4,5]

    def PlayerSetup(self):

        self.walk_right_textures = arcade.load_textures("Images/Character/Character_Right.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.stand_right_textures = arcade.load_textures("Images/Character/Character_RollRight.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.walk_left_textures = arcade.load_textures("Images/Character/Character_Left.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.stand_left_textures = arcade.load_textures("Images/Character/Character_RollLeft.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.walk_up_textures = arcade.load_textures("Images/Character/Character_Up.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.stand_up_textures = arcade.load_textures("Images/Character/Character_RollUp.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.walk_down_textures = arcade.load_textures("Images/Character/Character_Down.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.stand_down_textures = arcade.load_textures("Images/Character/Character_RollDown.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)

        self.sword_DownRight = arcade.load_textures("Images/Weapon/Sword_DownRight.png",[[94,35,25,20],[158,34,25,20],[221,29,25,20],[285,29,25,20]], scale = 12)
        self.sword_UpLeft = arcade.load_textures("Images/Weapon/Sword_UpLeft.png",[[73,12,26,32],[138,12,26,32],[202,12,26,32],[266,12,26,32]], scale = 12)
        self.sword_UpRight = arcade.load_textures("Images/Weapon/Sword_UpRight.png",[[83,11,35,26],[148,11,35,26],[213,11,35,26],[278,11,35,26]], scale = 12)

        self.SwordSprite = arcade.Sprite()
        self.SwordSprite.width, self.SwordSprite.height = 75, 60
        self.SwordSprite._texture = self.sword_DownRight[0]
        self.update_Sword_animation_counter = 0
        self.update_Sword_animation_frame_counter = 5
        self.sword_gate = 0

    def SwordSwing(self):
        if self.update_Sword_animation_frame_counter == 5:            #update sverðið breytist á hverjum 5ta frame og byrja strax!
            if self.change_x > 0 or self.face_direction == "right":
                self.SwordSprite._texture = self.sword_DownRight[self.update_Sword_animation_counter]
            elif self.change_x < 0 or self.face_direction == "left":
                self.SwordSprite._texture = self.sword_UpLeft[self.update_Sword_animation_counter]
            elif self.change_y < 0 or self.face_direction == "up":
                self.SwordSprite._texture = self.sword_UpRight[self.update_Sword_animation_counter]

            self.update_Sword_animation_counter == 0
            self.update_Sword_animation_frame_counter = 0

        if self.change_x > 0 or self.face_direction == "right": #uppfæra hvar sverðið er
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x + 20, self.center_y - 20
        elif self.change_x < 0 or self.face_direction == "left":
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x - 10, self.center_y
        elif self.change_y < 0 or self.face_direction == "up":
            self.SwordSprite.center_x, self.SwordSprite.center_y = self.center_x, self.center_y

        self.update_Sword_animation_frame_counter += 1
        self.update_Sword_animation_counter += 1

        if self.update_Sword_animation_counter == 3:
            self.update_Sword_animation_counter = 0


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
