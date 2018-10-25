from pico2d import *
import game_framework
from Fire_Wisp import fire_basic_attack
import game_world
from background import Universe
from tiena import Tiena

open_canvas(1500,800)
name = "MainState"
tiena=None
universe=None


class Water_Wisp:
    def __init__(self):
        self.image = load_image('Watar_wisp.png')
    def draw(self):
        pass






def enter():
    global tiena, universe
    tiena = Tiena()
    universe = Universe()
    game_world.add_object(universe, 0)
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


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()



