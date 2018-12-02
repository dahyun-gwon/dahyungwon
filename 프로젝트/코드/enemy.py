from pico2d import *
import game_framework
import game_world
import main_state
import wisp
import tiena
import leaf_basic_attack
import water_basic_attack
import fire_basic_attack
import fire_w
import fire_e
import fire_r
import water_w
import water_r
import leaf_w
import leaf_e
from lamp_attack import Lamp_attack
from lamp_attack2 import Lamp_attack2

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
        self.state = True
        self.HP = 50
        self.damage=50
        self.Xvelocity=8
        self.z=1
        self.death_sound=load_wav('fire.wav')
        self.death_sound.set_volume(100)

    def draw(self):
        self.image.draw(self.x,self.y)
    def handle_events(self,event):
        pass



    def update(self):
        self.x -=self.Xvelocity
        if self.x < -500 or self.x > 4000:
            game_world.remove_object(self)
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == leaf_basic_attack.Leaf_basic_attack:
                    if main_state.collide(self,o):
                        self.HP-=o.damage
                        game_world.remove_object(o)
                        if main_state.tiena_HP<200:
                             main_state.tiena_HP += 20

                if type(o) == water_basic_attack.Water_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)


                if type(o) == fire_basic_attack.Fire_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)


                if type(o) == fire_w.Fire_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage

                if type(o) == fire_e.Fire_e:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_r.Fire_r:
                    if main_state.collide(self, o):
                        self.HP -= o.damage

                if type(o) == water_w.Water_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        self.Xvelocity=3
                        if o.time<0.5:
                            self.Xvelocity=5


                if type(o) == water_r.Water_r:
                    if main_state.collide(self, o):
                        self.HP -= o.damage


                if type(o) == leaf_w.Leaf_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        o.HP-=self.damage

                if type(o) == leaf_e.Leaf_e:
                    if main_state.collide(self, o):
                        for i in range(0, 100, 2):
                            t = i / 100
                            self.x = (2 * t ** 2 - 3 * t + 1) * o.x + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.x + 5 + (2 * t ** 2 - t) * o.x
                            self.y = (2 * t ** 2 - 3 * t + 1) * o.y + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.y - 5 + (2 * t ** 2 - t) * o.y
                            self.Xvelocity = 0
                        if o.time<0.5:
                            self.Xvelocity=5
        if (self.HP < 1):
            if self.z == 1:
                main_state.socre += 50
                self.death_sound.play()
                self.z = 0
                game_world.remove_object(self)




    def XYreturn(self):
        return self.x-10,self.y-25,self.x+10,self.y+25


class Lamp_enemy:
    image = None
    lamp_image=None

    def __init__(self,x,y):
        if Lamp_enemy.image == None:
            Lamp_enemy.image = load_image('lamp.png')
        if Lamp_enemy.lamp_image==None:
            Lamp_enemy.lamp_image=load_image('lamp_down.png')
        self.death_sound=load_wav('lamp.wav')
        self.death_sound.set_volume(100)
        self.collid_state=0
        self.x=x
        self.y=y
        self.state = True
        self.HP = 500
        self.damage=200
        self.Xvelocity=-5
        self.frame=0
        self.cnt=0
        self.frame2=600
        self.framecnt=0
        self.fire_w_check=0
        self.fire_r_check=0
        self.check=0
        self.z=1


    def draw(self):
        self.image.clip_draw(self.frame * 150,self.frame2, 150, 200,self.x,self.y)
        self.lamp_image.draw(self.x+20,self.y-100)

    def handle_events(self,event):
        pass
    def update(self):

        self.x += self.Xvelocity
        if self.frame==8 and self.frame2==0:
            if self.check==0:
                lamp_attack=Lamp_attack(self.x,self.y)
                lamp_attack2=Lamp_attack2(self.x,self.y)
                game_world.add_object(lamp_attack,1)
                game_world.add_object(lamp_attack2,1)
                self.check=1


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
                self.check=0



        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)

        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == leaf_basic_attack.Leaf_basic_attack:
                    if main_state.collide(self,o):
                        self.HP -= o.damage
                        game_world.remove_object(o)
                        if main_state.tiena_HP<200:
                             main_state.tiena_HP += 20
                if type(o) == water_basic_attack.Water_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_basic_attack.Fire_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_w.Fire_w:
                    if main_state.collide(self, o):
                        if self.fire_w_check==0:
                            self.fire_w_check=1
                            self.HP -= o.damage
                if type(o) == fire_e.Fire_e:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_r.Fire_r:
                    if main_state.collide(self, o):
                        if self.fire_r_check==0:
                            self.HP -= o.damage
                            self.fire_r_check=1
                if type(o) == water_w.Water_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        if self.x>800:
                            self.Xvelocity=3
                            if o.time<0.5:
                                self.Xvelocity=5

                if type(o) == water_r.Water_r:
                    if main_state.collide(self, o):
                        self.HP -= o.damage

                if type(o) == leaf_w.Leaf_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        o.HP-=self.damage

                if type(o) == leaf_e.Leaf_e:
                    if main_state.collide(self, o):
                        for i in range(0, 100, 2):
                            t = i / 100
                            self.x = (2 * t ** 2 - 3 * t + 1) * o.x + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.x + 5 + (2 * t ** 2 - t) * o.x
                            self.y = (2 * t ** 2 - 3 * t + 1) * o.y + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.y - 5 + (2 * t ** 2 - t) * o.y
                            self.Xvelocity = 0

        if (self.HP <= 0):
            if self.z==1:
                self.death_sound.play()
                main_state.socre += 1000
                self.z=0
            game_world.remove_object(self)


    def XYreturn(self):
        if self.collid_state==0:
            return 0,0,0,0
        else:
            return self.x-50,self.y-75,self.x+50,self.y+75

