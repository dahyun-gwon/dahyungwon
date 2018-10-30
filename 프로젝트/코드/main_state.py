
from pico2d import *
import game_framework
import game_world

from wisp import Wisp
from tiena import Tiena


name = "MainState"

wisp=None
tiena = None

def enter():
    global wisp
    global tiena
    wisp = Wisp()
    tiena = Tiena()
    game_world.add_object(wisp, 1)
    game_world.add_object(tiena, 1)


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
        delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




