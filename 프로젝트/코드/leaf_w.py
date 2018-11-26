from pico2d import *
import game_world
import game_framework
import main_state


class Leaf_w:
    image = None


    def __init__(self,x ,y):
        if Leaf_w.image == None:
            Leaf_w.image = load_image('leaf_w.png')
        self.x, self.y= x, y
        self.Xvelocity=0
        self.Yvelocity=0
        self.state = True;
        self.HP=50
        self.damage=50
        self.time=3
    def draw(self):

        self.image.draw(self.x,self.y)

    def handle_event(self,event):
        pass


    def update(self):
        self.x,self.y = main_state.tienaa.XY()
        self.x+=self.Xvelocity
        self.y+=self.Yvelocity
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x - 90, self.y - 90, self.x + 90, self.y + 90


