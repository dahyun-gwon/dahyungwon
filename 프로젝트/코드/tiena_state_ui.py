import game_framework
from pico2d import *
import game_world
import tiena
import main_state
d,f= range(2)
key_event_table = {
    (SDL_KEYDOWN,SDLK_d):d,
    (SDL_KEYDOWN, SDLK_f): f,
}


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
        tiena_state_ui.fire_skill_ui_image.draw(600,400)
        tiena_state_ui.fire_ui_edge_image.draw(600,400)




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
        tiena_state_ui.water_skill_ui_image.draw(600,400)
        tiena_state_ui.water_ui_edge_image.draw(600,400)


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
        tiena_state_ui.leaf_skill_ui_image.draw(600,400)
        tiena_state_ui.leaf_ui_edge_image.draw(600,400)




next_state_table = {
    Fire_ver_state_ui: {d:Leaf_ver_state_ui,f:Water_ver_state_ui},
    Water_ver_state_ui: {d:Fire_ver_state_ui,f:Leaf_ver_state_ui},
    Leaf_ver_state_ui: {d:Water_ver_state_ui,f:Fire_ver_state_ui}
}

class Tiena_State_Ui:
    def __init__(self):

        global fire_skill_ui
        global fire_ui_edge
        global water_skill_ui
        global water_ui_edge
        global leaf_skill_ui
        global leaf_ui_edge
        self.cur_state = Fire_ver_state_ui
        self.cur_state.enter(self, None)
        self.x, self.y = 300,600
        self.event_que = []
        self.hp=200
        self.state = True
        self.image=load_image('tiena_hp.png')
        self.fire_ui_edge_image=load_image('fire_edge_ui.png')
        self.fire_skill_ui_image=load_image('fire_skill_ui.png')
        self.water_ui_edge_image=load_image('water_edge_ui.png')
        self.water_skill_ui_image=load_image('water_skill_ui.png')
        self.leaf_ui_edge_image=load_image('leaf_ui_edge.png')
        self.leaf_skill_ui_image=load_image('leaf_skill_ui.png')


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
        for o in game_world.objects[2]:
            if type(o) == tiena.Tiena:
                self.image.clip_draw(0, -(200 - main_state.tiena_HP), 200, 200, 100, 700 - (200 - main_state.tiena_HP) // 2,
                                     200, 200 - (200 - main_state.tiena_HP))
                self.cur_state.draw(self)

    def handle_events(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

