""" spriteGroup.py 
    shows how to check for a
    collision between a sprite and 
    a group"""
    
import pygame, collisionObjects
pygame.init()
WIDTH  = 1024
HEIGHT = 768

class TransCircle(collisionObjects.Circle):
    """ extended colisionObjects circle with 
       colorkey transparency.  """
    def __init__(self):
        collisionObjects.Circle.__init__(self)
        self.image.set_colorkey((255, 255, 255))
        
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colliding with a Group")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    #Construct and initalize a label object
    lblOutput = collisionObjects.Label()
    lblOutput.text = "Hi"
    lblOutput.center = (100, 50)

    #Construct a circle with transperancy
    circle = TransCircle()
    #circle = collisionObjects.Circle()

    #create a list to hold the square objects
    squares = []

    #Create 10 square objects and put them in the list
    for i in range(10):
        square = collisionObjects.Square((255, 0, 0), screen)
        squares.append(square)

    #create sprite groups   
    basicSprites = pygame.sprite.Group(circle, lblOutput)
    squareGroup = pygame.sprite.Group(squares)
    
    keepGoing = True
    clock = pygame.time.Clock()

    #start game loop
    while keepGoing:
        clock.tick(30)

        #check for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #check it circle has collided with anything in the squareGroup
        if pygame.sprite.spritecollide(circle, squareGroup, True):
            lblOutput.text = "Collision"
        else:
            lblOutput.text = "No collision"

        #erase all sprites in the sprite groups    
        squareGroup.clear(screen, background)
        basicSprites.clear(screen, background)

        #update all sprites information in the sprite groups
        squareGroup.update()
        basicSprites.update()

        #redraw all sprites with their new information
        squareGroup.draw(screen)
        basicSprites.draw(screen)
    
        pygame.display.flip()
        
    pygame.display.quit() #close graphics window gracefully
        
main()
