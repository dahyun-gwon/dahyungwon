import game_framework
from pico2d import *
import main_state

image = None


def enter():
    global image
    global stage_ui
    global frame
    global cnt
    global mouse_x
    global mouse_y
    global font
    global stage_image
    mouse_x=0
    mouse_y=0
    stage_image=load_image('stage.png')
    image = load_image('stage_background.jpg')
    stage_ui=load_image('stage_ui.png')
    font = load_font('SCRIPTBL.TTF', 16)
    frame=0
    cnt=0

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
                mouse_x, mouse_y = event.x,800 - 1 - event.y
                if mouse_x>=150 and mouse_x<=250 and mouse_y>=350 and mouse_y<=450:
                    game_framework.change_state(main_state)
def update():
    global cnt
    global frame
    global mouse_x
    global mouse_y
    if (cnt > 5):
        cnt = 0
        frame += 1
    cnt += 1
    frame =frame % 10
    delay(0.01)
    print(mouse_x,mouse_y)
    if (mouse_x, mouse_y > 150, 350 and mouse_x, mouse_y < 250, 450):
        stage_ui.opacify(1)
    else:
        stage_ui.opacify(0.8)

def draw():
    clear_canvas()
    image.draw(600, 400)
    stage_image.draw(600,600)
    stage_ui.clip_draw(100*frame,0,100,100,200,400)
    font.draw(170, 320, 'STAGE 1', (255, 255, 255))
    font.draw(370, 320, 'STAGE 2', (255, 255, 255))
    font.draw(570, 320, 'STAGE 3', (255, 255, 255))
    font.draw(770, 320, 'STAGE 4', (255, 255, 255))
    font.draw(970, 320, 'STAGE 5', (255, 255, 255))

    stage_ui.clip_draw(100 * frame, 0, 100, 100, 400, 400)
    stage_ui.clip_draw(100 * frame, 0, 100, 100, 600, 400)
    stage_ui.clip_draw(100 * frame, 0, 100, 100, 800, 400)
    stage_ui.clip_draw(100 * frame, 0, 100, 100, 1000, 400)


    update_canvas()