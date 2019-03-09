from arcade.geometry import check_for_collision_with_list
from arcade.geometry import check_for_collision
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList

sign = lambda x: (1, -1)[x < 0]

def boxCollision(sprite_a, sprite_b, stop_change_x, stop_change_y):
    xa_min, xa_max, ya_min, ya_max = sprite_a.left, sprite_a.right, sprite_a.bottom, sprite_a.top
    x0a_min, x0a_max, y0a_min, y0a_max = sprite_a.left-sprite_a.change_x, sprite_a.right-sprite_a.change_x, sprite_a.bottom-sprite_a.change_y, sprite_a.top-sprite_a.change_y
    xb_min, xb_max, yb_min, yb_max = sprite_b.left, sprite_b.right, sprite_b.bottom, sprite_b.top
    x0b_min, x0b_max, y0b_min, y0b_max = sprite_b.left-sprite_b.change_x, sprite_b.right-sprite_b.change_x, sprite_b.bottom-sprite_b.change_y, sprite_b.top-sprite_b.change_y

    horn = 0

    if y0a_min < y0b_max and y0a_max > y0b_min and not stop_change_x:
        pushback = min(abs(xa_min-xb_max),abs(xa_max-xb_min))*sign(sprite_a.change_x)
        sprite_a.center_x -= pushback
        sprite_b.center_x -= 0
        stop_change_x = 1
        horn += 1
    if x0a_min < x0b_max and x0a_max > x0b_min and not stop_change_y:
        pushback = min(abs(ya_min-yb_max),abs(ya_max-yb_min))*sign(sprite_a.change_y)
        sprite_a.center_y -= pushback
        sprite_b.center_y -= 0
        stop_change_y = 1
        horn += 1
    if horn == 2:
        sprite_a.center_x += sprite_a.change_x
        sprite_b.center_x += sprite_b.change_x
        sprite_a.center_y -= sprite_a.change_y
        sprite_b.center_y -= sprite_b.change_y


class PhysicsEngineHighburn:

    def __init__(self, player_sprite: Sprite, walls: SpriteList):
        assert(isinstance(player_sprite, Sprite))
        assert(isinstance(walls, SpriteList))
        self.player_sprite = player_sprite
        self.walls = walls

    def update(self):
        #Athuga hvort veggur rekst á spilara
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        if len(hit_list) > 0:
            stop_change_x, stop_change_x = 0, 0
            for hit in hit_list:
                boxCollision(self.player_sprite, hit, stop_change_x, stop_change_x)
