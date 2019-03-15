import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)



class HP_meter:
    def __init__(self):
        self.tx = arcade.load_textures("Images/Gem/heart_animated_1.png",[[68,0,17,16],[51,0,17,16],[34,0,17,16],[17,0,17,16],[0,0,17,16]], scale = 12)
        self.bars = arcade.SpriteList()
        x = 100
        for _ in range(5):
            self.bars.append(arcade.Sprite("Images/Gem/heart_animated_1.png", center_x=x, center_y=20, scale=2, image_x=0, image_y=0, image_width=17, image_height=16))
            x += 17*2

    def update(self, player1):
        for l, bar in zip((0,20,40,60,80), self.bars):
            life_index = min(4,int((max(0,player1.hp-l))/5))
            bar._texture = self.tx[life_index]
