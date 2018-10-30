import game_framework
from pico2d import *
import game_world




class Background:
    def __init__(self):
        self.image = load_image('universe.jpg')





    def add_event(self, event):
        pass
    def update(self):
        pass


    def handle_event(self,event):
        pass

    def draw(self):
        self.image.draw(600,400)
