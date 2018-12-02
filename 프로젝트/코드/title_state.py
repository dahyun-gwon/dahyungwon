import game_framework
from pico2d import *
import stage_state
import main_state
name = "TitleState"
image = None

def enter():
    global BGM
    global image
    image = load_image('title_state.jpg')
    BGM = load_music('background2.mp3')
    BGM.set_volume(80)
    BGM.repeat_play()


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    global mouse_x
    global mouse_y
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_MOUSEMOTION:
            mouse_x=event.x
            mouse_y=799-event.y

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_MOUSEMOTION:
                mouse_x, mouse_y = event.x, 800 - 1 - event.y

            elif event.type == SDL_MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.x, 800-1-event.y
                print(mouse_x,mouse_y)
                if mouse_x>=566 and mouse_x<=707 and mouse_y>=175 and mouse_y<=216:
                    game_framework.change_state(main_state)
                elif mouse_x>=583 and mouse_x<=687 and mouse_y>=36 and mouse_y<=75:
                    game_framework.quit()
                elif mouse_x >= 552 and mouse_x <= 724 and mouse_y >= 109 and mouse_y <= 149:
                    pass

def draw():
    clear_canvas()
    image.draw(600, 400)
    update_canvas()















def update():

    pass





def pause():

    pass





def resume():

    pass
