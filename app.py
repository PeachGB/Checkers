import pygame

HEIGHT = 800
WIDTH = 800
ROWS = 10
COLS = 10
SQUARE_SIZE  = HEIGHT // ROWS
CIRCLE_RADIUS = SQUARE_SIZE // 3


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,10,200)
PIECEWHITE = (239,238,210)
PIECEBLACK = (118,150,86)

class CursorClass:
    ENTER = False
    Pressed = 0
    TURN = 2
    def __init__(self,CursorPositionX,CursorPositionY):
        self.CursorPositionX = CursorPositionX
        self.CursorPositionY = CursorPositionY
    @staticmethod
    def clear(Board):
        for i in range(0,COLS):
            for j in range(0,ROWS):
                if Board[i][j] == '#':
                    Board[i][j] = 0

        else:
            return
    @staticmethod
    def ShowMove(Yplus,y,x,Board):
        if x not in (0, ROWS-1):
            if Board[y+Yplus][x+1] == 0:
                Board[y+Yplus][x+1] = '#'
            if Board[y+Yplus][x-1] == 0:
                Board[y+Yplus][x-1] = '#'
        elif x == 0:
            if Board[y+Yplus][x+1] == 0:
                Board[y+Yplus][x+1] = '#'
        else:
            if Board[y+Yplus][x-1] == 0:
                Board[y+Yplus][x-1] = '#'


    def CanMove(self,Board):
        x = self.AntCursorPosition[0]
        y = self.AntCursorPosition[1]
        if self.Pressed != '#':
            self.clear(Board)
        if self.TURN == self.Pressed:
            match self.Pressed:
                case 2:
                    self.ShowMove(-1,y,x,Board)
                case 1:
                    self.ShowMove(1,y,x,Board)
    def Move(self,Board):
        Grab = Board[self.AntCursorPosition[1]][self.AntCursorPosition[0]]
        Board[self.AntCursorPosition[1]][self.AntCursorPosition[0]] = 0
        Board[self.CursorPositionY][self.CursorPositionX] = Grab
        self.clear(Board)
        #this just returns 1 when the input(TURN) is 2 and 2 when the input is 1
        self.TURN = 2**(-self.TURN+2)


    def Return(self,Board):
        self.Pressed = Board[self.CursorPositionY][self.CursorPositionX]
        if self.Pressed == '#':
            self.Move(Board)
        self.AntCursorPosition = (self.CursorPositionX,self.CursorPositionY)
        self.CanMove(Board)

#create an array for managing the logic of the board
def CreateBoard():
    Board = [[0 for n in range(ROWS)] for n in range(COLS)]
    for i in range(0,3):
        for j in range(0,COLS):
            if i % 2 == 0:
                if j % 2 == 0:
                    Board[i][j] = 1
            else:
                if j % 2 != 0:
                    Board[i][j] = 1
    for i in range(ROWS-1,ROWS-4,-1):
        for j in range(0,COLS):
            if i % 2 != 0:
                if j % 2 != 0:
                    Board[i][j] = 2
            else:
                if j % 2 == 0:
                    Board[i][j] = 2
    return Board

#draw de board on the screen
def DrawBoard(screen,board,CURSORPOSITION_X,CURSORPOSITION_Y):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col  in range(row % 2, COLS,2):
            pygame.draw.rect(screen,BLACK,(col * SQUARE_SIZE, row * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
            if board[row][col] == 1:
                pygame.draw.circle(screen,PIECEBLACK,(col*SQUARE_SIZE+SQUARE_SIZE//2,row*SQUARE_SIZE+SQUARE_SIZE//2),CIRCLE_RADIUS)
            if board[row][col] == 2:
                pygame.draw.circle(screen,PIECEWHITE,(col*SQUARE_SIZE+SQUARE_SIZE//2,row*SQUARE_SIZE+SQUARE_SIZE//2),CIRCLE_RADIUS)
            if board[row][col] == '#':
                pygame.draw.circle(screen,(128,128,128),(col*SQUARE_SIZE+SQUARE_SIZE//2,row*SQUARE_SIZE+SQUARE_SIZE//2),CIRCLE_RADIUS/2)

    pygame.draw.rect(screen,BLUE,(CURSORPOSITION_X*SQUARE_SIZE,CURSORPOSITION_Y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),3)




def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    clock = pygame.time.Clock()
    running = True
    ENTER = False
    Board = CreateBoard()
    Cursor = CursorClass(ROWS//2,COLS//2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        Cursor.Return(Board)
                    case pygame.K_a:
                        Cursor.CursorPositionX -= 1
                        if Cursor.CursorPositionX == -1:
                            Cursor.CursorPositionX = ROWS-1
                    case pygame.K_d:
                         Cursor.CursorPositionX += 1
                         if Cursor.CursorPositionX == ROWS:
                             Cursor.CursorPositionX = 0
                    case pygame.K_s:
                         if event.key == pygame.K_s:
                             Cursor.CursorPositionY += 1
                             if Cursor.CursorPositionY == COLS:
                                 Cursor.CursorPositionY = 0
                    case pygame.K_w:
                        Cursor.CursorPositionY -= 1
                        if Cursor.CursorPositionY == -1:
                            Cursor.CursorPositionY = COLS-1
            if event.type == pygame.QUIT:
                running = False

        DrawBoard(screen,Board,Cursor.CursorPositionX,Cursor.CursorPositionY)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

