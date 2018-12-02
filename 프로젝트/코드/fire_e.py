from pico2d import *
import game_world
import game_framework
DISTANCE=0.3   #수치 적을수록 가까이
PIXEL_PER_METER = 90/1.5
RUN_SPEED_KMPH = 120
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
class Fire_e:
    image = None

    def __init__(self, x = 450, y = 300, Xvelocity = 1):
        if Fire_e.image == None:
            Fire_e.image = load_image('e_basic.png')
        self.x, self.y, self.Xvelocity = x, y, RUN_SPEED_PPS * DISTANCE
        self.state = True
        self.damage=70

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity * game_framework.frame_time
        if self.x < 25 or self.x > 1300:
            game_world.remove_object(self)
    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x - 40, self.y - 30, self.x + 40, self.y + 30