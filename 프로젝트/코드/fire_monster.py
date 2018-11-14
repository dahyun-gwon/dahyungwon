from pico2d import *
import game_world
import  random
import game_framework
from pico2d import *
import game_world


class Fire_Monster:
    image = None

    def __init__(self):
        if Fire_Monster.image == None:
            Fire_Monster.image = load_image('bomp.png')
        self.x=1400
        self.y=random.randint(0,800)

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x -= 8
        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x-15,self.y-25,self.x+15,self.y+25
