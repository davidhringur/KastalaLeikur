#Hér koma sóttir pakkar
import arcade
#Hér koma okkar skrár
import Player
from Levels import *
from MainMenu import *

def main():
    window = Levels(1200, 600, "Highburn Fortress", [[1,0]])
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
