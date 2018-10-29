from pico2d import *
import game_world
from fire_wisp import Fire_Wisp
from water_wisp import Water_Wisp
from leaf_wisp import Leaf_Wisp
RIGHT_DOWN, LEFT_DOWN,UP_UP,UP_DOWN,DOWN_UP,DOWN_DOWN, RIGHT_UP, LEFT_UP,SPACE,W,E,R,D,F= range(14)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP,SDLK_UP):UP_UP,
    (SDL_KEYDOWN,SDLK_UP):UP_DOWN,
    (SDL_KEYUP,SDLK_DOWN):DOWN_UP,
    (SDL_KEYDOWN,SDLK_DOWN):DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN,SDLK_SPACE):SPACE,
    (SDL_KEYDOWN,SDLK_w):W,
    (SDL_KEYDOWN,SDLK_e):E,
    (SDL_KEYDOWN,SDLK_r):R,
    (SDL_KEYDOWN,SDLK_d):D,
    (SDL_KEYDOWN,SDLK_f):F
}

class IdleState:

    @staticmethod
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += 1
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= 1
        elif event == RIGHT_UP:
            tiena.Xvelocity -= 1
        elif event == LEFT_UP:
            tiena.Xvelocity += 1
        elif event == UP_UP:
            tiena.Yvelocity -= 1
        elif event == UP_DOWN:
            tiena.Yvelocity+=1
        elif event == DOWN_UP:
            tiena.Yvelocity+=1
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=1


    @staticmethod
    def exit(tiena, event):
        if event==SPACE:
            tiena.fire_ball()
        elif event==W:
            pass
        elif event==E:
            pass
        elif event==R:
            pass
        elif event==D:
            pass
        elif event==F:
            pass

    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + 1) % 8


    @staticmethod
    def draw(tiena):
            tiena.image.clip_draw(tiena.frame * 200, 0, 200, 200, tiena.x, tiena.y)


class GoState:

    @staticmethod
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += 1
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= 1
        elif event == RIGHT_UP:
            tiena.Xvelocity -= 1
        elif event == LEFT_UP:
            tiena.Xvelocity += 1
        elif event == UP_UP:
            tiena.Yvelocity -= 1
        elif event == UP_DOWN:
            tiena.Yvelocity+=1
        elif event == DOWN_UP:
            tiena.Yvelocity+=1
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=1

    @staticmethod
    def exit(tiena, event):
        if event==SPACE:
            tiena.fire_ball()
        elif event==W:
            pass
        elif event==E:
            pass
        elif event==R:
            pass
        elif event==D:
            pass
        elif event==F:
            pass

    @staticmethod
    def do(tiena):
        tiena.frame=(tiena.frame+1)%16

    @staticmethod
    def draw(tiena):
        tiena.image.clip_draw(tiena.frame*200,0,200,200,tiena.x,tiena.y)


class Injured_State:
    def enter(tiena, event):
        if event == RIGHT_DOWN:
            tiena.Xvelocity += 1
        elif event == LEFT_DOWN:
            tiena.Xvelocity -= 1
        elif event == RIGHT_UP:
            tiena.Xvelocity -= 1
        elif event == LEFT_UP:
            tiena.Xvelocity += 1
        elif event == UP_UP:
            tiena.Yvelocity -= 1
        elif event == UP_DOWN:
            tiena.Yvelocity+=1
        elif event == DOWN_UP:
            tiena.Yvelocity+=1
        elif event==DOWN_DOWN:
            tiena.Yvelocity-=1


    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + 1) % 16
        tiena.x += tiena.velocity*3
        tiena.x = clamp(25, tiena.x, 1600 - 25)


    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: GoState, LEFT_UP: GoState, RIGHT_DOWN: GoState, LEFT_DOWN: GoState, UP_UP:GoState,UP_DOWN:GoState,DOWN_UP:GoState,DOWN_DOWN:GoState,SPACE:IdleState},
    GoState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,UP_UP:IdleState,UP_DOWN:IdleState,DOWN_UP:IdleState,DOWN_DOWN:IdleState,SPACE:GoState,},
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




    def basic_attack(self):

        game_world.add_object(ball,1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def hanlde_events(self):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y