from pico2d import *

open_canvas()


os.chdir('D:\\2D게임프로그래밍\\2018-2DGP\\Labs\Lecture03')

grass = load_image('grass.png')
character = load_image('character.png')
x=0
while(x<800):
      clear_canvas_now()
      grass.draw_now(400,30)
      character.draw_now(x,90)
      x=x+2
      delay(0.01)
    
close_canvas()
