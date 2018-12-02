from pico2d import *
import game_framework
import game_world
DISTANCE=0.3
PIXEL_PER_METER = 90/1.5
RUN_SPEED_KMPH = 150
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
class Fire_w:
    image = None

    def __init__(self, x ,y , Xvelocity = 1):
        if Fire_w.image == None:
            Fire_w.image = load_image('fire_w.png')
        self.x, self.y, self.Xvelocity = x, y,RUN_SPEED_PPS * DISTANCE
        self.damage=200
        self.state = True
    def handle_events(self,event):
        pass
    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.XYreturn())

    def update(self):
        self.x += self.Xvelocity * game_framework.frame_time
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x - 180, self.y - 90, self.x + 200, self.y + 90



