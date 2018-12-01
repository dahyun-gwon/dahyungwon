import game_framework
from pico2d import *
import main_state
import title_state
import game_world
image = None

class State_1_Script:
    def __init__(self):
        self.image = load_image('bastup.png')
        self.script_image=load_image('1.png')
        self.cnt=1
        self.state=True


    def draw(self):
        self.image.draw(600,400)
        self.script_image.draw(600,400)

    def update(self):
        pass



def enter():
    global image
    image = State_1_Script()
    game_world.add_object(image,1)

def exit():
    game_world.remove_object(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(title_state)
        if (image.cnt == 1 and event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            image.script_image = load_image('2.png')
            image.cnt =2
            print(image.cnt)
        elif (image.cnt == 2 and event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            image.script_image = load_image('3.png')
            image.cnt =3
            print(image.cnt)
        elif (image.cnt == 3 and event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            image.script_image = load_image('4.png')
            image.cnt =4
        elif (image.cnt == 4 and event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            image.script_image = load_image('5.png')
            image.cnt=5
        elif (image.cnt == 5 and event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.pop_state()





def draw():
    clear_canvas()
    main_state.tienaa.draw()
    main_state.wispp.draw()
    main_state.background.draw()
    image.draw()
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
