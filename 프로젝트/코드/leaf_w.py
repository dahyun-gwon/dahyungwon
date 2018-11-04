from pico2d import *
import game_world
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8
RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP,LEFT_UP= range(8)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}

class Leaf_w:
    image = None

    def __init__(self, x , y ):
        if Leaf_w.image == None:
            Leaf_w.image = load_image('leaf_w.png')
        self.x, self.y= x, y
        self.frame=0
        self.cnt=0
        self.Xvelocity=0
        self.Yvelocity=0

    def draw(self):

        self.image.draw(self.x,self.y)



    def update(self,event):
        if event == RIGHT_DOWN:
            self.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            self.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            self.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            self.Xvelocity += RUN_SPEED_PPS
        elif event == UP_UP:
            self.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            self.Yvelocity+=RUN_SPEED_PPS
        elif event == DOWN_UP:
            self.Yvelocity+=RUN_SPEED_PPS
        elif event==DOWN_DOWN:
            self.Yvelocity-=RUN_SPEED_PPS
        self.x+=self.Xvelocity
        self.y+=self.Yvelocity
