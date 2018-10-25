from pico2d import *
class Universe:
    def __init__(self):
        self.image=load_image('universe.jpg')
    def draw(self):
        self.image.draw(600,400)

