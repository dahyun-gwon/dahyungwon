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

    def draw(self):
        self.image.clip_draw(0,0,1200,230,self.x,self.y)

    def update(self):
        self.time-=game_framework.frame_time
        self.x=main_state.tienaa.X()+650
        self.y=main_state.tienaa.Y()
        if self.time<=0:
            game_world.remove_object(self)
