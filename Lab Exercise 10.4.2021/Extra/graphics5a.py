##Displays the tangent function
##Author: nmessa
##Date: 10.5.2017

import pygame, sys
import math

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
    y = int(math.tan(x/640.0 * 4 * math.pi) * 200 + 240)
    if y > 1000000:
        y = 1000000
    if y < -1000000:
        y = -1000000
    
    plotPoints.append([x, y])



pygame.draw.lines(screen, [0,0,0],False, plotPoints, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
