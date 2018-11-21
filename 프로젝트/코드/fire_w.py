from pico2d import *
import game_world

class Fire_w:
    image = None

    def __init__(self, x ,y , Xvelocity = 1):
        if Fire_w.image == None:
            Fire_w.image = load_image('fire_w.png')
        self.x, self.y, self.Xvelocity = x, y, Xvelocity
        self.damage=100
        self.state = True;

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.Xvelocity*12
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x - 180, self.y - 90, self.x + 200, self.y + 90



