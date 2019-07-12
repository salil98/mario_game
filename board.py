
# DEFINITION OF CLASS BOARD


class Board:
    #initializing the board
    def __init__(self,length,width):

        self.length = length
        self.width = width
        self.matrix = []
        self.score = 0

   # Initializing Matrix with blank spaces

        for x in range(0,length):
            self.matrix.append([])
            for y in range(0,width):
                self.matrix[x].append(' ')

    def returnMatrixBoard(self):
        # Return the board as matrix
        return self.matrix


    def returnStringBoard(self,mario,lives):
        #Return the matrix in string format
        stringBoard = ""
        for x in range(0,2):
                for y in range(0,143):
                    stringBoard += self.matrix[x][y]
                stringBoard += '\n'
        
        if mario.y <= 20:
            for x in range(2,28):
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                for y in range(4,139):
                    stringBoard+=self.matrix[x][y]
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                stringBoard+= '\n'
        elif mario.y >20 and mario.y<=520:
            for x in range(2,28):
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                for y in range(mario.y-20,mario.y+115):              # printing background in the vicinity of mario
                    stringBoard+=self.matrix[x][y]
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                stringBoard+='\n'
        else:
            for x in range(2,28):
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                for y in range(self.width-4-135,self.width-4):
                    stringBoard+=self.matrix[x][y]
                stringBoard+='\x1b[2;37;41m' + "XXXX" + '\x1b[0m'
                stringBoard+='\n'

        for x in range(28,30):
            for y in range(0,143):
                stringBoard += self.matrix[x][y]
            stringBoard += '\n'


        stringBoard += "SCORE: " + str(self.score) + '\n' # For score
        stringBoard += "Press 'q' to exit\n"
        stringBoard += "LIVES:" + str(lives)
        return stringBoard

    def editBoard(self,newMatrix):
        #edit the matrix
        self.matrix = newMatrix
