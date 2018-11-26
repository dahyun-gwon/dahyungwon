import game_framework
from pico2d import *
import game_world

class Fire_w_ui:
    image = None
    def __init__(self):
        if Fire_w_ui.image == None:
            Fire_w_ui.image = load_image('fire_w_ui.png')
        self.x, self.y=100,100
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
    def handle_event(self):
        pass

class Fire_e_ui:
    image = None
    def __init__(self):
        if Fire_e_ui.image == None:
            Fire_e_ui.image = load_image('fire_e_ui.png')
        self.x, self.y=110,100
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
    def handle_event(self):
        pass

class Fire_r_ui:
    image = None
    def __init__(self):
        if Fire_r_ui.image == None:
            Fire_r_ui.image = load_image('fire_r_ui.png')
        self.x, self.y=120,100
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
    def handle_event(self):
        pass


d,f= range(2)
key_event_table = { (SDL_KEYDOWN, SDLK_d): d, (SDL_KEYDOWN, SDLK_f): f }

class Fire_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        pass


    @staticmethod
    def exit(tiena_state_ui, event):
        pass


    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        tiena_state_ui.fire_ver_state_ui_image.draw(220,715)



class Water_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        pass



    @staticmethod
    def exit(tiena_state_ui, event):
        pass


    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        tiena_state_ui.water_ver_state_ui_image.draw(0,600)

class Leaf_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        pass



    @staticmethod
    def exit(tiena_state_ui, event):
        pass


    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        tiena_state_ui.laef_ver_state_ui_image.draw(0,600)




next_state_table = {
    Fire_ver_state_ui: {d:Leaf_ver_state_ui,f:Water_ver_state_ui},
    Water_ver_state_ui: {d:Fire_ver_state_ui,f:Leaf_ver_state_ui},
    Leaf_ver_state_ui: {d:Water_ver_state_ui,f:Fire_ver_state_ui}
}

class Tiena_State_Ui:
    def __init__(self):
        global fire_w_ui
        global fire_e_ui
        global fire_r_ui
        Tiena_State_Ui.fire_ver_state_ui_image=load_image('fire_ui.png')
        Tiena_State_Ui.water_ver_state_ui_image=load_image('water_ui.png')
        Tiena_State_Ui.leaf_ver_state_ui_image=load_image('leaf_ui.png')
        self.cur_state = Fire_ver_state_ui
        self.cur_state.enter(self, None)
        self.x, self.y = 300,600
        self.event_que = []
        self.state = True;
        fire_w_ui=Fire_w_ui()
        fire_e_ui=Fire_e_ui()
        fire_r_ui=Fire_r_ui()



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

