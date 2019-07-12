import sys
def placeWalls(board_object,enemies):
    # Placing walls on the board
    length = board_object.length
    width = board_object.width

    # Placing boundary walls

    for x in range(0, 2):
        for y in range(0, width):
            board_object.matrix[x][y] = '\x1b[2;37;41m' + "X" + '\x1b[0m'

    for x in range(length-2,length):
        for y in range(0, width):
            board_object.matrix[x][y] = '\x1b[2;37;41m' + "X" + '\x1b[0m'

    for y in range(0,4):
        for x in range(0, length):
            board_object.matrix[x][y] = '\x1b[2;37;41m' + "X" + '\x1b[0m'

    for y in range(width-4,width):
        for x in range(0,length):
            board_object.matrix[x][y] = '\x1b[2;37;41m' + "X" + '\x1b[0m'
    
    #for y in range(20,24):
        #board_object.matrix[29][y] ='\033[93m' + "!"

    for i in range(30,38):
        board_object.matrix[24][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(30,38,2):
        board_object.matrix[23][i] ='\033[93m' + "0"

    for i in range(35,38):
        board_object.matrix[20][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    board_object.matrix[19][35] = '\033[93m' + "0"
    board_object.matrix[19][36] = '\033[93m' + "!"
    board_object.matrix[19][37] = '\033[93m' + "!"
    for i in range(45,50):
        board_object.matrix[26][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for i in range(50,55,2):
        board_object.matrix[22][i] ='\033[93m' + "0"
    for i in range(50,55):
        board_object.matrix[23][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(55,60):
        board_object.matrix[20][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for i in range(85,90):
        board_object.matrix[27][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'   
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
        board_object.matrix[25][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
        board_object.matrix[24][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(85,90,2):
        board_object.matrix[23][i] ='\033[93m' + "0"
    for i in range(105,110):
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(110,112):
        board_object.matrix[23][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(115,130):
        board_object.matrix[20][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(115,130,2):
        board_object.matrix[19][i] ='\033[93m' + "0"

    for i in range(170,180):
        board_object.matrix[12][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'   
        board_object.matrix[16][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
        board_object.matrix[20][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
        board_object.matrix[24][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for i in range(170,180):
        board_object.matrix[23][i] ='\033[93m' + "0"

    for i in range(230,238):
        board_object.matrix[24][i] ='\x1b[2;30;47m' + "X" + '\x1b[0m'
    for i in range(230,238):
        board_object.matrix[23][i] ='\033[93m' + "0"

    for i in range(305,310):
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    board_object.matrix[25][307] = '\033[93m' + "!"
#   board_object.matrix[25][308] = '\033[93m' + "!"
    for i in range(400,410):
        board_object.matrix[23][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(400,410,2):
        board_object.matrix[22][i] ='\033[93m' + "0"

    for i in range(455,460):
        board_object.matrix[20][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for i in range(500,505):
        board_object.matrix[27][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'   
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
        board_object.matrix[25][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
        board_object.matrix[24][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(525,530):
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(525,530,2):
        board_object.matrix[25][i] ='\033[93m' + "0"

    for i in range(535,540):
        board_object.matrix[23][i] ='\x1b[2;30;47m' + "X" + '\x1b[0m'
    for i in range(545,570):
        board_object.matrix[20][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(575,580):
        board_object.matrix[23][i] ='\x1b[2;30;47m' + "X" + '\x1b[0m'
    for i in range(580,585):
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(600,605):
        board_object.matrix[26][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(603,608):
        board_object.matrix[25][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(605,610):
        board_object.matrix[24][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(608,613):
        board_object.matrix[23][i] ='\x1b[2;37;41m' + "X" + '\x1b[0m'
    for i in range(27,15,-1):
        board_object.matrix[i][625] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for i in range(625,628):
        board_object.matrix[15][i] ='\x1b[0;30;44m' + "X" + '\x1b[0m'
    for k in range(1,20):
        for i in range(4,6):
            for j in range(30*k,30*k+5):
                board_object.matrix[i][j] ='\x1b[2;30;46m' + "-" + '\x1b[0m'
            board_object.matrix[5][30*k-1] ='\x1b[2;30;46m' + "-" + '\x1b[0m'
            board_object.matrix[5][30*k+5] ='\x1b[2;30;46m' + "-" + '\x1b[0m'


    # PLacing enemies
    enemies[0].setNewPosition(board_object,26,39)
    enemies[1].setNewPosition(board_object,26,74)
    enemies[2].setNewPosition(board_object,26,140)
    enemies[3].setNewPosition(board_object,26,173)
    enemies[4].setNewPosition(board_object,26,195)
    enemies[5].setNewPosition(board_object,26,220)
    enemies[6].setNewPosition(board_object,26,255)
    enemies[7].setNewPosition(board_object,26,287)
    enemies[8].setNewPosition(board_object,26,330)
    enemies[9].setNewPosition(board_object,26,350)
    enemies[10].setNewPosition(board_object,26,375)
    enemies[11].setNewPosition(board_object,26,403)
    enemies[12].setNewPosition(board_object,26,430)
    enemies[13].setNewPosition(board_object,26,462)
    enemies[14].setNewPosition(board_object,26,485)
    enemies[15].setNewPosition(board_object,26,560)
    enemies[16].matrix = [['@','@', '@', '@'],['@','@','@','@']]
    
    enemies[16].setNewPosition(board_object,26,595)


    



