from pico2d import *
import game_world
import game_framework
import main_state

class Water_w:
    image = None

    def __init__(self, x = 400, y = 300):
        if Water_w.image == None:
            Water_w.image = load_image('water_e.png')
        self.x, self.y = x+100, y
        self.time=3
        self.state=True
        self.damage=0
        self.frame=0
        self.cnt=0

    def draw(self):
        self.image.clip_draw(self.frame*300,0,300,300,self.x,self.y)
    def handle_events(self,event):
        pass
    def update(self):
        self.cnt+=1
        if(self.cnt==5):
            self.cnt=0
            self.frame+=1
        self.frame=self.frame%14
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)
    def XYreturn(self):
        return self.x - 150, self.y - 150, self.x + 150, self.y + 150
