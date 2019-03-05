
import arcade
import os
import random
from Enemy import *
from Fire import *
from Pillar import *


class Room:
# Þessi klasi inniheldur allar upplýsingar um herbergin/levelin
    def __init__(self):

        # Aðrir listar fyrir t.d. gimsteina eru í levels file
        self.wall_list = None
        self.enemy_list = None
        self.coin_list = None
        self.prop_list = None

        # Bakgrunnsmynd
        self.background = None


def setup_room_1(width, height):
# Mögulega munum við færa room1 inn í aðra möppu ef þetta verður mikið
    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height
    SPRITE_SIZE = int(1200/30) #ATH 30 Verður að ganga upp í 1200 svo þetta passar!
    SPRITE_NATIVE_SIZE = 32
    SPRITE_SCALING = SPRITE_SIZE/SPRITE_NATIVE_SIZE

    room = Room()
    # Sprite listi
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.prop_list = arcade.SpriteList()

    # Búum til efri og neðri línu af útlínum borðsins
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loopum fyrir boxin til að fara til hliðar
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Búum til hægri og vinstri línuna af borðinu
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loopum fyrir boxin að fara upp og niður alveg
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Viljum skilja eftir autt pláss svo hægt sé að
            # "labba" yfir í næsta borð
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Setjum mynd á sprite-ið fyrir boxin/kassana
    #wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
    #wall.left = 7 * SPRITE_SIZE
    #wall.bottom = 5 * SPRITE_SIZE
    #room.wall_list.append(wall)

    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    #Búum til óvini
    room.Enemy1 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=8) #óvinur sem eltir player1
    room.Enemy1.center_x, room.Enemy1.center_y = 1050, 450
    room.enemy_list.append(room.Enemy1)


    # Búum til gimsteinana
    for i in range(15):

        # Setjum inn myndina við gimsteinana
        coin = arcade.Sprite("Images/Gem/gems_preview.png", 0.3)

        # Staðsetjum gimsteinana
        coin.center_x = 52 + random.randrange(SCREEN_WIDTH - 74)
        coin.center_y = 52 + random.randrange(SCREEN_HEIGHT - 74)

        # Bætum við gimsteinum við listann
        room.coin_list.append(coin)

    return room









def setup_room_2(width, height):
# Mögulega munum við færa room1 inn í aðra möppu ef þetta verður mikið
    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height
    SPRITE_SIZE = int(1200/30) #ATH 30 Verður að ganga upp í 1200 svo þetta passar!
    SPRITE_NATIVE_SIZE = 32
    SPRITE_SCALING = SPRITE_SIZE/SPRITE_NATIVE_SIZE

    room = Room()
    # Sprite listi
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.prop_list = arcade.SpriteList()

    # Búum til efri og neðri línu af útlínum borðsins

    Shift = SCREEN_WIDTH - int(1.5*SPRITE_SIZE)
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loopum fyrir boxin til að fara til hliðar
        for x in range(0 + Shift, SCREEN_WIDTH + Shift, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 13 + Shift and x != SPRITE_SIZE * 14 + Shift and x != SPRITE_SIZE * 15 + Shift) or y == 0:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Búum til vinstri línuna af borðinu
    x = (Shift + SCREEN_WIDTH - SPRITE_SIZE)
        # Loopum fyrir boxin að fara upp og niður alveg
    for y in range(SPRITE_SIZE,SCREEN_HEIGHT - SPRITE_SIZE,SPRITE_SIZE):
        # Viljum skilja eftir autt pláss svo hægt sé að
        # "labba" yfir í næsta borð

        wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
        wall.left = x
        wall.bottom = y
        room.wall_list.append(wall)

    # Setjum mynd á sprite-ið fyrir boxin/kassana
    #wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
    #wall.left = 7 * SPRITE_SIZE
    #wall.bottom = 5 * SPRITE_SIZE
    #room.wall_list.append(wall)

    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    #Búum til óvini
    room.Enemy2 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=8) #óvinur sem eltir player1
    room.Enemy2.center_x, room.Enemy2.center_y = Shift + 1050, 450
    room.enemy_list.append(room.Enemy2)

    room.fire = Fire("Images/ModelPack/DungeonStarter.png", 4, image_x=50, image_y=177, image_width=12, image_height=15)
    room.fire.center_x, room.fire.center_y = Shift + SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    room.prop_list.append(room.fire)

    return room
