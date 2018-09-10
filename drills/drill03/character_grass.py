from pico2d import *

open_canvas()
os.chdir('D:\\2D게임프로그래밍\\2018-2DGP\\Labs\\Lecture04')

image=load_image('grass.png')
image.draw_now(400,30)

delay(5)

close_canvas()
