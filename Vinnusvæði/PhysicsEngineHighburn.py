from arcade.geometry import check_for_collision_with_list
from arcade.geometry import check_for_collision
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList

class PhysicsEngineHighburn:
    """
    This class will move everything, and take care of collisions.
    """

    def __init__(self, player_sprite: Sprite, walls: SpriteList):
        """
        Constructor.
        """
        assert(isinstance(player_sprite, Sprite))
        assert(isinstance(walls, SpriteList))
        self.player_sprite = player_sprite
        self.walls = walls

    last_contact_x = None
    last_contact_y = None


    def update(self):
        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        # If we hit a wall, move so the edges are at the same point

        if len(hit_list) > 0:
            if self.player_sprite.change_x > 0:
                for item in hit_list:
                    if item.left <= self.player_sprite.right and self.last_contact_y != item.get_position:
                        self.player_sprite.center_x -= self.player_sprite.change_x
                        self.last_contact_x = item.get_position
                        print(self.last_contact_y)
                        break
                        #self.player_sprite.right = min(item.left,
                        #                               self.player_sprite.right)
            elif self.player_sprite.change_x < 0:
                for item in hit_list:
                    if item.right >= self.player_sprite.left and self.last_contact_y != item.get_position:
                        self.player_sprite.center_x -= self.player_sprite.change_x
                        self.last_contact_x = item.get_position
                        break
                    #self.player_sprite.left = max(item.right,
                    #                              self.player_sprite.left)

        # If we hit a wall, move so the edges are at the same point
            if self.player_sprite.change_y > 0:
                for item in hit_list:
                    if item.bottom <= self.player_sprite.top and self.last_contact_x != item.get_position:
                        print("hi")
                        self.player_sprite.center_y -= self.player_sprite.change_y
                        self.last_contact_y = item.get_position
                        break
                    #self.player_sprite.top = min(item.bottom,
                    #                             self.player_sprite.top)
            elif self.player_sprite.change_y < 0:
                for item in hit_list:
                    if item.top >= self.player_sprite.bottom and self.last_contact_x != item.get_position:
                        self.player_sprite.center_y -= self.player_sprite.change_y
                        self.last_contact_y = item.get_position
                        break
                    #self.player_sprite.bottom = max(item.top,
                    #                                self.player_sprite.bottom)
            else:
                print("Error, collision while player wasn't moving.")
