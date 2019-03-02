from arcade.geometry import check_for_collision_with_list
from arcade.geometry import check_for_collision
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList

class PhysicsEngineHighburn:

    def __init__(self, player_sprite: Sprite, walls: SpriteList):
        assert(isinstance(player_sprite, Sprite))
        assert(isinstance(walls, SpriteList))
        self.player_sprite = player_sprite
        self.walls = walls

    def update(self):
        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        if len(hit_list) > 0:
            corner_test = 0
            #Athuga hvort það er rekist á uppi
            self.player_sprite.center_y -= 2
            hit_list = check_for_collision_with_list(self.player_sprite, self.walls) #Það er fært kallinn 2 pixla niður og ef hann rekst ekki á í þetta skipti
            self.player_sprite.center_y += 2                            #þá vitum við að hann sé niðri (kallinn er box og við viljum vitha hvaða hlið klesir á)
            if len(hit_list) > 0:
                self.player_sprite.center_y -= self.player_sprite.change_y
                corner_test +=1

            #Athuga hvort það er rekist á niðri
            self.player_sprite.center_y += 2
            hit_list = check_for_collision_with_list(self.player_sprite, self.walls)
            self.player_sprite.center_y -= 2
            if len(hit_list) > 0:
                self.player_sprite.center_y += self.player_sprite.change_y
                corner_test +=1

            #Athuga hvort það er rekist á hægri
            self.player_sprite.center_x += 2
            hit_list = check_for_collision_with_list(self.player_sprite, self.walls)
            self.player_sprite.center_x -= 2
            if len(hit_list) > 0:
                self.player_sprite.center_x -= self.player_sprite.change_x
                corner_test +=1

            #Athuga hvort það er rekist á vinstri
            self.player_sprite.center_x -= 2
            hit_list = check_for_collision_with_list(self.player_sprite, self.walls)
            self.player_sprite.center_x += 2
            if len(hit_list) > 0:
                self.player_sprite.center_x -= self.player_sprite.change_x
                corner_test +=1

            #Ef corner_test er 4 þá var prófað allar áttir og kallinn rakst sammt á svo hann er í horni.
            if corner_test == 4:
                self.player_sprite.center_y -= 2
                self.player_sprite.center_x += 2
                # Check for wall hit
                hit_list = check_for_collision_with_list(self.player_sprite, self.walls)
                self.player_sprite.center_y += 2
                self.player_sprite.center_x -= 2
                if len(hit_list) > 0:
                    self.player_sprite.center_x += self.player_sprite.change_x  #Það vill svo til að sama hvað horni við erum í
                    self.player_sprite.center_y -= self.player_sprite.change_y  #þá förum við út úr því með þessum breytingum.
