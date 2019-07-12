from walls import *
from board import *
from mario import *
from person import * 
from enemy import *
from input import *
import os,time
try:
    from subprocess import DEVNULL  # Python 3.
except ImportError:
    DEVNULL = open(os.devnull, 'wb')
lives=3
board_object = Board(30,650)
mario = Mario(2, 4, 'mario')
mario.setNewPosition(board_object,26,10)
enemies = []
for i in range(0,17):
    enemies.append(Enemy(2,4,'enemy'))
placeWalls(board_object,enemies)
getch = Get()
jump=0
counter = 0
flag = 0
coins=0
print(board_object.returnStringBoard(mario,lives))
os.system('spd-say "Welcome to the world of mario\n"')
#os.system('spd-say "live\n"')
def jumper():
    global counter
    global flag
    global jump
    if counter<=7 and flag==0:
        mario.move('w',board_object)
        counter = counter + 1
    if counter>7:
        flag=1
    if flag==1:
        mario.move('s',board_object)
        counter = counter-1
        if counter==-1:
            jump=0 
            flag=0
            counter=0


while True:
    input = input_to(getch)
    if mario.y==621:
        f1()
        try:
            os.system('aplay -q clear.wav&')
        except:
            pass
        os.system('spd-say "You WON"')
        time.sleep(4)
        sys.exit()
    if jump == 1:
        jumper()
    if jump==0 and mario.x!=26:
        mario.move('s', board_object)


    os.system('clear')
    
            

    for i in range(0,len(enemies)):
        if enemies[i].destroyed=='True1':
            enemies[i].move(board_object)
            enemies[i].destroyed='True'
        elif enemies[i].destroyed=='False':
            enemies[i].move(board_object)
    for i in range(len(enemies)):
        if board_object.matrix[mario.x][mario.y+5] == 'E' or board_object.matrix[mario.x][mario.y-2]=='E':
            try:
                os.system('aplay -q die.wav&')
            except:
                pass
            print(board_object.returnStringBoard(mario,lives))
            time.sleep(3)
            if lives==0:
                f1()
                sys.exit()
            else:
                lives=lives-1

                for p in range(mario.x, mario.x+mario.length):
                    for q in range(mario.y, mario.y+mario.width):
                        board_object.matrix[p][q] = ' '
                mario.x=26
                mario.y=10
                print(board_object.returnStringBoard(mario,lives))
    for i in range(len(enemies)):
        for j in range(enemies[i].y-1,enemies[i].y+4):
            if board_object.matrix[24][j] == '^':
                if enemies[i].destroyed=='False':
                    enemies[i].destroyed = 'True1'
                    board_object.score +=5
                    try:
                        os.system('aplay -q stomp.wav&')
                    except:
                        pass
                    print(board_object.returnStringBoard(mario,lives))
                   


                break
    print(board_object.returnStringBoard(mario,lives))

    if input == 'w' or input == 'W':
        if jump==0:
            try:
                os.system('aplay -q jump.wav&')
            except:
                pass
        jump=1
    if input is not None:
        if input == 'w':
            if jump==0:
                mario.move(input,board_object)

        else:
            mario.move(input,board_object)

    
    if input == 'q' or input == 'Q':
        f1()
        sys.exit()

def f1():
    p3.kill()
