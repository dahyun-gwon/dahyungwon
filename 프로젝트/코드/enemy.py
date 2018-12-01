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
        self.damage=25
        self.Xvelocity=-5

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.XYreturn())

    def update(self):
        self.x +=self.Xvelocity
        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)
        if main_state.collide(self,main_state.tienaa):
            self.HP-=main_state.tienaa.damage
            main_state.tienaa.HP-=self.damage
        if (wisp.fire_attack):
            if main_state.collide(self,wisp.fire_attack):
                self.HP-=wisp.fire_attack.damage
                game_world.remove_object(wisp.fire_attack)
                wisp.fire_attack.x,wisp.fire_attack.y=0,0
        if (wisp.fire_w):
            if main_state.collide(self,wisp.fire_w):
                self.HP-=wisp.fire_w.damage
        if (wisp.fire_e):
            if main_state.collide(self,wisp.fire_e):
                self.HP-=wisp.fire_e.damage
                game_world.remove_object(wisp.fire_e)
                wisp.fire_e.x,wisp.fire_e.y=0,0
        if (wisp.fire_r):
            if main_state.collide(self,wisp.fire_r):
                self.HP-=wisp.fire_r.damage
        if (wisp.water_r):
            if main_state.collide(self,wisp.water_r):
                self.HP-=wisp.fire_r.damage
        if (wisp.leaf):
            if main_state.collide(self,wisp.leaf):
                self.HP-=wisp.leaf.damage
                game_world.remove_object(wisp.leaf)
                wisp.leaf.x,wisp.leaf.y=0,0
        if (wisp.water1):
            if main_state.collide(self, wisp.water1):
                self.HP -= wisp.water1.damage
                game_world.remove_object(wisp.water1)
                wisp.water1.x, wisp.water1.y = 0, 0
        if(wisp.water2):
            if main_state.collide(self, wisp.water2):
                self.HP -= wisp.water2.damage
                game_world.remove_object(wisp.water2)
                wisp.water2.x, wisp.water2.y = 0, 0
        if(wisp.water3):
            if main_state.collide(self, wisp.water3):
                self.HP -= wisp.water3.damage
                game_world.remove_object(wisp.water3)
                wisp.water3.x, wisp.water3.y = 0, 0

        if (wisp.leaf_w):
            if main_state.collide(self,wisp.leaf_w):
                self.HP-=wisp.leaf_w.damage
                wisp.leaf_w.HP-=self.damage
                if wisp.leaf_w.HP<1:
                    game_world.remove_object(wisp.leaf_w)
                    wisp.leaf_w.x,wisp.leaf_w.y=0,0
        if (wisp.leaf_e):
            if main_state.collide(self,wisp.leaf_e):
                for i in range(0, 100, 2):
                    t = i / 100
                    self.x = (2 * t ** 2 - 3 * t + 1) * wisp.leaf_e.x+5 + (-4 * t ** 2 + 4 * t) * self.x+5 + (2*t**2-t)*wisp.leaf_e.x
                    self.y = (2 * t ** 2 - 3 * t + 1) * wisp.leaf_e.y+5 + (-4 * t ** 2 + 4 * t) * self.y-5 + (2*t**2-t)*wisp.leaf_e.y
                    self.Xvelocity=0
                    print(self.x,self.y)
        if self.HP < 1:
            self.state = False
            self.x,self.y=0,0
            game_world.remove_object(self)

    def XYreturn(self):
        return self.x-10,self.y-25,self.x+10,self.y+25


