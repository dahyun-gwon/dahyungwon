from pico2d import *
import game_world
import game_framework
import main_state

PIXEL_PER_METER = (10.0/0.3)
i=1
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8
RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP, LEFT_UP= range(8)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    #(SDL_KEYUP,SDLK_LEFT and SDLK_UP) : DIAG_LEFTUP_UP,
    #(SDL_KEYUP,SDLK_RIGHT and SDLK_UP) : DIAG_RIGHTUP_UP,
    #(SDL_KEYUP,SDLK_LEFT and SDLK_DOWN) : DIAG_LEFTDOWN_UP,
    #(SDL_KEYUP,SDLK_RIGHT and SDLK_DOWN):DIAG_RIGHTDOWN_UP,
    #(SDL_KEYDOWN,SDLK_LEFT and SDLK_UP) : DIAG_LEFTUP_DOWN,
    #(SDL_KEYDOWN,SDLK_RIGHT and SDLK_UP) : DIAG_RIGHTUP_DOWN,
    #(SDL_KEYDOWN,SDLK_LEFT and SDLK_DOWN) : DIAG_LEFTDOWN_DOWN,
    #(SDL_KEYDOWN,SDLK_RIGHT and SDLK_DOWN):DIAG_RIGHTDOWN_DOWN

}

class Leaf_w:
    image = None


    def __init__(self,x ,y):
        if Leaf_w.image == None:
            Leaf_w.image = load_image('leaf_w.png')
        self.x, self.y= x, y
        self.Xvelocity=0
        self.Yvelocity=0
        self.time=3
    def draw(self):

        self.image.draw(self.x,self.y)

    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
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


    def update(self):
        self.x,self.y = main_state.tienaa.XY()
        self.x+=self.Xvelocity
        self.y+=self.Yvelocity
        self.time-=game_framework.frame_time
        if self.time<=0:
            game_world.remove_object(self)

