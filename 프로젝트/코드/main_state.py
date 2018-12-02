from pico2d import *
import game_framework
import game_world
from background import Background
from wisp import Wisp
from tiena import Tiena
import random
import game_clear
from planet import Planet
import main_state
import state_1_script
import wisp
from tiena_state_ui import Tiena_State_Ui
from enemy import Fire_Monster
from enemy import Lamp_enemy
import game_over
import tiena
import title_state
import state_1_script
import pause_state
import tiena_state_ui
tiena_HP=200
socre=0
death_time=0
class State_time:
    def __init__(self):
        self.time=60
        self.x,self.y=600,450
        self.image=load_image('start.png')
        self.opacity=0.8
        self.BGM=load_music('background.mp3')
        self.BGM.repeat_play()
        self.BGM.set_volume(80)
        self.font = load_font('segoepr.ttf', 25)



    def update(self):
        self.image.opacify(self.opacity)
        self.time+=1
        if self.y>400:
            self.y-=0.1
            self.opacity+=0.02
        if self.time>120:
            self.x,self.y=0,1500
    def draw(self):
        self.image.draw(self.x,self.y)
    def handle_events(self,event):
        pass



def collide(a,b):
    a_left,a_bottom,a_right,a_top=a.XYreturn()
    b_left,b_bottom,b_right,b_top=b.XYreturn()
    if a_left>b_right:return False
    if a_right<b_left:return False
    if a_top<b_bottom:return False
    if a_bottom>b_top:return False
    return True
def enter():
    global death_time
    global socre
    global tiena_HP
    game_framework.push_state(state_1_script)
    skill_ui=Tiena_State_Ui()
    tienaa=Tiena()
    time=State_time()
    background = Background()
    wispp = Wisp()
    tiena_state_ui=Tiena_State_Ui()
    game_world.add_object(tienaa, 2)
    game_world.add_object(background,0)
    game_world.add_object(wispp, 1)
    game_world.add_object(skill_ui,2)
    game_world.add_object(tiena_state_ui, 1)
    game_world.add_object(time,4)


def exit():
    game_world.clear()
def pause():
    pass
def resume():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            for game_object in game_world.all_objects():
                game_object.handle_events(event)


def update():
    global death_time
    for game_object in game_world.all_objects():
        game_object.update()
    for o in game_world.objects[4]:
        if type(o) == State_time:

            if(o.time==300):
                fire_monsters1 = [Fire_Monster(i, j) for (i, j) in [(1200, 500), (1250, 500), (1300, 500), (1350, 500),(1400,500)]]
                game_world.add_objects(fire_monsters1,3)
            elif (o.time==420):
                fire_monsters2=[Fire_Monster(i, j) for (i, j) in [(1200, 300), (1250, 300), (1300, 300), (1350, 300),(1400,300)]]
                game_world.add_objects(fire_monsters2,3)
            elif (o.time==700):
                fire_monsters3=[Fire_Monster(i, j) for (i, j) in [(1200, 650), (1250, 620), (1300, 590), (1350, 560),(1400,530),(1450,500),(1500,470),(1550,440)]]
                game_world.add_objects(fire_monsters3,3)
            elif (o.time==720):
                planet1=Planet(400,1000)
                game_world.add_object(planet1,3)
            elif (o.time==900):
                lamp_enemy1 = Lamp_enemy(1200, 500)
                game_world.add_object(lamp_enemy1, 3)
            elif (o.time==1100):
                fire_monsters4=[Fire_Monster(i, j) for (i, j) in [(1200, 200), (1250, 230), (1300, 260), (1350, 290),(1400,320),(1450,350),(1500,380),(1550,410),
                                                                 (1200, 440), (1250, 470), (1300, 500), (1350, 530),(1400, 560), (1450, 590)]]
                game_world.add_objects(fire_monsters4,3)
            elif (o.time==1200):
                planet2=Planet(600,1000)
                game_world.add_object(planet2,3)
            elif (o.time==1260):
                planet3=Planet(400,1000)
                game_world.add_object(planet3,3)
            elif (o.time==1320):
                planet4=Planet(200,1000)
                game_world.add_object(planet4,3)
            elif (o.time==1800):
                lamp_enemy2=Lamp_enemy(1200,550)
                lamp_enemy3=Lamp_enemy(1200,250)
                game_world.add_object(lamp_enemy2,3)
                game_world.add_object(lamp_enemy3,3)
            elif (o.time==1920):
                fire_monster5=[Fire_Monster(i, j) for (i, j) in [(1200, 650), (1250, 620), (1300, 590), (1350, 560),(1400,530),(1450,500),(1500,470),(1550,440),
                                   (1200,150),(1250,180),(1300,210),(1350,240),(1400,270),(1450,300),(1500,330),(1550,360)]]
                game_world.add_objects(fire_monster5,3)
            elif (o.time==2000):
                planet5=Planet(350,1000)
                game_world.add_object(planet5,3)
            elif (o.time==2200):
                fire_monster6=[Fire_Monster(i, j) for (i, j) in [(1200, 650), (1250, 650), (1300, 650), (1350, 650),(1400,650),(1450,600),(1500,600),(1550,600),
                                   (1600,600),(1650,600),(1700,550),(1750,550),(1800,550),(1850,550),(1900,550)]]
                game_world.add_objects(fire_monster6,3)
            elif (o.time==2300):
                planet6=Planet(random.randint(100,1100),1000)
                game_world.add_object(planet6,3)
            elif(o.time==2400):
                planet7=Planet(random.randint(100,1100),1000)
                game_world.add_object(planet7,3)

            elif(o.time==2500):
                lamp_enemy5=Lamp_enemy(1300,700)
                game_world.add_object(lamp_enemy5,3)

            elif(o.time==2800):
                fire_monsters7= [Fire_Monster(i, j) for (i, j) in [(1200, 500), (1250, 500), (1300, 500), (1350, 500),(1400,450),(1450,400),(1500,350),(1550,300),
                                   (1600,250),(1650,300),(1700,350),(1750,400),(1800,450)]]
                game_world.add_objects(fire_monsters7,3)
            elif(o.time==3250):
                fire_monsters8=[Fire_Monster(i, j) for (i, j) in [(1200, 650), (1250, 620), (1300, 590), (1350, 560),(1400,530),(1450,500),(1500,470),(1550,440),
                                   (1200,150),(1250,180),(1300,210),(1350,240),(1400,270),(1450,300),(1500,330),(1550,360)]]
                game_world.add_objects(fire_monsters8, 3)
            elif(o.time==3600):
                game_framework.push_state(game_clear)



    for i in range(len(game_world.objects)):
        for o in game_world.objects[i]:
            if type(o) == tiena.Failed_Tiena:
                death_time+=1
                if death_time==120:
                    game_framework.push_state(game_over)
    delay(0.01)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    for o in game_world.objects[4]:
        if type(o) == main_state.State_time:
            o.font.draw(1000, 750,'SCORE : %d'% socre, (255, 255, 255))
    update_canvas()





