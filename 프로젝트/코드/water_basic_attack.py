from pico2d import *
import game_world

class Water_basic_attack:
    image = None

    def __init__(self, x = 400, y = 300, Xvelocity = 1):
        if Water_basic_attack.image == None:
            Water_basic_attack.image = load_image('water_basic_attack.png')
        self.x, self.y,self.up_y,self.down_y, self.Xvelocity = x, y,y+10,y-10, Xvelocity

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x, self.up_y)
        self.image.draw(self.x, self.down_y)

    def update(self):
        self.x += self.Xvelocity*3
        self.up_y+=1
        self.down_y-=1

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
