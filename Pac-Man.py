import pygame
import time

pygame.init()

mult = 20
x = int(28*mult)
y = int(31*mult)
screen = pygame.display.set_mode([x,y])

board = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,2,2,1,1,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,1,1,2,2,3,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

pacX = 13*mult + int(mult/2)
pacY = 23*mult + int(mult/2)
dirX = 0
dirY = 0
bufX = 0
bufY = 0
pacman = pygame.draw.circle(screen,(255,255,0),(pacX,pacY),8)

def update():
    screen.fill((0,0,0))
    for i in range(0,x,mult):
        for j in range(0,y,mult):
            p = board[int(j/mult)][int(i/mult)]
            if p == 0:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
            elif p == 1:
                pygame.draw.rect(screen,(0,0,255),(i,j,mult-1,mult-1))
            elif p == 2:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,255),
                                   (i+int(mult/2),j+int(mult/2)),2)
            elif p == 3:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,0),
                                   (i+int(mult/2),j+int(mult/2)),4)

    for i in range(0,x,mult):
        for j in range(0,y,mult):
            p = board[int(j/mult)][int(i/mult)]
            if p == 4:
                global dirX
                global dirY
                global bufX
                global bufY
                global pacX
                global pacY
                #print(pacX,pacY)
                if (int(i/mult+bufX) < 28 and int(i/mult+bufX) > 0 and
                    board[int(j/mult+bufY)][int(i/mult+bufX)] != 1 and
                    pacX % mult == int(mult/2) and
                    pacY % mult == int(mult/2)):
                    dirX = bufX
                    dirY = bufY
                if board[int(j/mult+dirY)][int(i/mult+dirX)] != 1:
                    pacX = pacX + dirX
                    pacY = pacY + dirY
                    if (pacX % mult == int(mult/2) and
                        pacY % mult == int(mult/2)):
                        board[int(j/mult)][int(i/mult)] = 0
                        board[int(j/mult+dirY)][int(i/mult+dirX)] = 4
                        if int(i/mult+dirX) == 27:
                            board[int(j/mult+dirY)][int(i/mult+dirX)] = 0
                            board[int(j/mult+dirY)][1] = 4
                            pacX = pacX - 26*mult
                        elif int(i/mult+dirX) == 0:
                            board[int(j/mult+dirY)][int(i/mult+dirX)] = 0
                            board[int(j/mult+dirY)][26] = 4
                            pacX = pacX + 26*mult
                pygame.draw.circle(screen,(255,255,0),(pacX,pacY),8)
                #print(int(j/mult),int(i/mult))
                return
                
            #pygame.display.flip()
            #time.sleep(.001)

update()

counter = 0
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bufX = 0
                bufY = -1
            elif event.key == pygame.K_a:
                bufX = -1
                bufY = 0
            elif event.key == pygame.K_s:
                bufX = 0
                bufY = 1
            elif event.key == pygame.K_d:
                bufX = 1
                bufY = 0
            
    #screen.fill((255,255,255))

    counter = counter + 1
    if counter > 30:
        update()
        counter = 0
    pygame.display.flip()

pygame.quit()
