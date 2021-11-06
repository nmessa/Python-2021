##Lab Exercise 11.8.2021 Part II
##Author: 
##musicStream.py
##This program will stream in music from a file

import pygame

pygame.init()
pygame.mixer.init()


def main():
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Python Music Streamer")
    
    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #create labels for menu
    myFont2 = pygame.font.SysFont("None", 50)
    myFont = pygame.font.SysFont("None", 30)
    title = myFont2.render("Streaming Music Player", 1, (0, 0, 255))
    label = myFont.render("Press a choice from the menu", 1, (0, 0, 255))
    label1 = myFont.render("1.  Load Song", 1, (0, 0, 255))
    #Add other labels

    keepGoing = True
    clock = pygame.time.Clock()
    songLoaded = False
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.music.load("Dance The Night Away.ogg")
                    songLoaded = True
                elif event.key == pygame.K_2 and songLoaded:
                    pygame.mixer.music.play()
                #Add other event keys
    
        screen.blit(background, (0, 0))
        screen.blit(title, (150, 50))
        screen.blit(label1, (100, 100))
        #Blit other labels
        pygame.display.flip()     #end of while loop
        
    pygame.display.quit()    #kills display window
    
main()
    
