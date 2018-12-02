from pico2d import *
import game_world

class Water_basic_attack:
    image = None

    def __init__(self, x , y ,Xvelocity, Yvelocity):
        if Water_basic_attack.image== None:
            Water_basic_attack.image = load_image('water_basic_attack.png')
        self.x, self.y = x, y
        self.state=True
        self.damage=50
        self.Xvelocity=Xvelocity
        self.Yvelocity=Yvelocity



    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity
        self.y+=self.Yvelocity

        if self.x < 0 or self.x > 1600 - 25:
            game_world.remove_object(self)
    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x-15,self.y-15,self.x+15,self.y+15

