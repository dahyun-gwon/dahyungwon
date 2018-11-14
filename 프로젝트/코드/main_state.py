
from pico2d import *
import game_framework
import game_world
from background import Background
from wisp import Wisp
from tiena import Tiena
from tiena_state_ui import Tiena_State_Ui
from fire_monster import Fire_Monster

name = "MainState"

fire_monster=None
wisp=None
tiena = None
fire_monsters=[]

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
    global fire_monsters
    global tiena_state_ui
    background = Background()
    wisp = Wisp()
    tiena = Tiena()
    fire_monsters = [Fire_Monster() for i in range(10)]
    tiena_state_ui=Tiena_State_Ui()
    game_world.add_object(background,0)
    game_world.add_object(wisp, 1)
    game_world.add_object(tiena, 1)
    game_world.add_object(tiena_state_ui, 1)
    game_world.add_objects(fire_monsters,1)




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
        else:
            tiena.handle_event(event)
            wisp.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for fire_monster in fire_monsters:
        if collide(tiena,fire_monster):
            fire_monsters.remove(fire_monster)
            print("collision")
    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





