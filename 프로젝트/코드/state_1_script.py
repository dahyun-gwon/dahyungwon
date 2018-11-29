import game_framework
from pico2d import *
import main_state
import title_state
image = None

class State_1_Script:
    def __init__(self):
        self.image = load_image('bastup.png')


    def draw(self):
        self.image.draw(600,400)

    def update(self):
        pass

def enter():
    global image
    image = State_1_Script()

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(title_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
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
