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

        self.hit_frames = 10
        self.hit_frames_counter, self.hit_gate = self.hit_frames, [0,0,0,0] #Hit_gate: left, right, up, down

    #Fall sem ræðst á player
    def Attack(self, player):
        distX = player.center_x - self.center_x
        distY = player.center_y - self.center_y
        sign = lambda x: (1, -1)[x < 0]
        safezoneAdj = 50
        #færa sig í átt að spilara (Bara lóðrétt og lárétt)
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
                    if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                        player.center_x -= 10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
            elif self.change_x > 0 or self.hit_gate == [0,1,0,0]:   #ýtir leikmanni til hægri ef óvinur klessir á hann
                self.hit_gate = [0,1,0,0]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                        player.center_x -= -10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
            elif self.change_y > 0 or self.hit_gate == [0,0,1,0]:   #ýtir leikmanni upp ef óvinur klessir á hann
                self.hit_gate = [0,0,1,0]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                        player.center_y -= -10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
            elif self.change_y < 0 or self.hit_gate == [0,0,0,1]:   #ýtir leikmanni niður ef óvinur klessir á hann
                self.hit_gate = [0,0,0,1]
                if self.hit_frames_counter > 0:
                    self.hit_frames_counter -= 1
                    if player.bottom > safezoneAdj and player.top < SCREEN_HEIGHT-safezoneAdj and player.left > safezoneAdj and player.right < SCREEN_WIDTH-safezoneAdj:
                        player.center_y -= 10
                else:
                    self.hit_gate = [0,0,0,0]
                    self.hit_frames_counter = self.hit_frames
            else:
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
