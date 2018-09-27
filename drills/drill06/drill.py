from pico2d import *
KPU_WIDTH,KPU_HEIGHT=1280,1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)
os.chdir('D:\\2D게임프로그래밍\\제출\\2016180047\\drills\\drill06')


grass=load_image('grass.png')
boy=load_image('animation_sheet.png')
mouse=load_image('hand_arrow.png')
ground=load_image('KPU_GROUND.png')


def cursor():
    global x, y
    global go_x,go_y

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN:
            if event.key==SDL_MOUSEBUTTONDOWN:
                if event.botton==SDL_BUTTON_LEFT:
                    go_x,go_y=event.x,event,y



hide_cursor()
frame=0
while(True):
    clear_canvas()
    ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor()
    mouse.draw(x, y)
    boy.clip_draw(100,0,100,100,go_x,go_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)