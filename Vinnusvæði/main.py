#Hér koma sóttir pakkar
import arcade
#Hér koma okkar skrár
import Player
from Levels import *

def main():
    window = Level_1(1200, 600, "Highburn Fortress")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
