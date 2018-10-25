from pico2d import *
import game_framework

open_canvas(1500,800)
name = "MainState"
x = 0
y = 0

class Girl:

    def __init__(self):
        self.image = load_image('tiena_sprite.png')
        self.x_dir,self.y_dir=0,0
        self.x = 500
        self.y = 500
        self.frame=0


    def hanlde_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.x_dir += 1
                elif event.key == SDLK_LEFT:
                    self.x_dir -= 1
                elif event.key == SDLK_UP:
                    self.y_dir += 1
                elif event.key == SDLK_DOWN:
                    self.y_dir -= 1


            elif event.type== SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.x_dir -= 1
                elif event.key == SDLK_LEFT:
                    self.x_dir += 1
                elif event.key == SDLK_UP:
                    self.y_dir -= 1
                elif event.key == SDLK_DOWN:
                    self.y_dir += 1

    def update(self):
        self.x+=self.x_dir*5
        self.y+=self.y_dir*5
        self.frame = (self.frame + 1) % 16

    def draw(self):
        self.image.clip_draw(self.frame*200,0,200,200,self.x, self.y)
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y


class Basic_Missile:
    def __init__(self):
        self.image = load_image('basic.png')
        self.x = girl.returnX() + 25
        self.y = girl.returnY()
    def hanlde_events(self):
        pass
    def update(self):
        self.x +=12
    def draw(self):
        self.image.draw(self.x, self.y)

class Fire_Wisp:
    def __init__(self):
        self.image = load_image('fire_wisp.png')
        self.x = girl.returnX()-30
        self.y = girl.returnY()+50
    def hanlde_events(self):
        pass
    def update(self):
        self.x=girl.returnX()-30
        self.y=girl.returnY()+50
    def draw(self):
        self.image.draw(self.x, self.y)

class Water_Wisp:
    def __init__(self):
        self.image = load_image('Watar_wisp.png')
    def draw(self):
        pass

class Universe:
    def __init__(self):
        self.image=load_image('universe.jpg')
    def draw(self):
        self.image.draw(600,400)

universe=Universe()
girl=Girl()
fire=Fire_Wisp()


def enter():
    pass
def exit():
    pass
def pause():
    pass
def resume():
    pass
def handle_events():
    girl.hanlde_events()


def update():
    girl.update()
    fire.update()


def draw():
    universe.draw()
    girl.draw()
    fire.draw()



while(True):

    clear_canvas()
    draw()
    handle_events()
    update_canvas()
    update()
    delay(0.05)




