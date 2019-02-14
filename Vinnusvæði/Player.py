import arcade

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
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the Players with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the Player
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the Player hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius




def main():
    window = Level1(1200, 600, "Highburn Fortress")
    arcade.run()


if __name__ == "__main__":
    main()
