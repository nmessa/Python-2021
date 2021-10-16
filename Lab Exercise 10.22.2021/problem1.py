##Lab Exercise 10.22.2021 Problem 1
##Author: 
##This program draws a moving block.
##It moves from upper left to lower right

from graphics import GraphicsWindow
from time import sleep

def main() :
   #define window size
   WIN_WIDTH = 400
   WIN_HEIGHT = 400   

   #create a graphics window
   win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)

   #create a canvas
   canvas = win.canvas()

   #set color to red and clear canvas
   canvas.setColor("red")
   canvas.clear()
   
   DELAY = 0.01   # 10 milliseconds between frames

   #animate the frame from upper left corner (0,0)
   #to lower right corner (WIN_WIDTH, WIN_WIDTH)
   #Add code here
   
   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   #define vlock size
   BLOCK_WIDTH = 20
   BLOCK_HEIGHT = 20

   #clear the canvas
   canvas.clear()

   #draw a rectangle at (frame, frame) with a width and height of
   #BLOCK_WIDTH and BLOCK_HEIGHT
   canvas.drawRect(frame, frame, BLOCK_WIDTH, BLOCK_HEIGHT)


# Start the program.
main()
