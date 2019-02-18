
import arcade
import os

SPRITE_SCALING = 1.3
SPRITE_NATIVE_SIZE = 30
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

#SCREEN_WIDTH = SPRITE_SIZE * 14
#SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Rooms Example"

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    # Skilgreina myndina úr pakkanum
    #arcade.draw_commands.get_image(x=0, y=47, width=32, height=34)
    #image = arcade.get_image()
    #image.save('Images/ModelPack/Dungeon_Tileset.png', 'PNG')
    # Setjum nú upp veggina
    # Búum til efri og neðri línu af útlínum borðsins
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=34, image_height=34)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Búum til hægri og vinstri línuna af borðinu
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=34, image_height=34)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=34, image_height=34)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    return room
