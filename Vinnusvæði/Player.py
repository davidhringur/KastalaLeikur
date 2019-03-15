import arcade
from Sword import Sword
from Bow import Bow

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

        if self.update_animation_counter == 2:
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




class Player(arcade.Sprite):

    def __init__(self,MenuOptions,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0,
                 repeat_count_x=1, repeat_count_y=1):
        super(Player, self).__init__(filename=filename, scale=scale,
                 image_x=image_x, image_y=image_y,
                 image_width=image_width, image_height=image_height,
                 repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y,
                 center_x=center_x, center_y=center_y)



        #Leikmaður 1
        if MenuOptions == [[1,0]]:
            self.walk_right_textures = arcade.load_textures("Images/Character/p1.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
            self.walk_left_textures = arcade.load_textures("Images/Character/p1.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
            self.walk_up_textures = arcade.load_textures("Images/Character/p1.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
            self.walk_down_textures = arcade.load_textures("Images/Character/p1.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)
        #Leikmaður 2
        elif MenuOptions == [[0,1]]:
            self.walk_right_textures = arcade.load_textures("Images/Character/p2.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
            self.walk_left_textures = arcade.load_textures("Images/Character/p2.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
            self.walk_up_textures = arcade.load_textures("Images/Character/p2.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
            self.walk_down_textures = arcade.load_textures("Images/Character/p2.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)

        self.Sword = Sword()
        self.Bow = Bow()

        self.MOVEMENT_SPEED = 6
        self.hp = 100

    def update(self):
        #Færa spilara
        self.center_x += self.change_x
        self.center_y += self.change_y

        #drepa leikmann ef líf er undir 0
        if self.hp < 0:
            self.kill()

        #Uppfæra kallinn að labba á hverjum 5-ta frame(fallið búið til að ofan)
        self.update_animation(5)
