import game_framework
from pico2d import *
import game_world
import main_state
import enemy



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

#DIAG_LEFTUP_UP,DIAG_RIGHTUP_UP,DIAG_LEFTDOWN_UP,DIAG_RIGHTDOWN_UP,DIAG_LEFTUP_DOWN,DIAG_RIGHTUP_DOWN,DIAG_LEFTDOWN_DOWN,DIAG_RIGHTDOWN_DOWN

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

class IdleState:
    @staticmethod
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            tiena.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            tiena.Xvelocity += RUN_SPEED_PPS
        elif event == UP_UP:
            tiena.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            tiena.Yvelocity+=RUN_SPEED_PPS
        elif event == DOWN_UP:
            tiena.Yvelocity+=RUN_SPEED_PPS
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=RUN_SPEED_PPS



    @staticmethod
    def exit(tiena, event):
        pass


    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        tiena.x += tiena.Xvelocity * game_framework.frame_time
        tiena.y += tiena.Yvelocity * game_framework.frame_time


    @staticmethod
    def draw(tiena):
        tiena.idle_image.clip_draw(int(tiena.frame) * 150, 0, 150, 150, tiena.x, tiena.y)



class GoState:

    @staticmethod
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            tiena.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            tiena.Xvelocity += RUN_SPEED_PPS
        elif event == UP_UP:
            tiena.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            tiena.Yvelocity+=RUN_SPEED_PPS
        elif event == DOWN_UP:
            tiena.Yvelocity+=RUN_SPEED_PPS
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=RUN_SPEED_PPS



    @staticmethod
    def exit(tiena, event):
        pass


    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        tiena.x += tiena.Xvelocity * game_framework.frame_time
        tiena.y+=tiena.Yvelocity*game_framework.frame_time


    @staticmethod
    def draw(tiena):
        tiena.image.clip_draw(int(tiena.frame) * 150, 0, 150, 150, tiena.x, tiena.y)





next_state_table = {
    IdleState: {RIGHT_DOWN: GoState, LEFT_DOWN: GoState, UP_UP: GoState, UP_DOWN: GoState, DOWN_UP:GoState,DOWN_DOWN:GoState,RIGHT_UP:GoState,LEFT_UP:GoState},
    GoState: {RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_UP: IdleState, UP_DOWN: IdleState,DOWN_UP:IdleState,DOWN_DOWN:IdleState,RIGHT_UP:IdleState,LEFT_UP:IdleState},
}

class Tiena:
    def __init__(self):
        self.image = load_image('tiena_sprite.png')
        self.idle_image=load_image('tiena_idle.png')
        self.x_dir,self.y_dir=0,0
        self.x = 500
        self.y = 500
        self.frame=0
        self.HP = 100
        self.Xvelocity=0
        self.Yvelocity=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.damage=100


        self.state = True;


    def add_event(self, event):
        self.event_que.insert(0, event)
    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)





        if(self.HP<1):
            self.state=False
            self.x,self.y=0,0





    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def XYreturn(self):
        return self.x-25,self.y-25,self.x+25,self.y+25

    def XY(self):
        return self.x,self.y
    def X(self):
        return self.x
    def Y(self):
        return self.y
    def killed(self):
        game_world.remove_object(self)
