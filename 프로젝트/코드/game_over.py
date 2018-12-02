import game_framework
from pico2d import *
import main_state
import title_state
import game_world


class Game_Over:
    def __init__(self):
        self.game_over_image = load_image('game_over.png')
        self.score_image=load_image('score.png')
        self.regame_image=load_image('regame.png')
        self.title_image=load_image('title_ui.png')
        self.state=True
        self.font=load_font('segoepr.ttf',55)
        self.check=0


    def draw(self):
        if self.check<240:
            self.game_over_image.draw(600,400)
        else:
            self.score_image.draw(600,400)
            self.regame_image.draw(500,300)
            self.title_image.draw(700, 300)

            self.font.draw(555, 460, '%d' % main_state.socre, (55, 55, 55))

    def update(self):
        self.check+=1

    def handle_events(self,event):
        pass

def enter():
    global game_over
    global mouse_x
    global mouse_y
    mouse_x,mouse_y=0,0
    game_over = Game_Over()

def exit():
    clear_canvas()


def handle_events():
    global mouse_x
    global mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 800 - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x, 800 - 1 - event.y
            if mouse_x >= 410 and mouse_x <= 590 and mouse_y >= 260 and mouse_y <= 340:
                main_state.socre = 0
                main_state.tiena_HP = 200
                main_state.death_time=0
                game_world.clear()
                game_framework.pop_state()
                game_framework.change_state(main_state)

            elif mouse_x >= 610 and mouse_x <= 790 and mouse_y >= 260 and mouse_y <= 340:
                main_state.socre = 0
                main_state.death_time = 0
                main_state.tiena_HP = 200
                game_world.clear()
                game_framework.pop_state()
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    game_over.draw()
    update_canvas()

def update():
    global mouse_x
    global mouse_y
    game_over.update()

def pause():
    pass

def resume():
    pass
