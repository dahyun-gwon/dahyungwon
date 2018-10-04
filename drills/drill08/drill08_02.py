from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
m = 100
x = 25
y = 50


def move_to_point(p1, p2):
    global x, y, frame, motion

    for i in range(0, 50 + 1, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1]
        clear_canvas()

        if p1[0] > p2[0]:
            m = 0
        else:
            m = 100

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, m, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


i = 0

points = [(random.randint(0 + 50, KPU_WIDTH - 50), random.randint(0 + 50, KPU_HEIGHT - 50)) for i in range(10)]

while True:
    move_to_point(points[i - 1], points[i])


    i = (i + 1) % 10

close_canvas()