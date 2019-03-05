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

        self.MOVEMENT_SPEED = 2
        self.hp = 100

#Fall sem ræðst á player
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

#Vondi kall á eftir að skipta út
        #self.walk_right_textures = arcade.load_textures("Images/Character/p3.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
        #self.stand_right_textures = arcade.load_textures("Images/Character/p3.png",[[4,63,25,32],[36,63,25,32],[67,63,25,32]], scale = 3)
        #self.walk_left_textures = arcade.load_textures("Images/Character/p3.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
        #self.stand_left_textures = arcade.load_textures("Images/Character/p3.png",[[4,32,25,32],[36,32,25,32],[67,32,25,32]], scale = 3)
        #self.walk_up_textures = arcade.load_textures("Images/Character/p3.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
        #self.stand_up_textures = arcade.load_textures("Images/Character/p3.png",[[4,96,25,32],[36,96,25,32],[67,96,25,32]], scale = 3)
        #self.walk_down_textures = arcade.load_textures("Images/Character/p3.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)
        #self.stand_down_textures = arcade.load_textures("Images/Character/p3.png",[[4,0,25,32],[36,0,25,32],[67,0,25,32]], scale = 3)
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