class Lamp_enemy:
    image = None

    def __init__(self,x,y):
        if Lamp_enemy.image == None:
            Lamp_enemy.image = load_image('lamp.png')
        self.collid_state=0
        self.x=x
        self.y=y
        self.state = True
        self.HP = 1000
        self.damage=200
        self.Xvelocity=-5
        self.frame=0
        self.cnt=0
        self.frame2=600
        self.framecnt=0

    def draw(self):
            self.image.clip_draw(self.frame * 150,self.frame2, 150, 200,self.x,self.y)
            draw_rectangle(*self.XYreturn())

    def update(self):
        if self.state==True :
            print("살아잇음")
        elif self.state==False:
            print("죽음")
        self.x += self.Xvelocity
        if self.x==800:
            self.Xvelocity=0
            self.framecnt += 1
            if self.framecnt == 3:
                self.frame += 1
                self.framecnt = 0
                self.cnt+=1
                self.frame = self.frame % 10

            if self.cnt == 10:
                self.frame2 = 400
                self.collid_state=1
            elif self.cnt == 20:
                self.frame2 = 200
            elif self.cnt == 30:
                self.frame2 = 0
            elif self.cnt == 40:
                self.frame2 = 200
            elif self.cnt==50:
                self.frame2=800
                self.collid_state=0
            elif self.cnt == 80:
                self.frame2 = 600
                self.cnt=0



        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)
        if main_state.collide(self,main_state.tienaa):
            self.HP-=main_state.tienaa.damage
            main_state.tienaa.HP-=self.damage
        if (wisp.fire_attack):
            if main_state.collide(self,wisp.fire_attack):
                self.HP-=wisp.fire_attack.damage
                game_world.remove_object(wisp.fire_attack)
                wisp.fire_attack.x,wisp.fire_attack.y=0,0
        if (wisp.fire_w):
            if main_state.collide(self,wisp.fire_w):
                self.HP-=wisp.fire_w.damage
        if (wisp.fire_e):
            if main_state.collide(self,wisp.fire_e):
                self.HP-=wisp.fire_e.damage
                game_world.remove_object(wisp.fire_e)
                wisp.fire_e.x,wisp.fire_e.y=0,0
        if (wisp.fire_r):
            if main_state.collide(self,wisp.fire_r):
                self.HP-=wisp.fire_r.damage
        if (wisp.water_r):
            if main_state.collide(self,wisp.water_r):
                self.HP-=wisp.fire_r.damage
        if (wisp.leaf):
            if main_state.collide(self,wisp.leaf):
                self.HP-=wisp.leaf.damage
                game_world.remove_object(wisp.leaf)
                wisp.leaf.x,wisp.leaf.y=0,0
        if (wisp.water1):
            if main_state.collide(self, wisp.water1):
                self.HP -= wisp.water1.damage
                game_world.remove_object(wisp.water1)
                wisp.water1.x, wisp.water1.y = 0, 0
        if(wisp.water2):
            if main_state.collide(self, wisp.water2):
                self.HP -= wisp.water2.damage
                game_world.remove_object(wisp.water2)
                wisp.water2.x, wisp.water2.y = 0, 0
        if(wisp.water3):
            if main_state.collide(self, wisp.water3):
                self.HP -= wisp.water3.damage
                game_world.remove_object(wisp.water3)
                wisp.water3.x, wisp.water3.y = 0, 0


        if (wisp.leaf_w):
            if main_state.collide(self,wisp.leaf_w):
                self.HP-=wisp.leaf_w.damage
                wisp.leaf_w.HP-=self.damage
                if wisp.leaf_w.HP<1:
                    game_world.remove_object(wisp.leaf_w)
                    wisp.leaf_w.x,wisp.leaf_w.y=0,0
        if (wisp.leaf_e):
            if main_state.collide(self,wisp.leaf_e):
                for i in range(0, 100, 2):
                    t = i / 100
                    self.x = (2 * t ** 2 - 3 * t + 1) * wisp.leaf_e.x+5 + (-4 * t ** 2 + 4 * t) * self.x+5 + (2*t**2-t)*wisp.leaf_e.x
                    self.y = (2 * t ** 2 - 3 * t + 1) * wisp.leaf_e.y+5 + (-4 * t ** 2 + 4 * t) * self.y-5 + (2*t**2-t)*wisp.leaf_e.y
                    self.Xvelocity=0
                    print(self.x,self.y)
        if self.HP < 1:
            self.state = False
            self.x,self.y=0,0
            game_world.remove_object(self)

    def XYreturn(self):
        if self.collid_state==0:
            return 0,0,0,0
        else:
            return self.x-50,self.y-75,self.x+50,self.y+75

