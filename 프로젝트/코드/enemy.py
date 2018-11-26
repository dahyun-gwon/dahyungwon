from pico2d import *
import game_framework
import game_world
import main_state
import wisp

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Fire_Monster:
    image = None

    def __init__(self,x,y):
        if Fire_Monster.image == None:
            Fire_Monster.image = load_image('bomp.png')
        self.x=x
        self.y=y
        self.state = True;
        self.HP = 20
        self.damage=50

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.XYreturn())

    def update(self):
        self.x -= 5
        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)

        if main_state.collide(self,main_state.tienaa):
            self.HP-=main_state.tienaa.damage
            main_state.tienaa.HP-=self.damage
        elif (wisp.fire_attack):
            if main_state.collide(self,wisp.fire_attack):
                self.HP-=wisp.fire_attack.damage
                game_world.remove_object(wisp.fire_attack)
                wisp.fire_attack.x,wisp.fire_attack.y=0,0
        elif (wisp.fire_w):
            if main_state.collide(self,wisp.fire_w):
                self.HP-=wisp.fire_w.damage
        elif (wisp.fire_e):
            if main_state.collide(self,wisp.fire_e):
                self.HP-=wisp.fire_e.damage
                game_world.remove_object(wisp.fire_e)
                wisp.fire_e.x,wisp.fire_e.y=0,0
        elif (wisp.fire_r):
            if main_state.collide(self,wisp.fire_r):
                self.HP-=wisp.fire_r.damage
                print("외안대")
        elif (wisp.water):
            if main_state.collide(self,wisp.water):
                self.HP-=wisp.water.damage
                game_world.remove_object(wisp.water)
                wisp.water.x,wisp.water.y=0,0
        elif (wisp.water_r):
            if main_state.collide(self,wisp.water_r):
                self.HP-=wisp.fire_r.damage
        elif (wisp.leaf):
            if main_state.collide(self,wisp.leaf):
                self.HP-=wisp.leaf.damage
                game_world.remove_object(wisp.leaf)
                wisp.leaf.x,wisp.leaf.y=0,0



        if self.HP < 1:
            self.state = False
            self.x,self.y=0,0
            game_world.remove_object(self)



    def XYreturn(self):
        return self.x-10,self.y-25,self.x+10,self.y+25



