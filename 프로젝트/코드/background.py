import game_framework
from pico2d import *
import game_world




class Background:
    def __init__(self):
        self.image = load_image('universe.jpg')
        self.light_image=load_image('light.png')
        self.i=0
        self.j=1
        self.state = True
        self.light_state=0






    def add_event(self, event):
        pass
    def update(self):
        if self.light_state==0:
            if (self.i<1.00):
                self.i+=0.005
            else:
                self.light_state=1
                self.i=1
        elif self.light_state==1:
            if (self.i>0.5):
                self.i-=0.005
            else:
                self.light_state=0
                self.i=0.5




    def handle_events(self,event):
        pass

    def draw(self):
        self.light_image.opacify(self.i)
        self.image.draw(600,400)
        self.light_image.draw(600,400)
