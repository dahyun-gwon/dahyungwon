
from pico2d import *
import game_framework
import game_world
from background import Background
from wisp import *
from tiena import Tiena
from tiena_state_ui import Tiena_State_Ui
from enemy import Fire_Monster
import title_state
import pause_state
from fire_basic_attack import Fire_basic_attack

name = "MainState"

fire_monster=None
tiena = None
fire_monsters=[]
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
    global wisp
    global tiena
    global background
    global tiena_state_ui
    global time
    global fire_monsters1
    fire_monsters1 = [Fire_Monster(i, j) for (i, j) in [(1200, 500), (1250, 500), (1300, 500), (1350, 500)]]
    time=State_time()
    background = Background()
    wisp = Wisp()
    tiena = Tiena()
    tiena_state_ui=Tiena_State_Ui()
    game_world.add_object(background,0)
    game_world.add_object(wisp, 1)
    game_world.add_object(tiena, 1)
    game_world.add_object(tiena_state_ui, 1)





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
            tiena.handle_event(event)
            wisp.handle_event(event)


def update():
    time.update()
    for game_object in game_world.all_objects():
        game_object.update()
    for fire_monster in fire_monsters1:
        if collide(tiena,fire_monster):
            fire_monsters1.remove(fire_monster)
            game_world.remove_object(fire_monster)
            tiena.HP-=50





    if(tiena.HP<1):
        game_world.remove_object(tiena)

    if(time.time==300):
        game_world.add_objects(fire_monsters1,1)

    if(time.time==420):
        game_world.add_objects(fire_monsters1,1)



    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





