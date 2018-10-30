from pico2d import*
import game_framework
import game_world
import tiena
d, f= range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): d,
    (SDL_KEYDOWN, SDLK_f): f
}

class Fire_Wisp:
    @staticmethod
    def enter(tiena, event):
        pass

    @staticmethod
    def exit(tiena, event):
        pass

    @staticmethod
    def do(wisp):
        wisp.x+=0.1



    @staticmethod
    def draw(wisp):
        wisp.image.draw(500,500)

class Water_Wisp:
    @staticmethod
    def enter(tiena, event):
        pass

    @staticmethod
    def exit(tiena, event):
        pass

    @staticmethod
    def do(wisp):
        wisp.x+=0.1

    @staticmethod
    def draw(wisp):
        wisp.image.draw(500,500)

class Leaf_Wisp:
    @staticmethod
    def enter(tiena, event):
        pass

    @staticmethod
    def exit(tiena, event):
        pass

    @staticmethod
    def do(wisp):
        wisp.x+=0.1



    @staticmethod
    def draw(wisp):
        wisp.image.draw(500,500)

next_state_table = {
        Fire_Wisp: {d:Leaf_Wisp,f:Water_Wisp},
        Water_Wisp: {d:Fire_Wisp,f:Leaf_Wisp},
        Leaf_Wisp:{d:Water_Wisp,f:Fire_Wisp}
    }

class Wisp:
    image=None
    def __init__(self):
        if Wisp.image == None:
            Wisp.image = load_image('fire_wisp.png')
        self.x, self.y = 200,200
        self.event_que = []
        self.cur_state = Fire_Wisp
        self.cur_state.enter(self, None)

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


