## Lab Exercise 10.22.2021 Problem 2
## Author: 
## This program will have a red block bouncing from upper left to
## lower right corner

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

   #det color to red and clear the canvas
   canvas.setColor("red")
   canvas.clear()
   
   DELAY = 0.01   # 10 milliseconds between frames

   while True:
      #move block from upper left to lower right
      #Add code here
      

      #move block from lower right to upper left
      #Add code here
      

   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   #define block size
   BLOCK_WIDTH = 20
   BLOCK_HEIGHT = 20

   #clear the canvas
   canvas.clear()

   #draw a rectangle at (frame, frame) with a width and height
   #of BLOCK_WIDTH and BLOCK_HEIGHT
   canvas.drawRect(frame, frame, BLOCK_WIDTH, BLOCK_HEIGHT)


# Start the program.
main()
