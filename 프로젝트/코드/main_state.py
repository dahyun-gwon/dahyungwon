from pico2d import *
import game_framework
from tiena import Tiena
from fire_wisp import Fire_Wisp
open_canvas(1500,800)
name = "MainState"
x = 0
y = 0






tiena=Tiena()
tiena=None
class Universe:
    def __init__(self):
        self.image=load_image('universe.jpg')
    def draw(self):
        self.image.draw(600,400)

universe=Universe()
tiena=Tiena()
fire_wifp=Fire_Wisp()


def enter():
    global tiena
    tiena=Tiena()


def exit():
    global tiena
    del tiena
def pause():
    pass
def resume():
    pass
def handle_events():
    tiena.hanlde_events()


def update():
    tiena.update()
    fire.update()


def draw():
    clear_canvas()
    universe.draw()
    tiena.draw()
    fire.draw()
    update_canvas()







