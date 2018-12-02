import game_framework
from pico2d import *
import game_world
import main_state
import enemy
import lamp_attack
import lamp_attack2
import planet

DISTANCE=0.3   #수치 적을수록 가까이
PIXEL_PER_METER = 90/1.5
i=1
RUN_SPEED_KMPH = 60.0
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
}

class IdleState:
    @staticmethod
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += RUN_SPEED_PPS*DISTANCE
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == RIGHT_UP:
            tiena.Xvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == LEFT_UP:
            tiena.Xvelocity += RUN_SPEED_PPS*DISTANCE
        elif event == UP_UP:
            tiena.Yvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == UP_DOWN:
            tiena.Yvelocity+=RUN_SPEED_PPS*DISTANCE
        elif event == DOWN_UP:
            tiena.Yvelocity+=RUN_SPEED_PPS*DISTANCE
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=RUN_SPEED_PPS*DISTANCE



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
            tiena.Xvelocity += RUN_SPEED_PPS*DISTANCE
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == RIGHT_UP:
            tiena.Xvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == LEFT_UP:
            tiena.Xvelocity += RUN_SPEED_PPS*DISTANCE
        elif event == UP_UP:
            tiena.Yvelocity -= RUN_SPEED_PPS*DISTANCE
        elif event == UP_DOWN:
            tiena.Yvelocity+=RUN_SPEED_PPS*DISTANCE
        elif event == DOWN_UP:
            tiena.Yvelocity+=RUN_SPEED_PPS*DISTANCE
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=RUN_SPEED_PPS*DISTANCE



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
class Failed_Tiena:
    def __init__(self,x,y):
        self.image = load_image('failed.png')
        self.x=x
        self.y=y

        self.state = True
        self.frame=0

    def update(self):
        self.y-=10
        self.frame+=self.frame%10


    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.x,self.y)

    def handle_events(self,event):
        pass

    def XYreturn(self):
        pass

class Tiena:
    def __init__(self):
        self.image = load_image('tiena_sprite.png')
        self.idle_image=load_image('tiena_idle.png')
        self.x_dir,self.y_dir=0,0
        self.x = 500
        self.y = 500
        self.frame=0
        self.HP = 200
        self.Xvelocity=0
        self.Yvelocity=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.damage=100
        self.state = True


    def add_event(self, event):
        self.event_que.insert(0, event)
    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        self.x=clamp(0, self.x, 1200)
        self.y = clamp(0, self.y, 800)

        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == enemy.Fire_Monster:
                    if main_state.collide(self,o):
                        main_state.tiena_HP-=50
                        game_world.remove_object(o)
                if type(o) == enemy.Lamp_enemy:
                    if main_state.collide(self,o):
                        main_state.tiena_HP-=200
                        game_world.remove_object(o)
                if type(o) == enemy.Lamp_enemy:
                    if main_state.collide(self,o):
                        main_state.tiena_HP-=200
                        game_world.remove_object(o)
                if type(o) == planet.Planet:
                    if main_state.collide(self,o):
                        main_state.tiena_HP-=80
                        game_world.remove_object(o)


        if(main_state.tiena_HP<1):
            fail_tiena=Failed_Tiena(self.x,self.y)
            game_world.add_object(fail_tiena,2)
            game_world.remove_object(self)





    def draw(self):
        self.cur_state.draw(self)

    def handle_events(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def XYreturn(self):
        return self.x-40,self.y-35,self.x+40,self.y+35

    def XY(self):
        return self.x,self.y
    def X(self):
        return self.x
    def Y(self):
        return self.y
