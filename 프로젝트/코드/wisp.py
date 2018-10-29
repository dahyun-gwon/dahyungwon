from pico2d import*

from tiena import Tiena

class Fire_Wisp:
    image=None
    def __init__(self):
        if Fire_Wisp.image == None:
            Fire_Wisp.image = load_image('fire_wisp.png')
        self.x, self.y,self.Xvelocity,self.Yvelocity = Tiena.x, Tiena.y, Tiena.Xvelocity, Tiena.Yvelocity

    def draw(self):
        self.image.draw(self.x-100, self.y+100)

    def update(self):
        self.x += self.Xvelocity
        self.y += self.Xvelocity

class Water_Wisp:
    image=None
    def __init__(self):
        if Water_Wisp.image == None:
            Water_Wisp.image = load_image('fire_wisp.png')
        self.x, self.y, self.Xvelocity, self.Yvelocity = Tiena.x, Tiena.y, Tiena.Xvelocity, Tiena.Yvelocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity
        self.y += self.Xvelocity

class Leaf_Wisp:
    image=None
    def __init__(self, x, y,Xvelocity,Yvelocity):
        if Fire_Wisp.image == None:
            Fire_Wisp.image = load_image('fire_wisp.png')
        self.x, self.y, self.Xvelocity, self.Yvelocity = Tiena.x, Tiena.y, Tiena.Xvelocity, Tiena.Yvelocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.Xvelocity
        self.y += self.Xvelocity



