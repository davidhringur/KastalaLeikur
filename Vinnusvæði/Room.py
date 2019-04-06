
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
        self.pillars = None
        self.fire = None
        self.door = None

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
    room.pillars = arcade.SpriteList()
    room.fire = arcade.SpriteList()
    room.door = arcade.SpriteList()

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
            else:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.door.append(wall)


    # Setjum mynd á sprite-ið fyrir boxin/kassana
    #wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
    #wall.left = 7 * SPRITE_SIZE
    #wall.bottom = 5 * SPRITE_SIZE
    #room.wall_list.append(wall)

    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    #Búum til óvini
    room.Enemy1 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=6) #óvinur sem eltir player1
    room.Enemy1.center_x, room.Enemy1.center_y = 1050, 450
    room.enemy_list.append(room.Enemy1)

    #room.Enemy2 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=5) #óvinur sem eltir player1
    #room.Enemy2.center_x, room.Enemy2.center_y = 750, 450
    #room.enemy_list.append(room.Enemy2)

    #room.Enemy3 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=6) #óvinur sem eltir player1
    #room.Enemy3.center_x, room.Enemy3.center_y = 450, 450
    #room.enemy_list.append(room.Enemy3)

    #room.Enemy4 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=8) #óvinur sem eltir player1
    #room.Enemy4.center_x, room.Enemy4.center_y = 250, 450
    #room.enemy_list.append(room.Enemy4)


    # Búum til gimsteinana
    for i in range(int(SCREEN_WIDTH/6), SCREEN_WIDTH, int(SCREEN_WIDTH/6)):
        for j in range(int(SCREEN_HEIGHT/4), SCREEN_HEIGHT , int(SCREEN_HEIGHT/4)):

            # Setjum inn myndina við gimsteinana
            coin = arcade.Sprite("Images/Gem/gems_preview.png", 0.3)

            # Staðsetjum gimsteinana
            coin.center_x = i
            coin.center_y = j

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
    room.pillars = arcade.SpriteList()
    room.door = arcade.SpriteList()


    # Búum til efri og neðri línu af útlínum borðsins

    Shift = SCREEN_WIDTH - SPRITE_SIZE
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loopum fyrir boxin til að fara til hliðar
        for x in range(0 + Shift, SCREEN_WIDTH + Shift, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 13 + Shift and x != SPRITE_SIZE * 14 + Shift and x != SPRITE_SIZE * 15 + Shift) or y == 0:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
            else:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.door.append(wall)


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
    room.Enemy2 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=4) #óvinur sem eltir player1
    room.Enemy2.center_x, room.Enemy2.center_y = Shift + 1050, 450
    room.enemy_list.append(room.Enemy2)

    room.fire = Fire("Images/ModelPack/DungeonStarter.png", 4, image_x=50, image_y=177, image_width=12, image_height=15)
    room.fire.center_x, room.fire.center_y = Shift + SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    room.prop_list.append(room.fire)

    for i in range(4):
        p = Pillar(filename="Images/ModelPack/DungeonStarter.png", pillar_look=i, scale=0.5, image_width=90, image_height=120)
        room.pillars.append(p)
        room.prop_list.append(p)
    room.pillars[0].center_x, room.pillars[0].center_y =  Shift + 77, 510
    room.pillars[1].center_x, room.pillars[1].center_y =  Shift + 1120, 510
    room.pillars[2].center_x, room.pillars[2].center_y =  Shift + 77, 100
    room.pillars[3].center_x, room.pillars[3].center_y =  Shift + 1120, 100

    return room



def setup_room_3(width, height):
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
    room.pillars = arcade.SpriteList()
    room.door = arcade.SpriteList()
    room.fire = arcade.SpriteList()


    # Búum til efri og neðri línu af útlínum borðsins

    Shift = SCREEN_HEIGHT - SPRITE_SIZE
    y = SCREEN_HEIGHT - SPRITE_SIZE + Shift
    # Loopum fyrir boxin til að fara til hliðar
    for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
        wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
        wall.left = x
        wall.bottom = y
        room.wall_list.append(wall)



    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
            # Loopum fyrir boxin að fara upp og niður alveg
        for y in range(SPRITE_SIZE + Shift,SCREEN_HEIGHT - SPRITE_SIZE + Shift,SPRITE_SIZE):
            if (y != Shift + SPRITE_SIZE * 5 and y != Shift + SPRITE_SIZE * 6) or x == SCREEN_WIDTH - SPRITE_SIZE:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
            else:
                wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
                wall.left = x
                wall.bottom = y
                room.door.append(wall)

    # Setjum mynd á sprite-ið fyrir boxin/kassana
    #wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=34)
    #wall.left = 7 * SPRITE_SIZE
    #wall.bottom = 5 * SPRITE_SIZE
    #room.wall_list.append(wall)

    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")

    #Búum til óvini
    room.Enemy1 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=5) #óvinur sem eltir player1
    room.Enemy1.center_x, room.Enemy1.center_y = 100, 450 + Shift
    room.Enemy1.enemyIsArcher = 1
    room.enemy_list.append(room.Enemy1)

    #Búum til óvini
    room.Enemy2 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=5) #óvinur sem eltir player1
    room.Enemy2.center_x, room.Enemy2.center_y = 500, 2*Shift -50
    room.Enemy2.enemyIsArcher, room.Enemy2.isTop = 1, 1
    room.enemy_list.append(room.Enemy2)

    room.Enemy3 = Enemy("Images/Enemy/Dungeon_Character.png", image_x=17, image_y=17, image_width=12, image_height=13, scale=5) #óvinur sem eltir player1
    room.Enemy3.center_x, room.Enemy3.center_y = 900, 450 + Shift
    room.enemy_list.append(room.Enemy3)

    return room


def setup_room_4(width, height):
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
    room.pillars = arcade.SpriteList()
    room.door = arcade.SpriteList()
    room.fire = arcade.SpriteList()


    # Búum til efri og neðri línu af útlínum borðsins

    Shift = SCREEN_WIDTH - SPRITE_SIZE
    # Loopum fyrir boxin til að fara til hliðar
    y = SCREEN_HEIGHT - SPRITE_SIZE
    for x in range(-Shift, SCREEN_WIDTH- Shift, SPRITE_SIZE):
        wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
        wall.left = x
        wall.bottom = y
        room.wall_list.append(wall)



            # Loopum fyrir boxin að fara upp og niður alveg
    x = -SCREEN_WIDTH + SPRITE_SIZE
    for y in range(SPRITE_SIZE,SCREEN_HEIGHT - SPRITE_SIZE ,SPRITE_SIZE):
        wall = arcade.Sprite("Images/ModelPack/Dungeon_Tileset.png", SPRITE_SCALING, image_x=0, image_y=47, image_width=32, image_height=32)
        wall.left = x
        wall.bottom = y
        room.wall_list.append(wall)



    # Bakgrunnsmynd
    room.background = arcade.load_texture("Images/ModelPack/MakingMap1.png")


    return room
