import game_framework
from pico2d import *
import game_world
from fire_basic_attack import Fire_basic_attack
from wisp import Fire_Wisp
from wisp import Water_Wisp
from wisp import Leaf_Wisp
import wisp

PIXEL_PER_METER = (10.0/0.3)
i=1
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8
RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP, LEFT_UP, SPACE, w, e, r= range(12)

Wisp=(Fire_Wisp,Water_Wisp,Leaf_Wisp)

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
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_w): w,
    (SDL_KEYDOWN, SDLK_e): e,
    (SDL_KEYDOWN, SDLK_r): r
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
        if event==SPACE:
            tiena.fire_basic_attack()
        elif event==w:
            tiena.fire_basic_attack()
        elif event==e:
            tiena.fire_basic_attack()
        elif event==r:
            tiena.fire_basic_attack()


    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16


    @staticmethod
    def draw(tiena):
        tiena.image.clip_draw(int(tiena.frame) * 150, 0, 150, 150, tiena.x, tiena.y)


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
        elif event==RIGHT_DOWN and UP_DOWN:
            tiena.Xvelocity+=RUN_SPEED_PPS
            tiena.Yvelocity+=RUN_SPEED_PPS
        elif event==LEFT_UP and DOWN_UP:
            tiena.Xvelocity++RUN_SPEED_PPS
            tiena.Yvelocity+=RUN_SPEED_PPS


    @staticmethod
    def exit(tiena, event):
        if event==SPACE:
            tiena.fire_basic_attack()
        elif event==w:
            tiena.fire_basic_attack()
        elif event==e:
            tiena.fire_basic_attack()
        elif event==r:
            tiena.fire_basic_attack()


    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        tiena.x += tiena.Xvelocity * game_framework.frame_time
        tiena.y+=tiena.Yvelocity*game_framework.frame_time


    @staticmethod
    def draw(tiena):
        tiena.image.clip_draw(int(tiena.frame) * 150, 0, 150, 150, tiena.x, tiena.y)



next_state_table = {
    IdleState: {RIGHT_DOWN: GoState, LEFT_DOWN: GoState, UP_UP: GoState, UP_DOWN: GoState, DOWN_UP:GoState,DOWN_DOWN:GoState,RIGHT_UP:GoState,LEFT_UP:GoState,SPACE:IdleState},
    GoState: {RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_UP: IdleState, UP_DOWN: IdleState,DOWN_UP:IdleState,DOWN_DOWN:IdleState,RIGHT_UP:IdleState,LEFT_UP:IdleState,SPACE:GoState},
}

class Tiena:
    def __init__(self):
        self.image = load_image('tiena_sprite.png')
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
    def wisp(self):
        pass

    def fire_basic_attack(self):
        ball = Fire_basic_attack(self.x, self.y, 3)
        game_world.add_object(ball, 1)
    def add_event(self, event):
        self.event_que.insert(0, event)
    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def Xreturn(self):
        return self.x
    def Yreturn(self):
        return self.y