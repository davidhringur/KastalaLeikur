import arcade

class Pillar(arcade.Sprite):

    def __init__(self, pillar_look = 0,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0,
                 repeat_count_x=1, repeat_count_y=1):
        super(Pillar, self).__init__(filename=filename, scale=scale,
                 image_x=image_x, image_y=image_y,
                 image_width=image_width, image_height=image_height,
                 repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y,
                 center_x=center_x, center_y=center_y)

        self.pillar_look = pillar_look
        self.pillar_textures = arcade.load_textures("Images/ModelPack/Dungeon_Tileset.png",
            [[254,6,20,33],[302,6,20,33],[350,6,20,33],[398,6,20,33]])
        self.pillar_broken_textures = arcade.load_textures("Images/ModelPack/Dungeon_Tileset.png",
            [[254,55,20,33],[302,55,20,33],[350,55,20,33],[398,55,20,33]])

        self._texture = self.pillar_textures[pillar_look]
        self.stop = 0

    def updateFire(self, sword_sprite, fire_activate):
        if arcade.check_for_collision(self, sword_sprite) and self.stop == 0:
            self._texture = self.pillar_broken_textures[self.pillar_look]
            fire_activate.lever_count += 1
            self.stop = 1
