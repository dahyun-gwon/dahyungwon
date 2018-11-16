from pico2d import *
import game_world

class Leaf_basic_attack:
    image = None

    def __init__(self, x = 400, y = 300, Xvelocity = 1):
        if Leaf_basic_attack.image == None:
            Leaf_basic_attack.image = load_image('leaf_basic_attack.png')
        self.x, self.y,self.up_y,self.down_y, self.Xvelocity = x, y,y+10,y-10, Xvelocity

    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.x += self.Xvelocity*4

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x-50,self.y-50,self.x+50,self.y+50