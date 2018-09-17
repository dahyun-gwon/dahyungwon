from pico2d import *

open_canvas()
os.chdir('D:\\2D게임프로그래밍\\2018-2DGP\\Labs\Lecture05')

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_203_535():
      x, y = 400, 90
      frame = 0
      
      while (x > 203 and y < 535):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 1.3 *1.5
            y += 3 *1.5
            delay(0.05)
            get_events()


def move_132_243():
      x, y = 203, 535
      frame=0

      while (x > 132 and y > 243):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 1
            y -= 4.2
            delay(0.05)
            get_events()

def move_535_470():
      x, y = 132, 243
      frame=0

      while (x < 535 and y < 470):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 1.7*2
            y += 1*2
            delay(0.05)
            get_events()

def move_477_203():
      x, y = 535, 470
      frame=0

      while (x > 477 and y > 203):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 1
            y -= 4.6
            delay(0.05)
            get_events()

def move_715_136():
      x, y = 477, 203
      frame=0

      while (x < 715 and y > 136):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 3.5
            y -= 1
            delay(0.05)
            get_events()

def move_316_225():
      x, y = 715, 136
      frame=0

      while (x > 316 and y < 225):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 4.48
            y += 1
            delay(0.05)
            get_events()

def move_510_92():
      x, y = 316, 225
      frame=0

      while (x < 510 and y > 92):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 1.43*2.5
            y -= 1*2.5
            delay(0.05)
            get_events()

def move_692_518():
      x, y = 510, 92
      frame=0

      while (x < 692 and y < 518):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 1*1.5
            y += 2.3*1.5
            delay(0.05)
            get_events()

def move_682_336():
      x, y = 692, 518
      frame=0

      while (x > 682 and y > 336):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 1*0.3
            y -= 18.2*0.3
            delay(0.05)
            get_events()

def move_712_349():
      x, y = 682, 336
      frame=0

      while (x < 712 and y < 349):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 2.3
            y += 1
            delay(0.05)
            get_events()

def move_400_90():
      x, y = 712, 349
      frame=0

      while (x > 400 and y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 1.2*2.5
            y -= 1*2.5
            delay(0.05)
            get_events()




while True:
    move_203_535()

    move_132_243()

    move_535_470()
    
    move_477_203()

    move_715_136()
    
    move_316_225()
    
    move_510_92()
    
    move_692_518()
    
    move_682_336()
    
    move_712_349()

    move_400_90()
