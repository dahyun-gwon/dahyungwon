from pico2d import *
import game_framework
import game_world
from background import Background
from wisp import Wisp
from tiena import Tiena
import wisp
from tiena_state_ui import Tiena_State_Ui
from enemy import Fire_Monster
import title_state
import pause_state


fire_monster=None
fire_monsters1=[]

tienaa=None
class State_time:
    def __init__(self):
        self.time=60
    def update(self):
        self.time+=1

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

    tienaa=Tiena()
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            tienaa.handle_event(event)
            wispp.handle_event(event)


def update():
    time.update()

    if(time.time==300):
        game_world.add_objects(fire_monsters1,1)
    elif(time.time==480):
        game_world.add_objects(fire_monsters2,1)


    for game_object in game_world.all_objects():
        game_object.update()


        if not game_object.state:
            game_world.remove_object(game_object)

    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





