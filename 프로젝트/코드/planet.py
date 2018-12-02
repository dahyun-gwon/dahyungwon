from pico2d import *
import random
import game_world
import main_state
import leaf_w



PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Planet:
    image = None
    image50=None
    image35=None
    image10=None
    def __init__(self,x,y):
        if Planet.image == None:
            Planet.image = load_image('planet.png')
        if Planet.image50 == None:
            Planet.image50 = load_image('planet50.png')
        if Planet.image35 == None:
            Planet.image35 = load_image('planet35.png')
        if Planet.image10 == None:
            Planet.image10 = load_image('planet10.png')
        self.x=x
        self.y=y
        self.state = True
        self.HP = 2000
        self.damage=100
        self.Xvelocity=0
        self.Yeolocity=10

    def draw(self):
        self.image.draw(self.x,self.y+1000)
        self.image10.draw(random.randint(self.x-30,self.x+30),random.randint(self.y-100,self.y+100))
        self.image10.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image10.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image10.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image10.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image10.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image50.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image35.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image35.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))
        self.image35.draw(random.randint(self.x - 30, self.x + 30), random.randint(self.y - 300, self.y + 300))

    def update(self):
        self.y-=self.Yeolocity
        if self.y<-3000:
            game_world.remove_object(self)
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == leaf_w.Leaf_w:
                    if main_state.collide(self, o):
                        game_world.remove_object(self)
                        o.HP-=self.damage




    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x-90,self.y-90+1000,self.x+90,self.y+90+1000
