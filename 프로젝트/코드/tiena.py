from pico2d import *

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,SLEEP_TIMER,SPACE = range(6)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE

}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 100

    @staticmethod
    def exit(boy, event):
        if event==SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer-=1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:
    @staticmethod
    def enter(boy,enter):
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25,boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState,SPACE:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,SPACE:RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState,SPACE: IdleState}

}

class Tiena:

    def __init__(self):
        self.image = load_image('tiena_sprite.png')
        self.x_dir,self.y_dir=0,0
        self.x = 500
        self.y = 500
        self.velocity = 0
        self.frame=0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def hanlde_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.x_dir += 1
                elif event.key == SDLK_LEFT:
                    self.x_dir -= 1
                elif event.key == SDLK_UP:
                    self.y_dir += 1
                elif event.key == SDLK_DOWN:
                    self.y_dir -= 1


            elif event.type== SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.x_dir -= 1
                elif event.key == SDLK_LEFT:
                    self.x_dir += 1
                elif event.key == SDLK_UP:
                    self.y_dir -= 1
                elif event.key == SDLK_DOWN:
                    self.y_dir += 1

    def update(self):
        self.x+=self.x_dir*10
        self.y+=self.y_dir*10
        self.frame = (self.frame + 1) % 16

    def draw(self):
        self.image.clip_draw(self.frame*200,0,200,200,self.x, self.y)
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y

