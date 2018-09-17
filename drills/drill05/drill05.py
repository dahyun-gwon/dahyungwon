from pico2d import *
import math

open_canvas()


os.chdir('D:\\2D게임프로그래밍\\2018-2DGP\\Labs\Lecture03')

grass = load_image('grass.png')
character = load_image('character.png')


while(True):
      
      x=0
      y=0
      i=0
      j=0
      z=0
      m=0
      
      while(x<750):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(0+x,90)
            x=x+2
            delay(0.01)

      while(y<450):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(0+x,90+y)
            y=y+2
            delay(0.01)
            
      while(i<750):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now((0+x-i),90)
            i=i+2
            delay(0.01)
            
      while(j<450):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now((0+x-i),(90+y-j))
            j=j+2
            delay(0.01)

      while(m<360):
           theta=math.radians(1.7)
           clear_canvas_now()
           grass.draw_now(400,30)
           character.draw_now(400+x,300+y)
           x=220*math.cos(math.radians(z))
           y=220*math.sin(math.radians(z))
           z=z+1
           delay(0.01)
           m=m+1
   

    
close_canvas()
