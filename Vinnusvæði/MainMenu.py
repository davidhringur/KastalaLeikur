import arcade
import Player
from pick import pick

class MainMenu(arcade.Window):

    #def __init__(self, width, height, title):

    #    file_path = os.path.dirname(os.path.abspath(__file__))
    #    os.chdir(file_path)

        # Notum smið yfirklasanns
        #super().__init__(width, height, title)

        #self.SCREEN_WIDTH = width
        #self.SCREEN_HEIGHT = height

        # Viljum að músin hverfi þegar hún er staðsett yfir glugganum
        #self.set_mouse_visible(False)

        title = 'Choose a player'
        options = ['p1', 'p2', 'p3', 'p4']
        option, index = pick(options, title)
        print(option)

        #self.LEFT_RIGHT_UP_DOWN_key_is_down = [0,0,0,0]
