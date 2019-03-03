import arcade

class Sword:
    def __init__(self):
        self.sword_DownRight = arcade.load_textures("Images/Weapon/Sword_DownRight.png",[[94,35,25,20],[158,34,25,20],[221,29,25,20],[285,29,25,20]], scale = 12)
        self.sword_UpLeft = arcade.load_textures("Images/Weapon/Sword_UpLeft.png",[[73,12,26,32],[138,12,26,32],[202,12,26,32],[266,12,26,32]], scale = 12)
        self.sword_UpRight = arcade.load_textures("Images/Weapon/Sword_UpRight.png",[[83,11,35,26],[148,11,35,26],[213,11,35,26],[278,11,35,26]], scale = 14)
        self.sword_DownLeft = arcade.load_textures("Images/Weapon/Sword_DownLeft.png",[[74,34,33,23],[137,34,33,23],[201,34,33,23],[266,34,33,23]], scale = 12)

        self.SwordSprite = arcade.Sprite()
        self.SwordSprite.width, self.SwordSprite.height = 75, 60
        self.SwordSprite._texture = self.sword_DownRight[0]
        self.update_Sword_animation_counter = 0
        self.update_Sword_animation_frame_counter = 5
        self.sword_gate = 0

    def SwordSwing(self,center_x, center_y, change_x, change_y, face_direction):
        if self.update_Sword_animation_frame_counter == 5:            #update sverðið breytist á hverjum 5ta frame og byrja strax!
            if change_x > 0 or face_direction == "right":
                self.SwordSprite._texture = self.sword_DownRight[self.update_Sword_animation_counter]
            elif change_x < 0 or face_direction == "left":
                self.SwordSprite._texture = self.sword_UpLeft[self.update_Sword_animation_counter]
            elif change_y > 0 or face_direction == "up":
                self.SwordSprite._texture = self.sword_UpRight[self.update_Sword_animation_counter]
            elif change_y < 0 or face_direction == "down":
                self.SwordSprite._texture = self.sword_DownLeft[self.update_Sword_animation_counter]

            self.update_Sword_animation_counter == 0
            self.update_Sword_animation_frame_counter = 0

        if change_x > 0 or face_direction == "right": #uppfæra hvar sverðið er
            self.SwordSprite.center_x, self.SwordSprite.center_y = center_x + 20, center_y - 20
        elif change_x < 0 or face_direction == "left":
            self.SwordSprite.center_x, self.SwordSprite.center_y = center_x - 10, center_y
        elif change_y > 0 or face_direction == "up":
            self.SwordSprite.center_x, self.SwordSprite.center_y = center_x, center_y
        elif change_y < 0 or face_direction == "down":
            self.SwordSprite.center_x, self.SwordSprite.center_y = center_x - 4, center_y - 23

        self.update_Sword_animation_frame_counter += 1
        self.update_Sword_animation_counter += 1

        if self.update_Sword_animation_counter == 3:
            self.update_Sword_animation_counter = 0

    def hit_enemy(self, enemy_sprite_list):
        hit_list = arcade.check_for_collision_with_list(self.SwordSprite, enemy_sprite_list)
        if hit_list:
            for enemy in hit_list:
                enemy.hp -= 5
                enemy._set_color=(124, 10, 2)
                if enemy.hp <= 0:
                    enemy.kill()
