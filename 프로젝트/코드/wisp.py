from pico2d import*
import game_framework
import game_world
from fire_basic_attack import Fire_basic_attack
from fire_w import Fire_w
from fire_e import Fire_e
from fire_r import Fire_r
from water_basic_attack import Water_basic_attack
from water_r import Water_r
from leaf_basic_attack import Leaf_basic_attack
from leaf_e import Leaf_e
from leaf_w import Leaf_w
import main_state
fire_attack=None
fire_w=None
fire_e=None
fire_r=None
water1=None
water2=None
water3=None
water_r=None
leaf=None
leaf_e=None
leaf_w=None

from tiena import  Tiena

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8



#DIAG_LEFTUP_UP,DIAG_RIGHTUP_UP,DIAG_LEFTDOWN_UP,DIAG_RIGHTDOWN_UP,DIAG_LEFTUP_DOWN,DIAG_RIGHTUP_DOWN,DIAG_LEFTDOWN_DOWN,DIAG_RIGHTDOWN_DOWN
RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP, LEFT_UP, d,f, w, e, r,SPACE= range(14)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN,SDLK_d):d,
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
        if event==SPACE:
            if (wisp.fire_e_using_time <= 0):
                wisp.fire_basic_attack()
            else:
                wisp. fire_e()

        elif event == w:
            if(wisp.fire_w_timer>=10):
                wisp.fire_w()
                wisp.fire_w_timer=0

        elif event == e:
            if(wisp.fire_e_cool_timer>=10):
                wisp.fire_e_using_time=5
                wisp.fire_e_cool_timer=0


        elif event == r:
            if(wisp.fire_r_timer>=40):
                wisp.fire_r()
                wisp.fire_r_timer=0

    @staticmethod
    def do(wisp):
        if(wisp.cnt==5):
            wisp.cnt=0
            wisp.frame+=1
        wisp.frame=wisp.frame%17
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time
        wisp.cnt += 1

    @staticmethod
    def draw(wisp):
        wisp.fire_image.clip_draw(wisp.frame*101,0,101,100,wisp.x,wisp.y)

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

        elif event == r:
            if(wisp.water_r_timer>=40):
                wisp.water_r()
                wisp.water_timer=0

    @staticmethod
    def do(wisp):
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time
        wisp.i+=0.01

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
            wisp.leaf_basic_attack()
        elif event==e:
            if(wisp.leaf_e_timer>=15):
                wisp.leaf_e()
                wisp.leaf_e_timer=0
        elif event==w:
            if(wisp.leaf_w_timer>=20):
                wisp.leaf_w()
                wisp.leaf_w_timer=0

    @staticmethod
    def do(wisp):
        wisp.x += wisp.Xvelocity * game_framework.frame_time
        wisp.y += wisp.Yvelocity * game_framework.frame_time
        if(wisp.cnt>3):
            wisp.cnt=0
            wisp.frame+=1
        wisp.cnt+=1
        wisp.frame = wisp.frame  % 16

    @staticmethod
    def draw(wisp):
        wisp.leaf_image.clip_draw(wisp.frame * 60, 0, 60, 75, wisp.x, wisp.y)


