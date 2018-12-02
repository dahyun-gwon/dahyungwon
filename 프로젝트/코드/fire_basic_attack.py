from pico2d import *
import game_world
import game_framework
DISTANCE=0.3   #수치 적을수록 가까이
PIXEL_PER_METER = 90/1.5
RUN_SPEED_KMPH = 100
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
class Fire_basic_attack:
    image = None

    def __init__(self, x , y):
        if Fire_basic_attack.image == None:
            Fire_basic_attack.image = load_image('basic.png')
        self.x, self.y, self.Xvelocity = x, y,RUN_SPEED_PPS*DISTANCE
        self.state = True

        self.damage=50

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity * game_framework.frame_time

        if self.x < 0 or self.x > 1300:
            game_world.remove_object(self)
    def XYreturn(self):
        return self.x-20,self.y-20,self.x+20,self.y+20
    def handle_events(self,event):
        pass