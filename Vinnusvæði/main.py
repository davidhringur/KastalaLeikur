#Hér koma sóttir pakkar
import arcade
#Hér koma okkar skrár
import Player
from Levels import *
from MainMenu import *

def main():
<<<<<<< HEAD
    window = Levels(1200, 600, "Highburn Fortress")
=======
    window = MainMenu(1200, 600, "Main Menu")
    arcade.run()
    window = Level_1(1200, 600, "Highburn Fortress")
>>>>>>> f95ec85fdc1d49af1b63704b5d5965a76bcbba1f
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