class Planet:
    image = None
    image50=None
    image35=None
    image10=None
    def __init__(self,x,y):
        if Planet.image == None:
            Lamp_enemy.image = load_image('planet.png')
        if Planet.image50 == None:
            Lamp_enemy.image = load_image('planet50.png')
        if Planet.image35 == None:
            Lamp_enemy.image = load_image('planet35.png')
        if Planet.image10 == None:
            Lamp_enemy.image = load_image('planet10.png')
        self.death_sound=load_wav('lamp.wav')
        self.death_sound.set_volume(100)
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
        self.fire_w_check=0
        self.fire_r_check=0
        self.check=0
        self.z=1


    def draw(self):
        self.image.clip_draw(self.frame * 150,self.frame2, 150, 200,self.x,self.y)
        self.lamp_image.draw(self.x+20,self.y-100)

    def handle_events(self,event):
        pass
    def update(self):

        self.x += self.Xvelocity
        if self.frame==8 and self.frame2==0:
            if self.check==0:
                lamp_attack=Lamp_attack(self.x,self.y)
                lamp_attack2=Lamp_attack2(self.x,self.y)
                game_world.add_object(lamp_attack,1)
                game_world.add_object(lamp_attack2,1)
                self.check=1


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
                self.check=0



        if self.x < -500 or self.x > 2500:
            game_world.remove_object(self)

        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == leaf_basic_attack.Leaf_basic_attack:
                    if main_state.collide(self,o):
                        self.HP -= o.damage
                        game_world.remove_object(o)
                        main_state.tiena_HP += 20

                if type(o) == water_basic_attack.Water_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_basic_attack.Fire_basic_attack:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_w.Fire_w:
                    if main_state.collide(self, o):
                        if self.fire_w_check==0:
                            self.fire_w_check=1
                            self.HP -= o.damage
                if type(o) == fire_e.Fire_e:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        game_world.remove_object(o)

                if type(o) == fire_r.Fire_r:
                    if main_state.collide(self, o):
                        if self.fire_r_check==0:
                            self.HP -= o.damage
                            self.fire_r_check=1
                if type(o) == water_w.Water_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        if self.x>800:
                            self.Xvelocity=3
                            if o.time<0.5:
                                self.Xvelocity=5

                if type(o) == water_r.Water_r:
                    if main_state.collide(self, o):
                        self.HP -= o.damage

                if type(o) == leaf_w.Leaf_w:
                    if main_state.collide(self, o):
                        self.HP -= o.damage
                        o.HP-=self.damage

                if type(o) == leaf_e.Leaf_e:
                    if main_state.collide(self, o):
                        for i in range(0, 100, 2):
                            t = i / 100
                            self.x = (2 * t ** 2 - 3 * t + 1) * o.x + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.x + 5 + (2 * t ** 2 - t) * o.x
                            self.y = (2 * t ** 2 - 3 * t + 1) * o.y + 5 + (
                                        -4 * t ** 2 + 4 * t) * self.y - 5 + (2 * t ** 2 - t) * o.y
                            self.Xvelocity = 0

        if (self.HP <= 0):
            if self.z==1:
                self.death_sound.play()
                main_state.socre += 1000
                self.z=0
            game_world.remove_object(self)


    def XYreturn(self):
        if self.collid_state==0:
            return 0,0,0,0
        else:
            return self.x-50,self.y-75,self.x+50,self.y+75
