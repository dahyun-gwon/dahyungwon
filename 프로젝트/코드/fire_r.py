from pico2d import *
import game_world

class Fire_r:
    image = None

    def __init__(self, x = 400, y = 300, Xvelocity = 1):
        if Fire_r.image == None:
            Fire_r.image = load_image('fire_r.png')
        self.x, self.y, self.Xvelocity = x, y, Xvelocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.Xvelocity*8


        if self.x < 0 or self.x > 1800:
            game_world.remove_object(self)
