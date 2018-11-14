from pico2d import *
import game_world
import game_framework
from tiena import Tiena
class Leaf_w:
    image = None

    def __init__(self,x ,y):
        if Leaf_w.image == None:
            Leaf_w.image = load_image('leaf_w.png')
        self.x, self.y= x, y
        self.time=3

    def draw(self):

        self.image.draw(self.x,self.y)



    def update(self):
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)

