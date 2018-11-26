from pico2d import *
import game_world

class Fire_e:
    image = None

    def __init__(self, x = 450, y = 300, Xvelocity = 1):
        if Fire_e.image == None:
            Fire_e.image = load_image('e_basic.png')
        self.x, self.y, self.Xvelocity = x, y, Xvelocity
        self.state = True;
        self.damage=70

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity*6
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x - 40, self.y - 30, self.x + 40, self.y + 30