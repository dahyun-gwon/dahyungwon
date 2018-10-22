from pico2d import *

2

3
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
4

5  # 최종완성
6

7


def handle_events():
    8
    global mx, my  # 마우스 좌표


9
global gx, gy  # 클릭한 좌표 ( 캐릭터가 도착해야하는 좌표 )
10
global sx, sy  # 시작 좌표 ( 캐릭터의 시작 좌표 )
11
global x, y  # 현재 캐릭터의 좌표
12
global click
13
global count
14
global running
15

16
events = get_events()
17
18
for event in events:
    19
    if event.type == SDL_MOUSEBUTTONDOWN:
        20
    gx, gy = event.x, KPU_HEIGHT - 1 - event.y
21
sx, sy = x, y
22
count = 30
23
click = True
24 elif event.type == SDL_MOUSEMOTION:
25
mx, my = event.x, KPU_HEIGHT - 1 - event.y
26 elif event.type == SDL_KEYDOWN:
27
if event.key == SDLK_ESCAPE:
    28
    running = False
29 elif event.type == SDL_QUIT:
30
running = False
31

32
open_canvas(KPU_WIDTH, KPU_HEIGHT)
33

34
MouseIcon = load_image('hand_arrow.png')
35
kpu_ground = load_image('KPU_GROUND.png')
36
character = load_image('animation_sheet.png')
37

38
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

running = True

click = False

mx, my = 0, 0

gx, gy = 0, 0

sx, sy = 0, 0

count = 30
direc = 1

frame = 0

hide_cursor()





while running:

    clear_canvas()

kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)



if click == True:



if gx - sx > 0:

    direc = 1
elif gx - sx < 0:

direc = -1

x += (gx - sx) / 30

y += (gy - sy) / 30

count -= 1

if count == 0:

    click = False



if direc == 1:

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
elif direc == -1:

character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

MouseIcon.draw(mx + 25, my - 25)

frame = (frame + 1) % 8


update_canvas()



delay(0.02)

handle_events()


close_canvas()
