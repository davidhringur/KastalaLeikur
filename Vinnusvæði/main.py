#Hér koma sóttir pakkar
import arcade
#Hér koma okkar skrár
import Player
from Levels import *
from MainMenu import *

def main():
    mainMenu = MainMenu(1200, 600, "Main Menu")
    arcade.run()

if __name__ == "__main__":
    main()
