from pico2d import *
import game_world
import game_framework
import main_state

class Water_r:
    image = None

    def __init__(self, x = 400, y = 300):
        if Water_r.image == None:
            Water_r.image = load_image('water_r.png')
        self.x, self.y = x, y
        self.time=4
        self.state=True
        self.damage=10

    def draw(self):
        self.image.clip_draw(0,0,1200,230,self.x,self.y)

    def update(self):
        for o in game_world.objects[2]:
            if type(o) == main_state.Tiena:
                self.x = o.x+650
                self.y = o.y
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)
        if main_state.tiena_HP<1:
            game_world.remove_object(self)
    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x - 600, self.y - 115, self.x + 600, self.y + 115