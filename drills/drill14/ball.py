import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y=random.randint(0,1800),random.randint(0,1100)
        self.canvas_width = 23
        self.canvas_height = 23
        self.w =23
        self.h = 23

    def set_center_object(self, boy):
        self.center_object = boy
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width,self.canvas_height,
            self.x, self.y)

    def update(self):
        self.window_left = clamp(0, int( self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)


