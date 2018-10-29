import game_framework
from pico2d import *
import game_world
from fire_basic_attack import Fire_basic_attack

RIGHT_DOWN, LEFT_DOWN, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, RIGHT_UP, LEFT_UP, SPACE, w, e, r, d, f = range(14)

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
    (SDL_KEYDOWN, SDLK_r): r,
    (SDL_KEYDOWN, SDLK_d): d,
    (SDL_KEYDOWN, SDLK_f): f
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
            tiena.fire_basic_attack()
        elif event==w:
            tiena.fire_basic_attack()
        elif event==e:
            tiena.fire_basic_attack()
        elif event==r:
            tiena.fire_basic_attack()
        elif event==d:
            tiena.fire_basic_attack()
        elif event==f:
            tiena.fire_basic_attack()

    @staticmethod
    def do(tiena):
        tiena.frame = (tiena.frame + 1) % 16


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
            tiena.fire_basic_attack()
        elif event==w:
            tiena.fire_basic_attack()
        elif event==e:
            tiena.fire_basic_attack()
        elif event==r:
            tiena.fire_basic_attack()
        elif event==d:
            tiena.fire_basic_attack()
        elif event==f:
            tiena.fire_basic_attack()

    @staticmethod
    def do(tiena):
        tiena.frame=(tiena.frame+1)%16

    @staticmethod
    def draw(tiena):
        tiena.image.clip_draw(tiena.frame*200,0,200,200,tiena.x,tiena.y)


class Injured_State:

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

    def fire_ball(self):
        ball = Fire_basic_attack(self.x, self.y, self.dir*3)
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

    def handle_event(self):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)