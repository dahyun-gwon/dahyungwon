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
        self.state = True
        self.HP=2000
        self.damage=50
        self.time=3
    def draw(self):

        self.image.draw(self.x,self.y)

    def handle_events(self,event):
        pass


    def update(self):
        for o in game_world.objects[2]:
            if type(o) == main_state.Tiena:
                self.x = o.x
                self.y = o.y
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)
        if self.HP<=0:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x - 90, self.y - 90, self.x + 90, self.y + 90


