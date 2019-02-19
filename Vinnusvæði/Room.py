
import arcade
import os

SPRITE_SCALING = 1.3
SPRITE_NATIVE_SIZE = 30
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

#SCREEN_WIDTH = SPRITE_SIZE * 14
#SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Level 1"

MOVEMENT_SPEED = 5


class Room:
# Þessi klasi inniheldur allar upplýsingar um herbergin/levelin
    def __init__(self):

        # Aðrir listar fyrir t.d. gimsteina eru í levels file
        self.wall_list_horizontal = None
        self.wall_list_vertical = None

        # Bakgrunnsmynd
        self.background = None


def setup_room_1():
# Mögulega munum við færa room1 inn í aðra möppu ef þetta verður mikið
    room = Room()
    # Sprite listi
    room.wall_list_horizontal = arcade.SpriteList()
    room.wall_list_vertical = arcade.SpriteList()

    # Búum til efri og neðri línu af útlínum borðsins
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loopum fyrir boxin til að fara til hliðar
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
            wall.left = x
            wall.bottom = y
            room.wall_list_horizontal.append(wall)

    # Búum til hægri og vinstri línuna af borðinu
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loopum fyrir boxin að fara upp og niður alveg
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Viljum skilja eftir autt pláss svo hægt sé að
            # "labba" yfir í næsta borð
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
                wall.left = x
                wall.bottom = y
                room.wall_list_vertical.append(wall)

    # Setjum mynd á sprite-ið fyrir boxin/kassana
    #wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
    #wall.left = 7 * SPRITE_SIZE
    #wall.bottom = 5 * SPRITE_SIZE
    #room.wall_list.append(wall)

    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    return room
