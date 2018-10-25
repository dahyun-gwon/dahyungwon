from tiena import tiena
from pico2d import *
import game_world
class Fire_Wisp:
    def __init__(self):
        self.image = load_image('fire_wisp.png')
        self.x = tiena.returnX()-30
        self.y = tiena.returnY()+50
    def hanlde_events(self):
        pass
    def update(self):
        self.x=tiena.returnX()-30
        self.y=tiena.returnY()+50
    def draw(self):
        self.image.draw(self.x, self.y)


class fire_basic_attack:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if fire_basic_attack.image == None:
            fire_basic_attack.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
