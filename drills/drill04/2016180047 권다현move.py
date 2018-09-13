from pico2d import *
os.chdir('D:\\2D게임프로그래밍\\제출\\2016180047\\drills\\drill04')

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
true=1
x = 0
y=0
frame=0
while (true):

      while(x<800):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame*100,100,100,100,x,90)
            update_canvas()
            frame=(frame+1)%8
            x+=10
            delay(0.05)
            get_events()

      while(y<800):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame*100,0,100,100,800-y,90)
            update_canvas()
            frame=(frame+1)%8
            y+=10
            delay(0.05)
            get_events()
            
      x=0
      y=0

    
close_canvas()
