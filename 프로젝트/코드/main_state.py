
from pico2d import *
import game_framework
import game_world

from tiena import Tiena
from wisp import Wisp

name = "MainState"

tiena = None
wisp=None

def enter():
    global tiena
    global wisp
    tiena = Tiena()
    wisp=Wisp()
    game_world.add_object(tiena, 1)
    game_world.add_object(wisp,1)


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


def update():
    for game_object in game_world.all_objects():
        game_object.update()
        delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




