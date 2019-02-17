import arcade

arcade.Sprite.update_animation_counter = 0
def update_animation(self):
    self.update_animation_counter += 1
    if  self.change_x > 0:
        self._texture = self.walk_right_textures[self.update_animation_counter]    #Breytir um texture í hvert sinn sem fallið er notað

    if self.update_animation_counter == 3:
        self.update_animation_counter = 0


setattr(arcade.Sprite, "update_animation", update_animation)   #Breyta update_animation fallinu fyrir arcade (fallið var gert til þess að verða breytt.)
setattr(arcade.Sprite, "update_animation_counter", 0)


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 6


class Player1:

    Hp = 100
    Gender = 0
    Clothes = [1,2,3,4,5]

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color




        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("Images/Kall.png", 0.2)

        self.player_sprite.center_x = position_x
        self.player_sprite.center_y = position_y


        self.player_sprite.walk_right_textures = arcade.load_textures("Images/Character/Character_Right.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.stand_right_textures = arcade.load_textures("Images/Character/Character_RollRight.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.walk_left_textures = arcade.load_textures("Images/Character/Character_Left.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.stand_left_textures = arcade.load_textures("Images/Character/Character_RollLeft.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.walk_up_textures = arcade.load_textures("Images/Character/Character_Up.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.stand_up_textures = arcade.load_textures("Images/Character/Character_RollUp.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.walk_down_textures = arcade.load_textures("Images/Character/Character_Down.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)
        self.player_sprite.stand_down_textures = arcade.load_textures("Images/Character/Character_RollDown.png",[[8,6,15,20],[40,6,15,20],[72,6,15,20],[104,6,15,20]], scale = 8)

        self.player_sprite.texture_change_distance = 20

        self.player_list.append(self.player_sprite)



    def draw(self):
        arcade.start_render()
        """ Draw the Players with the instance variables we have. """
        #arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        self.player_sprite.draw()


    def update(self):
        #self.player_list.update_animation()

        # Move the Player
        self.position_y += self.player_sprite.change_y
        self.position_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y
        self.player_sprite.center_x += self.player_sprite.change_x


        # See if the Player hit the edge of the screen. If so, change direction
        if self.position_x < 0:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - 0:
            self.position_x = SCREEN_WIDTH - 0

        if self.position_y < 0:
            self.position_y = 0

        if self.position_y > SCREEN_HEIGHT - 0:
            self.position_y = SCREEN_HEIGHT -0
