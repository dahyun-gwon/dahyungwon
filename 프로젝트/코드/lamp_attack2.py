from pico2d import *
import game_world
import main_state
import leaf_w
import tiena
class Lamp_attack2:
    image = None
    image2=None


    def __init__(self, x ,y ):
        if Lamp_attack2.image == None:
            Lamp_attack2.image = load_image('lamp_attack.png')
        if Lamp_attack2.image2==None:
            Lamp_attack2.image2=load_image('lamp_attack2.png')
        self.x, self.y=x, y
        self.Xvelocity=7
        self.Yvelocity=2
        self.damage=100
        self.state = True
        self.frame=0
        self.frame2=0
        self.cnt=0
        self.cnt2=0
        self.XYplus=7.5

    def draw(self):

        if self.frame<10:
            self.image.clip_draw(self.frame*150,0,150,150,self.x,self.y)
        else:
            self.image2.clip_draw(self.frame2*150,0,150,150,self.x,self.y)


    def update(self):
        self.x -= self.Xvelocity
        self.y-=self.Yvelocity
        self.cnt+=1
        if self.frame<10:
            if self.cnt==3:
                self.cnt=0
                self.frame+=1
                self.XYplus += 5
        else:
            self.cnt2+=1
            if self.cnt2==5:
                self.cnt2=0
                self.frame2+=1
        for i in range(len(game_world.objects)):
            for o in game_world.objects[i]:
                if type(o) == leaf_w.Leaf_w:
                    if main_state.collide(self,o):
                        game_world.remove_object(self)
                if type(o) == tiena.Tiena:
                    if main_state.collide(self,o):
                        game_world.remove_object(self)
                        main_state.tiena_HP -= 100
        self.frame2=self.frame2%4
        if self.x < 0 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x - 14-self.XYplus, self.y - 14-self.XYplus, self.x + 14+self.XYplus, self.y + 14+self.XYplus
