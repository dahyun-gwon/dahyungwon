from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Fire_Monster:
    image = None

    def __init__(self,x,y):
        if Fire_Monster.image == None:
            Fire_Monster.image = load_image('bomp.png')
        self.x=x
        self.y=y
        self.state = True;
        self.HP = 20
        self.damage=20

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x -= 5
        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)
        if self.HP<1:self.state=False

    def XYreturn(self):
        return self.x-15,self.y-25,self.x+15,self.y+25
    def killed(self):
        game_world.remove_object(self)


