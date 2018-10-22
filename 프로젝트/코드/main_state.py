from pico2d import *
import game_framework

open_canvas()
name = "MainState"




class Fire_Wisp:
    def __init__(self):
        self.image = load_image('fire_wisp.png')
        self.x,self.y=200-50,400+10
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        events = get_events()
        for event in events:
            if event.key == SDLK_RIGHT:
                self.x = self.x + 10
            elif event.key == SDLK_LEFT:
                self.x = self.x - 10
            elif event.key==SDLK_UP:
                self.y=self.y+10
            elif event.key==SDLK_DOWN:
                self.y=self.y-10

class Water_Wisp:
    def __init__(self):
        self.image = load_image('Watar_wisp.png')
        self.x,self.y=200-50,400+10
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        events = get_events()
        for event in events:
            if event.key == SDLK_RIGHT:
                self.x = self.x + 10
            elif event.key == SDLK_LEFT:
                self.x = self.x - 10
            elif event.key==SDLK_UP:
                self.y=self.y+10
            elif event.key==SDLK_DOWN:
                self.y=self.y-10

class Universe:
    def __init__(self):
        self.image=load_image('universe.jpg')
        self.x,self.y=600,400
    def draw(self):
        self.image.draw(self.x,self.y)


class Girl:
    def __init__(self):
        self.x, self.y = 200, 600
        self.image = load_image('tiena.png')


    def update(self):
        events = get_events()
        for event in events:
            if event.key == SDLK_RIGHT:
                self.x = self.x + 10
            elif event.key == SDLK_LEFT:
                self.x = self.x - 10
            elif event.key==SDLK_UP:
                self.y=self.y+10
            elif event.key==SDLK_DOWN:
                self.y=self.y-10

    def draw(self):
        self.image.draw(self.x,self.y)


universe=Universe()
girl=Girl()
fire_wisp=Fire_Wisp()
water_wisp=Water_Wisp()

def enter():
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    girl.update()
    fire_wisp.update()
    water_wisp.update()


def draw():
    universe.draw()
    girl.draw()
    fire_wisp.draw()
    water_wisp.draw()


while(True):
    handle_events()
    clear_canvas()

    update()
    draw()

    update_canvas()

