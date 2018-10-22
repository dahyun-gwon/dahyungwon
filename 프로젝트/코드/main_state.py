from pico2d import *
import game_framework

open_canvas(1200,800)
name = "MainState"






class Girl:
    def __init__(self):
        self.x, self.y = 200, 300
        self.image = load_image('tiena.png')
        self.x_dir,self.y_dir=0,0

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
        global G_x
        global G_y
        self.x+=self.x_dir*1
        self.y+=self.y_dir*1
        G_x=self.x
        G_y=self.y


    def draw(self):
        self.image.draw(self.x,self.y)

class Fire_Wisp:
    def __init__(self):
        self.image = load_image('fire_wisp.png')
        self.x,self.y=G_x,G_y

    def draw(self):
        self.image.draw(self.x,self.y)



class Water_Wisp:
    def __init__(self):
        self.image = load_image('Watar_wisp.png')

    def draw(self):
        self.image.draw(G_x,G_y)


class Universe:
    def __init__(self):
        self.image=load_image('universe.jpg')

    def draw(self):
        self.image.draw(600,400)

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
    girl.hanlde_events()



def update():
    girl.update()




def draw():
    universe.draw()
    girl.draw()
    fire_wisp.draw()
    water_wisp.draw()


while(True):
    clear_canvas()


    draw()
    update_canvas()

    handle_events()
    update()




