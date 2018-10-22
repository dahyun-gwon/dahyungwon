from pico2d import *
import random

# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y=random.randint(0,200),90
        self.frame=random.randint(0,7)
        self.image= load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x +=0.5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):
        self.x,self.y=400,30
        self.image=load_image('grass.png')


    def draw(self):
        self.image.draw(self.x,self.y)

class SBall:
    def __init__(self):
        self.x,self.y=random.randint(0,1200),800
        self.Ball=random.randint(0,1)
        if self.Ball==1:
            self.image=load_image('ball21x21.png')

        else:
            self.image=load_image('ball41x41.png')

    def update(self):
        if(self.y>70):
            self.y-=random.randint(1,4)

    def draw(self):
        self.image.draw(self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


open_canvas()
grass=Grass()
team=[Boy() for i in range(11)]
running=True
balls=[SBall() for i in range(20)]
# game main loop code

while(True):
    handle_events()
    clear_canvas()

    grass.draw()
    for boy in team:
        boy.update()

        boy.draw()

    for ball in balls:
        ball.update()
        ball.draw()


    update_canvas()

delay(0.05)
# finalization code