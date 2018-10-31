from pico2d import*
import game_framework
import game_world
from fire_basic_attack import Fire_basic_attack
from water_basic_attack import Water_basic_attack
from fire_w import Fire_w
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#DIAG_LEFTUP_UP,DIAG_RIGHTUP_UP,DIAG_LEFTDOWN_UP,DIAG_RIGHTDOWN_UP,DIAG_LEFTUP_DOWN,DIAG_RIGHTUP_DOWN,DIAG_LEFTDOWN_DOWN,DIAG_RIGHTDOWN_DOWN
RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP, LEFT_UP, f, w, e, r,SPACE= range(13)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_f): f,
    (SDL_KEYDOWN, SDLK_w): w,
    (SDL_KEYDOWN, SDLK_e): e,
    (SDL_KEYDOWN, SDLK_r): r,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
    #(SDL_KEYUP,SDLK_LEFT and SDLK_UP) : DIAG_LEFTUP_UP,
    #(SDL_KEYUP,SDLK_RIGHT and SDLK_UP) : DIAG_RIGHTUP_UP,
    #(SDL_KEYUP,SDLK_LEFT and SDLK_DOWN) : DIAG_LEFTDOWN_UP,
    #(SDL_KEYUP,SDLK_RIGHT and SDLK_DOWN):DIAG_RIGHTDOWN_UP,
    #(SDL_KEYDOWN,SDLK_LEFT and SDLK_UP) : DIAG_LEFTUP_DOWN,
    #(SDL_KEYDOWN,SDLK_RIGHT and SDLK_UP) : DIAG_RIGHTUP_DOWN,
    #(SDL_KEYDOWN,SDLK_LEFT and SDLK_DOWN) : DIAG_LEFTDOWN_DOWN,
    #(SDL_KEYDOWN,SDLK_RIGHT and SDLK_DOWN):DIAG_RIGHTDOWN_DOWN

}

class Fire_Wisp:
    @staticmethod
    def enter(wisp, event):
        if event == RIGHT_DOWN:
            wisp.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            wisp.Xvelocity += RUN_SPEED_PPS
        elif event == UP_UP:
            wisp.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            wisp.Yvelocity+=RUN_SPEED_PPS
        elif event == DOWN_UP:
            wisp.Yvelocity+=RUN_SPEED_PPS
        elif event==DOWN_DOWN:
            wisp.Yvelocity-=RUN_SPEED_PPS

    @staticmethod
    def exit(wisp, event):
        if event == SPACE:
            wisp.fire_basic_attack()

        elif event == w:
            wisp.fire_w()

    @staticmethod
    def do(wisp):
        wisp.frame=(wisp.frame+1)%18
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time



    @staticmethod
    def draw(wisp):
        wisp.fire_image.clip_draw(wisp.frame*98,0,100,100,wisp.x,wisp.y)



class Water_Wisp:
    @staticmethod
    def enter(wisp, event):
        if event == RIGHT_DOWN:
            wisp.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            wisp.Xvelocity += RUN_SPEED_PPS
        elif event == UP_UP:
            wisp.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            wisp.Yvelocity += RUN_SPEED_PPS
        elif event == DOWN_UP:
            wisp.Yvelocity += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            wisp.Yvelocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(wisp, event):
        if event==SPACE:
            wisp.water_basic_attack()

    @staticmethod
    def do(wisp):
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time

    @staticmethod
    def draw(wisp):
        wisp.water_image.draw(wisp.x,wisp.y)


class Leaf_Wisp:
    @staticmethod
    def enter(wisp, event):
        if event == RIGHT_DOWN:
            wisp.Xvelocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            wisp.Xvelocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            wisp.Xvelocity +=RUN_SPEED_PPS
        elif event == UP_UP:
            wisp.Yvelocity -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            wisp.Yvelocity+=RUN_SPEED_PPS
        elif event == DOWN_UP:
            wisp.Yvelocity+=RUN_SPEED_PPS
        elif event==DOWN_DOWN:
            wisp.Yvelocity-=RUN_SPEED_PPS


    @staticmethod
    def exit(wisp, event):
        if event == SPACE:
            wisp.fire_basic_attack()


    @staticmethod
    def do(wisp):
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time



    @staticmethod
    def draw(wisp):
        wisp.water_image.draw(wisp.x, wisp.y)

next_state_table = {
    Water_Wisp: {RIGHT_DOWN: Water_Wisp, LEFT_DOWN: Water_Wisp, UP_UP: Water_Wisp, UP_DOWN: Water_Wisp, DOWN_UP:Water_Wisp,DOWN_DOWN:Water_Wisp,RIGHT_UP:Water_Wisp,LEFT_UP:Water_Wisp,f:Fire_Wisp,SPACE:Water_Wisp},
    Fire_Wisp: {RIGHT_DOWN: Fire_Wisp, LEFT_DOWN: Fire_Wisp, UP_UP: Fire_Wisp, UP_DOWN: Fire_Wisp,DOWN_UP:Fire_Wisp,DOWN_DOWN:Fire_Wisp,RIGHT_UP:Fire_Wisp,LEFT_UP:Fire_Wisp,f:Water_Wisp,SPACE:Fire_Wisp,w:Fire_Wisp}
}
#next_state_table = {
#        Fire_Wisp: {d:Leaf_Wisp,f:Water_Wisp},
#        Water_Wisp: {d:Fire_Wisp,f:Leaf_Wisp},
#        Leaf_Wisp:{d:Water_Wisp,f:Fire_Wisp}
#    }

class Wisp:
    def __init__(self):
        Wisp.fire_image = load_image('fire_wisp_sprite.png')
        Wisp.water_image = load_image('Watar_wisp.png')
        self.frame=0
        self.x, self.y = 500-30,500+30
        self.event_que = []
        self.cur_state = Fire_Wisp
        self.cur_state.enter(self, None)
        self.Xvelocity=0
        self.Yvelocity=0

    def fire_basic_attack(self):
        fire = Fire_basic_attack(self.x+30+30, self.y-30, 1)
        game_world.add_object(fire, 1)
    def fire_w(self):
        fire_w = Fire_w(self.x+30+30, self.y-30, 1)
        game_world.add_object(fire_w, 1)
    def water_basic_attack(self):
        water=Water_basic_attack(self.x+30+30, self.y-30, 1)
        game_world.add_object(water, 1)



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


