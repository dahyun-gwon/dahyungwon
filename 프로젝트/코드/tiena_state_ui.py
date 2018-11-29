import game_framework
from pico2d import *
import game_world
import main_state
d,f= range(2)
key_event_table = {
    (SDL_KEYDOWN,SDLK_d):d,
    (SDL_KEYDOWN, SDLK_f): f,
}

fire_skill_ui=None
fire_ui_edge=None
water_skill_ui=None
water_ui_edge=None
leaf_skill_ui=None
leaf_ui_edge=None

class Fire_skill_ui:
    image = None
    def __init__(self):
        if Fire_skill_ui.image == None:
            Fire_skill_ui.image = load_image('fire_skill_ui.png')
        self.x, self.y=600,400
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
        print(self.state)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d :
                self.state = False
                print('된다')
            elif event.type == SDL_KEYDOWN and  event.key == f :
                self.state = False

class Fire_edge_ui:
    image=None
    def __init__(self):
        if Fire_edge_ui.image==None:
            Fire_edge_ui.image=load_image('fire_edge_ui.png')
        self.x,self.y=600,400
        self.state=True
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d :
                game_world.remove_object(self)
                self.state = False
            elif event.type == SDL_KEYDOWN and  event.key == f :
                game_world.remove_object(self)
                self.state = False

class Water_skill_ui:
    image = None
    def __init__(self):
        if Water_skill_ui.image == None:
            Water_skill_ui.image = load_image('water_skill_ui.png')
        self.x, self.y=600,400
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d :
                game_world.remove_object(self)
                self.state = False
            elif event.type == SDL_KEYDOWN and  event.key == f :
                game_world.remove_object(self)
                self.state = False

class Water_edge_ui:
    image=None
    def __init__(self):
        if Water_edge_ui.image==None:
            Water_edge_ui.image=load_image('water_edge_ui.png')
        self.x,self.y=600,400
        self.state=True
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d :
                game_world.remove_object(self)
                self.state = False
            elif event.type == SDL_KEYDOWN and  event.key == f :
                game_world.remove_object(self)
                self.state = False

class Leaf_skill_ui:
    image = None
    def __init__(self):
        if Leaf_skill_ui.image == None:
            Leaf_skill_ui.image = load_image('leaf_skill_ui.png')
        self.x, self.y=600,400
        self.state = True
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d :
                game_world.remove_object(self)
                self.state = False
            elif event.type == SDL_KEYDOWN and  event.key == f :
                game_world.remove_object(self)
                self.state = False

class Leaf_edge_ui:
    image=None
    def __init__(self):
        if Leaf_edge_ui.image==None:
            Leaf_edge_ui.image=load_image('leaf_ui_edge.png')
        self.x,self.y=600,400
        self.state=True
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if self.state==False:
            game_world.remove_object(self)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and  event.key == d:
                game_world.remove_object(self)
                self.state = False
            elif event.type == SDL_KEYDOWN and  event.key == f:
                game_world.remove_object(self)
                self.state = False

d,f= range(2)
key_event_table = { (SDL_KEYDOWN, SDLK_d): d, (SDL_KEYDOWN, SDLK_f): f }

class Fire_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        tiena_state_ui.fire_skill_ui()
        tiena_state_ui.fire_ui_edge()


    @staticmethod
    def exit(tiena_state_ui, event):
        game_world.remove_object(tiena_state_ui.fire_ui_edge)




    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        pass



class Water_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        tiena_state_ui.water_skill_ui()
        tiena_state_ui.water_ui_edge()



    @staticmethod
    def exit(tiena_state_ui, event):
        pass


    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        pass

class Leaf_ver_state_ui:
    @staticmethod
    def enter(tiena_state_ui, event):
        tiena_state_ui.leaf_skill_ui()
        tiena_state_ui.leaf_ui_edge()



    @staticmethod
    def exit(tiena_state_ui, event):
        pass



    @staticmethod
    def do(tiena_state_ui):
        pass


    @staticmethod
    def draw(tiena_state_ui):
        pass




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

    def fire_skill_ui(self):
        global fire_skill_ui
        fire_skill_ui = Fire_skill_ui()
        game_world.add_object(fire_skill_ui, 2)

    def fire_ui_edge(self):
        global fire_ui_edge
        fire_ui_edge=Fire_edge_ui()
        game_world.add_object(fire_ui_edge,4)

    def water_skill_ui(self):
        global water_skill_ui
        water_skill_ui=Water_skill_ui()
        game_world.add_object(water_skill_ui, 2)

    def water_ui_edge(self):
        global water_ui_edge
        water_ui_edge=Water_edge_ui()
        game_world.add_object(water_ui_edge, 4)

    def leaf_skill_ui(self):
        global leaf_skill_ui
        leaf_skill_ui=Leaf_skill_ui()
        game_world.add_object(leaf_skill_ui, 2)

    def leaf_ui_edge(self):
        global leaf_ui_edge
        leaf_ui_edge=Leaf_edge_ui()
        game_world.add_object(leaf_ui_edge,4)

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
        self.image.clip_draw(0,-(200-main_state.tienaa.HP),200,200,100,700-(200-main_state.tienaa.HP)//2,200,200-(200-main_state.tienaa.HP))
    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

