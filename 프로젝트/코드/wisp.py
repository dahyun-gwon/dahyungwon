from pico2d import*
import game_framework
import game_world
from fire_basic_attack import Fire_basic_attack
from fire_w import Fire_w
from fire_e import Fire_e
from fire_r import Fire_r
from water_basic_attack import Water_basic_attack
from water_w import Water_w
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
water_w=None
water_r=None
leaf=None
leaf_e=None
leaf_w=None
import tiena
from tiena import  Tiena

PIXEL_PER_METER = 10
RUN_SPEED_KMPH = 100.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8

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

}

class Fire_Wisp:
    @staticmethod
    def enter(wisp, event):
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == tiena.Tiena:
                    wisp.x=o.x - 5*PIXEL_PER_METER
                    wisp.y=o.y + 7*PIXEL_PER_METER

    @staticmethod
    def exit(wisp, event):
        if event==SPACE:
            if (wisp.fire_e_using_time <= 0):
                if wisp.fire_basic_timer >0.25:
                    wisp.fire_basic_attack()
                    wisp.fire_basic_timer=0

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
            for o in game_world.objects[2]:
                if type(o) == tiena.Tiena:
                    wisp.x = o.x - 5 * PIXEL_PER_METER
                    wisp.y = o.y + 7 * PIXEL_PER_METER
            wisp.cnt+=1
            if wisp.cnt==3:
                wisp.frame+=1
                wisp.cnt=0
            wisp.frame=wisp.frame%17

    @staticmethod
    def draw(wisp):
        wisp.fire_image.clip_draw(wisp.frame*101,0,101,100,wisp.x,wisp.y)

class Water_Wisp:
    @staticmethod
    def enter(wisp, event):
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == tiena.Tiena:
                    wisp.x=o.x - 5*PIXEL_PER_METER
                    wisp.y=o.y + 7*PIXEL_PER_METER

    @staticmethod
    def exit(wisp, event):
        if event==SPACE:
            if wisp.water_e_using_time<=0:
                if wisp.water_basic_timer>0.5:
                    wisp.water_basic_attack()
                    wisp.water_basic_timer=0
            elif wisp.water_e_using_time>0:
                wisp.water_basic_attack()
        elif event == w:
            if(wisp.water_w_timer>=15):
                wisp.water_w()
                wisp.water_w_timer=0
        elif event == e:
            if(wisp.water_e_timer>=15):
                wisp.water_e_using_time=5
                wisp.water_e_timer=0

        elif event == r:
            if(wisp.water_r_timer>=40):
                wisp.water_r()
                wisp.water_timer=0

    @staticmethod
    def do(wisp):
        for o in game_world.objects[2]:
            if type(o) == main_state.Tiena:
                wisp.x=o.x - 5*PIXEL_PER_METER
                wisp.y=o.y + 7*PIXEL_PER_METER


    @staticmethod
    def draw(wisp):
        wisp.water_image.draw(wisp.x,wisp.y)

class Leaf_Wisp:
    @staticmethod
    def enter(wisp, event):
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == tiena.Tiena:
                    wisp.x=o.x - 5*PIXEL_PER_METER
                    wisp.y=o.y + 7*PIXEL_PER_METER

    @staticmethod
    def exit(wisp, event):
        if event == SPACE:
            if wisp.leaf_basic_timer>0.5:
                wisp.leaf_basic_attack()
                wisp.leaf_basic_timer=0
        elif event==e:
            if(wisp.leaf_e_timer>=15):
                wisp.leaf_e()
                wisp.leaf_e_timer=0
        elif event==w:
            if(wisp.leaf_w_timer>=20):
                wisp.leaf_w()
                wisp.leaf_w_timer=0
        elif event==r:
             pass

    @staticmethod
    def do(wisp):
        if(wisp.cnt>3):
            wisp.cnt=0
            wisp.frame+=1
        wisp.cnt+=1
        wisp.frame = wisp.frame  % 16
        for o in game_world.objects[2]:
            if type(o) == main_state.Tiena:
                wisp.x=o.x - 5*PIXEL_PER_METER
                wisp.y=o.y + 7*PIXEL_PER_METER

    @staticmethod
    def draw(wisp):
        wisp.leaf_image.clip_draw(wisp.frame * 60, 0, 60, 75, wisp.x, wisp.y)