next_state_table = {

    Fire_Wisp: {RIGHT_DOWN: Fire_Wisp, LEFT_DOWN: Fire_Wisp, UP_UP: Fire_Wisp, UP_DOWN: Fire_Wisp,DOWN_UP:Fire_Wisp,DOWN_DOWN:Fire_Wisp,RIGHT_UP:Fire_Wisp,LEFT_UP:Fire_Wisp,d:Leaf_Wisp,f:Water_Wisp,SPACE:Fire_Wisp,e:Fire_Wisp,w:Fire_Wisp,r:Fire_Wisp},
    Water_Wisp: {RIGHT_DOWN: Water_Wisp, LEFT_DOWN: Water_Wisp, UP_UP: Water_Wisp, UP_DOWN: Water_Wisp, DOWN_UP:Water_Wisp,DOWN_DOWN:Water_Wisp,RIGHT_UP:Water_Wisp,LEFT_UP:Water_Wisp,d:Fire_Wisp,f:Leaf_Wisp,SPACE:Water_Wisp,r:Water_Wisp},
    Leaf_Wisp: {RIGHT_DOWN: Leaf_Wisp, LEFT_DOWN:Leaf_Wisp, UP_UP: Leaf_Wisp, UP_DOWN: Leaf_Wisp, DOWN_UP:Leaf_Wisp,DOWN_DOWN:Leaf_Wisp,RIGHT_UP:Leaf_Wisp,LEFT_UP:Leaf_Wisp,d:Water_Wisp,f:Fire_Wisp,SPACE:Leaf_Wisp,w:Leaf_Wisp,e:Leaf_Wisp},
}

class Wisp:
    def __init__(self):
        Wisp.fire_image = load_image('fire_wisp_sprite.png')
        Wisp.water_image = load_image('Watar_wisp.png')
        Wisp.leaf_image = load_image('leaf_wisp_sprite.png')
        self.frame=0
        self.x, self.y = 500-40,500+60
        self.event_que = []
        self.cur_state = Fire_Wisp
        self.cur_state.enter(self, None)
        self.Xvelocity=0
        self.Yvelocity=0
        self.i=1
        self.cnt=0
        self.state = True;

        self.fire_w_timer=10
        self.fire_e_using_time=0
        self.fire_e_cool_timer=10
        self.fire_r_timer = 40

        self.water_r_timer=40

        self.leaf_w_timer=20
        self.leaf_e_timer=15

    def fire_basic_attack(self):
        global fire_attack
        fire_attack = Fire_basic_attack(self.x+30+100, self.y-30-30, 1)
        game_world.add_object(fire_attack, 1)

    def fire_w(self):
        global fire_w
        fire_w= Fire_w(self.x+30, self.y-30, 1)
        game_world.add_object(fire_w, 1)

    def fire_e(self):
        global  fire_e
        fire_e = Fire_e(self.x+130, self.y-60, 1)
        game_world.add_object(fire_e, 1)

    def fire_r(self):
        global fire_r
        fire_r=Fire_r(0,400)
        game_world.add_object(fire_r,1)
    def water_basic_attack(self):
        global water1
        global water2
        global water3
        water1=Water_basic_attack(self.x+30+100, self.y-30-30,5,0)
        game_world.add_object(water1, 1)
        water2 = Water_basic_attack(self.x + 30 + 100, self.y - 30 - 30, 5, 2)
        game_world.add_object(water2, 1)
        water3 = Water_basic_attack(self.x + 30 + 100, self.y - 30 - 30, 5, -2)
        game_world.add_object(water3, 1)


    def water_r(self):
        global water_r
        water_r=Water_r(self.x+700,self.y-30)
        game_world.add_object(water_r,1)
    def leaf_basic_attack(self):
        global leaf
        leaf=Leaf_basic_attack(self.x+30+100, self.y-30-30, 1)
        game_world.add_object(leaf, 1)
    def leaf_w(self):
        global leaf_w
        leaf_w=Leaf_w(self.x+40,self.y-60)
        game_world.add_object(leaf_w, 1)

    def leaf_e(self):
        global leaf_e
        leaf_e=Leaf_e(self.x+250,self.y-40)
        game_world.add_object(leaf_e, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        self.fire_w_timer+=game_framework.frame_time
        self.fire_r_timer+=game_framework.frame_time
        self.fire_e_using_time-=game_framework.frame_time
        self.fire_e_cool_timer += game_framework.frame_time
        self.fire_r_timer+=game_framework.frame_time
        self.leaf_w_timer+=game_framework.frame_time
        self.leaf_e_timer+=game_framework.frame_time
        if (main_state.tienaa.state==False):
            self.state=False



    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

