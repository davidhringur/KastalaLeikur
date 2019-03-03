import arcade

class Fire(arcade.Sprite):

    def __init__(self,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0,
                 repeat_count_x=1, repeat_count_y=1):
        super(Fire, self).__init__(filename=filename, scale=scale,
                 image_x=image_x, image_y=image_y,
                 image_width=image_width, image_height=image_height,
                 repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y,
                 center_x=center_x, center_y=center_y)

        self.lever_count = 0
        self.fire_textures = arcade.load_textures("Images/ModelPack/DungeonStarter.png",
            [[50,177,12,15],[82,161,12,13],[82,177,12,13],[82,193,12,13],[82,209,12,13]])

        self.update_animation_frame_counter = 0
        self.update_animation_counter = 1


    def update_animation(self, frame):
        if self.lever_count == 4:
            self.update_animation_frame_counter += 1
            if frame == self.update_animation_frame_counter:
                self.update_animation_counter += 1
                self.update_animation_frame_counter = 0

                self._texture = self.fire_textures[self.update_animation_counter]

                if self.update_animation_counter == 4:
                    self.update_animation_counter = 1

    def update(self):
        self.update_animation(6)
