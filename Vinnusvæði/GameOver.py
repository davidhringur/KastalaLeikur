import arcade


class EndGame(arcade.Window):
    def __init__(self, width, height):
        self.Congrats = arcade.Sprite("Images/Main/Congratulations.png", center_x=width // 2, center_y=height // 4 * 3)
        self.gameOver = arcade.Sprite("Images/GameOver/GameOver.png", center_x=width // 2, center_y=height // 4 * 3)
        self.PlayAgain = arcade.Sprite("Images/Main/Play-again.png", center_x=width // 2, center_y=height // 4 * 2)
        self.quit = arcade.Sprite("Images/Main/Quit.png", center_x=width // 2, center_y=height // 4)

        self.options = 0
        self.i = 0

    def update(self, player):
        if player.hp <= 0:
            self.gameOver.draw()
        else:
            self.Congrats.draw()
        #print("Hi")
        if self.options == 0:
            self.i += 1
            if self.i < 20:
                self.PlayAgain.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.PlayAgain.draw()

        if self.options == 1:
            self.i += 1
            if self.i < 20:
                self.quit.draw()
            elif self.i == 40:
                self.i = 0
        else:
            self.quit.draw()
    def newGame(self):
        from MainMenu import MainMenu
        window = MainMenu(1200, 600, "Main Menu")



    def on_key_press(self, key, modifiers):
        # Kallað er á þetta í hvert sinn sem notandi ýtir á takka
        if key == arcade.key.LEFT:
            pass
        elif key == arcade.key.RIGHT:
            pass
        elif key == arcade.key.UP:
            self.options += 1
        elif key == arcade.key.DOWN:
            self.options -= 1
        elif key == arcade.key.ENTER:
            pass
