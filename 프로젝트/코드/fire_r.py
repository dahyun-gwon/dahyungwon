from pico2d import *
import game_world

class Fire_r:
    image = None

    def __init__(self, x = 400, y = 300, Xvelocity = 1):
        if Fire_r.image == None:
            Fire_r.image = load_image('fire_r.png')
        self.x, self.y, self.Xvelocity = x, y, Xvelocity
        self.state = True
        self.damage=100

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.XYreturn())

    def update(self):
        self.x += self.Xvelocity*8
        if self.x < 0 or self.x > 1300:
            game_world.remove_object(self)
    def handle_events(self,event):
        pass
    def XYreturn(self):
        return self.x - 130, self.y - 400, self.x + 130, self.y + 400
