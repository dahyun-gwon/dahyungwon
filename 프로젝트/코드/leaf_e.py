from pico2d import *
import game_world
import game_framework

class Leaf_e:
    image = None

    def __init__(self, x = 400, y = 300):
        if Leaf_e.image == None:
            Leaf_e.image = load_image('leaf_e.png')
        self.x, self.y= x, y
        self.frame=0
        self.cnt=0
        self.time=6

    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.x,self.y)



    def update(self):
        if (self.cnt == 3):
            self.cnt = 0
            self.frame += 1
        self.frame = self.frame % 10
        self.time-=game_framework.frame_time
        self.cnt+=1
        if self.time<0:
            game_world.remove_object(self)