next_state_table = {
    Fire_Wisp: {RIGHT_DOWN: Fire_Wisp, LEFT_DOWN: Fire_Wisp, UP_UP: Fire_Wisp, UP_DOWN: Fire_Wisp,DOWN_UP:Fire_Wisp,DOWN_DOWN:Fire_Wisp,RIGHT_UP:Fire_Wisp,LEFT_UP:Fire_Wisp,d:Leaf_Wisp,f:Water_Wisp,SPACE:Fire_Wisp,e:Fire_Wisp,w:Fire_Wisp,r:Fire_Wisp},
    Water_Wisp: {RIGHT_DOWN: Water_Wisp, LEFT_DOWN: Water_Wisp, UP_UP: Water_Wisp, UP_DOWN: Water_Wisp, DOWN_UP:Water_Wisp,DOWN_DOWN:Water_Wisp,RIGHT_UP:Water_Wisp,LEFT_UP:Water_Wisp,d:Fire_Wisp,f:Leaf_Wisp,SPACE:Water_Wisp,w:Water_Wisp,e:Water_Wisp,r:Water_Wisp},
    Leaf_Wisp: {RIGHT_DOWN: Leaf_Wisp, LEFT_DOWN:Leaf_Wisp, UP_UP: Leaf_Wisp, UP_DOWN: Leaf_Wisp, DOWN_UP:Leaf_Wisp,DOWN_DOWN:Leaf_Wisp,RIGHT_UP:Leaf_Wisp,LEFT_UP:Leaf_Wisp,d:Water_Wisp,f:Fire_Wisp,SPACE:Leaf_Wisp,w:Leaf_Wisp,e:Leaf_Wisp,r:Leaf_Wisp},
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
        self.state = True
        self.fire_basic_timer=1
        self.water_basic_timer=1
        self.leaf_basic_timer=2
        self.fire_w_timer=10
        self.fire_e_using_time=0
        self.fire_e_cool_timer=10
        self.fire_r_timer = 40
        self.water_e_timer=10
        self.water_e_using_time=0
        self.water_w_timer=15
        self.water_r_timer=40
        self.leaf_w_timer=20
        self.leaf_e_timer=15

    def fire_basic_attack(self):
        fire_attack = Fire_basic_attack(self.x+30+100, self.y-30-30)
        game_world.add_object(fire_attack, 1)

    def fire_w(self):
        fire_w= Fire_w(self.x+30, self.y-30, 1)
        game_world.add_object(fire_w, 1)

    def fire_e(self):
        fire_e = Fire_e(self.x+130, self.y-60, 1)
        game_world.add_object(fire_e, 1)

    def fire_r(self):
        fire_r=Fire_r(0,400)
        game_world.add_object(fire_r,1)
    def water_basic_attack(self):
        water1=Water_basic_attack(self.x+30+100, self.y-30-30,5,0)
        game_world.add_object(water1, 1)
        water2 = Water_basic_attack(self.x + 30 + 100, self.y - 30 - 30, 5, 2)
        game_world.add_object(water2, 1)
        water3 = Water_basic_attack(self.x + 30 + 100, self.y - 30 - 30, 5, -2)
        game_world.add_object(water3, 1)
    def water_w(self):
        water_w=Water_w(self.x+30,self.y-30)
        game_world.add_object(water_w,1)


    def water_r(self):
        water_r=Water_r(self.x+700,self.y-30)
        game_world.add_object(water_r,1)
    def leaf_basic_attack(self):
        leaf=Leaf_basic_attack(self.x+30+100, self.y-30-30, 1)
        game_world.add_object(leaf, 1)
    def leaf_w(self):
        leaf_w=Leaf_w(self.x+40,self.y-60)
        game_world.add_object(leaf_w, 1)

    def leaf_e(self):
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
        self.fire_basic_timer+=game_framework.frame_time
        self.water_basic_timer+=game_framework.frame_time
        self.leaf_basic_timer+=game_framework.frame_time
        self.fire_w_timer+=game_framework.frame_time
        self.fire_r_timer+=game_framework.frame_time
        self.fire_e_using_time-=game_framework.frame_time
        self.fire_e_cool_timer += game_framework.frame_time
        self.fire_r_timer+=game_framework.frame_time
        self.water_w_timer+=game_framework.frame_time
        self.water_e_timer+=game_framework.frame_time
        self.water_e_using_time-=game_framework.frame_time
        self.leaf_w_timer+=game_framework.frame_time
        self.leaf_e_timer+=game_framework.frame_time
        if main_state.tiena_HP<1:
            game_world.remove_object(self)




    def draw(self):
        self.cur_state.draw(self)


    def handle_events(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

