from pico2d import *
import game_framework
import game_world
from background import Background
from wisp import Wisp
from tiena import Tiena
import state_1_script
import wisp
from tiena_state_ui import Tiena_State_Ui
from enemy import Fire_Monster
from enemy import Lamp_enemy
import title_state
import state_1_script
import pause_state
import tiena_state_ui

fire_monster=None
fire_monsters1=[]
lamp_enemy1=None
tienaa=None
wispp=None
background=None
class State_time:
    def __init__(self):
        self.time=60
        self.x,self.y=600,450
        self.image=load_image('start.png')
        self.opacity=0.8

    def update(self):
        self.image.opacify(self.opacity)
        self.time+=1
        if self.y>400:
            self.y-=0.1
            self.opacity+=0.02
        if self.time>120:
            self.x,self.y=0,1500
    def draw(self):
        self.image.draw(self.x,self.y)

def collide(a,b):
    a_left,a_bottom,a_right,a_top=a.XYreturn()
    b_left,b_bottom,b_right,b_top=b.XYreturn()
    if a_left>b_right:return False
    if a_right<b_left:return False
    if a_top<b_bottom:return False
    if a_bottom>b_top:return False
    return True
def enter():
    global wispp
    global tienaa
    global background
    global tiena_state_ui
    global time
    global fire_monsters1
    global fire_monsters2
    global skill_ui
    global lamp_enemy1
    game_framework.push_state(state_1_script)
    skill_ui=Tiena_State_Ui()
    tienaa=Tiena()
    lamp_enemy1=Lamp_enemy(1200,500)
    fire_monsters1 = [Fire_Monster(i, j) for (i, j) in [(1200, 500), (1250, 500), (1300, 500), (1350, 500)]]
    fire_monsters2 = [Fire_Monster(i, j) for (i, j) in [(1200, 200), (1250, 200), (1300, 200), (1350, 200)]]
    time=State_time()
    background = Background()
    wispp = Wisp()
    tiena_state_ui=Tiena_State_Ui()
    game_world.add_object(background,0)
    game_world.add_object(wispp, 1)
    game_world.add_object(tiena_state_ui, 1)
    game_world.add_object(tienaa, 1)
    fire_monster=Fire_Monster(0,0)


def exit():
    game_world.clear()
def pause():
    pass
def resume():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            tienaa.handle_event(event)
            wispp.handle_event(event)
            tiena_state_ui.handle_event(event)


def update():
    time.update()
    if (time.time==120):
        game_world.add_object(lamp_enemy1, 1)
    if(time.time==300):
        game_world.add_objects(fire_monsters1,2)
    if(time.time==480):
        game_world.add_objects(fire_monsters2,2)
    for game_object in game_world.all_objects():
        game_object.update()
        if not game_object.state:
            game_world.remove_object(game_object)

    delay(0.01)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    time.draw()
    update_canvas()





