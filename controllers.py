"""Controllers."""
import sys
import os
import subprocess
try:
    from subprocess import DEVNULL  # Python 3.
except ImportError:
    DEVNULL = open(os.devnull, 'wb') # for not showing output of sound to screen
p2=0
try:
    p3 =subprocess.Popen(['mplayer','theme.wav'],stdout=DEVNULL, stderr=DEVNULL)
except:
    pass



def overlayMatrix(board_object, item_object, x, y):
    """Overlay item on board with top left corner of item at (x,y) of board."""
    board_matrix = board_object.returnMatrixBoard()
    item_matrix = item_object.returnMatrix()
    k = 0
    l = 0
    for i in range(x, x + item_object.length):
        for j in range(y, y + item_object.width):
            board_matrix[i][j] = item_matrix[k][l]
            l += 1
        k += 1
        l = 0
    board_object.editBoard(board_matrix)


def check4clash(board_object, item_object, x, y,fl):
    """Check if the item_object clashes with a wall."""
    """Here, (x, y) represent potential new position."""
    board_matrix = board_object.returnMatrixBoard()
    prev_x = item_object.x
    prev_y = item_object.y

    # Erase object before checking
    if fl==1:
        if prev_x is not None:
            for i in range(prev_x, prev_x+item_object.length):
                for j in range(prev_y, prev_y+item_object.width):
                    board_matrix[i][j] = ' '

    # Check for clash with fire
    for i in range(x, x+item_object.length):
        for j in range(y, y+item_object.width):
            if board_matrix[i][j] != ' ' and board_matrix[i][j] !=  '\033[93m' + "0":
                overlayMatrix(board_object, item_object, prev_x, prev_y)
                if board_object.matrix[i][j] == '\033[93m' + "!":
                    try:
                        os.system('aplay -q die.wav&')
                    except:
                        pass
                    global p3
                    p3.kill()
                    sys.exit()
                return 1
    
    # Checking for coins near mario    
    for i in range(x, x+item_object.length):
        for j in range(y, y+item_object.width):
            if board_matrix[i][j] == '\033[93m' + "0":
                os.system('aplay -q coin.wav&')
                board_object.score+=2
                
    return 0


def f1():
    global p3
    p3.kill()
    sys.exit
