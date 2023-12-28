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
TURN = True

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
    
    pygame.draw.rect(screen,BLUE,(CURSORPOSITION_X*SQUARE_SIZE,CURSORPOSITION_Y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),3)
#Manage the movement of the pieces
def CursorPressed(CURSORPOSITION_X,CURSORPOSITION_Y,ENTER,board=None,AntCursorPositionX=None,AntCursorPositionY=None):
    if board[AntCursorPositionY][AntCursorPositionX] != 0:
        if ENTER == False:
            ENTER = True
            return (CURSORPOSITION_X,CURSORPOSITION_Y,ENTER)
        if ENTER == True:
            ENTER = False
            Grab = board[AntCursorPositionY][AntCursorPositionX]
            board[AntCursorPositionY][AntCursorPositionX] = 0
            board[CURSORPOSITION_Y][CURSORPOSITION_X] = Grab 
            return(CURSORPOSITION_X,CURSORPOSITION_Y,ENTER)
    else:
        ENTER = False
        return (CURSORPOSITION_X,CURSORPOSITION_Y,ENTER)

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    clock = pygame.time.Clock()
    running = True
    ENTER = False
    CURSORPOSITION_X = ROWS//2
    CURSORPOSITION_Y = COLS//2
    Board = CreateBoard()
    antCURSORPOSITION_X = 0
    antCURSORPOSITION_Y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    antCURSORPOSITION_X,antCURSORPOSITION_Y,ENTER = CursorPressed(CURSORPOSITION_X,CURSORPOSITION_Y,ENTER,Board,antCURSORPOSITION_X,antCURSORPOSITION_Y)
                    print(ENTER)
                    print(antCURSORPOSITION_X,antCURSORPOSITION_Y)
                if event.key == pygame.K_a:
                    CURSORPOSITION_X -= 1
                if event.key == pygame.K_d:
                    CURSORPOSITION_X += 1
                if event.key == pygame.K_s:
                    CURSORPOSITION_Y += 1
                if event.key == pygame.K_w:
                    CURSORPOSITION_Y -= 1

            if event.type == pygame.QUIT:
                running = False

        DrawBoard(screen,Board,CURSORPOSITION_X,CURSORPOSITION_Y)
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    print(Board)

if __name__ == '__main__':
    main()
    
