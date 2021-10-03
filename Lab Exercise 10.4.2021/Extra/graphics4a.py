##Displays the cosine function
##Author: nmessa
##Date: 10.5.2017

import pygame, sys
import math

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])

for x in range(0, 640):
    y = int(math.cos(x/640.0 * 4 * math.pi) * 200 + 240)
    pygame.draw.rect(screen, [0,0,0],[x, y, 1, 1], 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
