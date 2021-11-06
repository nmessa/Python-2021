## Lab Exercise 11/12/2021
## Author:
## A basic painting program that draws a variety of shapes as
## well as freehand drawing

import pygame, sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Paint:  (r)ed, (g)reen, (b)lue, (w)hite, blac(k), (1-9) width, (c)lear, (s)ave, (l)oad, (q)uit")  #This is all on one line

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
            #place myData into a tuple to be passed to checkKeys
                myData = (event, background, drawColor, lineWidth, keepGoing)
                myData = checkKeys(myData)
                (event, background, drawColor, lineWidth, keepGoing) = myData
        screen.blit(background, (0, 0))
        myLabel = showStats(drawColor, lineWidth)
        screen.blit(myLabel, (850, 730))
        pygame.display.flip()
    pygame.display.quit()
    sys.exit()
    
def checkKeys(myData):
    """test for various keyboard inputs"""
    
    #extract the data
    (event, background, drawColor, lineWidth, keepGoing) = myData
    if event.key == pygame.K_q:
        #quit
        #Add code here
    elif event.key == pygame.K_c:
        #clear screen
        #Add code here
    elif event.key == pygame.K_s:
        #save picture
        #Add code here
    elif event.key == pygame.K_l:
        #load picture
        #Add code here
    elif event.key == pygame.K_r:
        #red
        #Add code here
    elif event.key == pygame.K_g:
        #green
        #Add code here
    elif event.key == pygame.K_w:
        #white
        #Add code here
    elif event.key == pygame.K_b:
        #blue
        #Add code here
    elif event.key == pygame.K_k:
        #black
        #Add code here

#line widths
    elif event.key == pygame.K_1:
        lineWidth = 1
    #Add code here

#return all values 
    #Add code here
    return myData

def showStats(drawColor, lineWidth):
    """ shows the current statistics """
    myFont = pygame.font.SysFont("None", 20)
    stats = "color: %s, width: %d" % (drawColor, lineWidth)
    statSurf = myFont.render(stats, 1, (drawColor))
    return statSurf

main()
