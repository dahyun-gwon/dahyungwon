from pico2d import *
KPU_WIDTH,KPU_HEIGHT=1280,1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)
os.chdir('D:\\2D게임프로그래밍\\제출\\2016180047\\drills\\drill06')


grass=load_image('grass.png')
boy=load_image('animation_sheet.png')
mouse=load_image('hand_arrow.png')
ground=load_image('KPU_GROUND.png')

global running
def cursor():
    pass

def move():
    pass


running(True)
while(running):
    cursor()
    move()
