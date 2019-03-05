#Hér koma sóttir pakkar
import arcade
#Hér koma okkar skrár
import Player
from Levels import *
from MainMenu import *

def main():
    mainMenu = MainMenu(1200, 600, "Main Menu")
    arcade.run()
    arcade.window_commands.pause(1)
    window = Levels(1200, 600, "Highburn Fortress", mainMenu.options)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
