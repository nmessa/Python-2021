##Lab Exercise 10/5/2021 Problem 2
##Author: 
##This program will print a checkerboard
from graphics import *

# Create the window and access the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Initialize values
colors = ['red', 'green']
count = 0    #This variable is for keeping track of color (even = red odd = green)
x = 0
y = 0
width = 50
height = 50

#draw checkerboard
for row in range(8):
    for col in range(8):
        #draw all columns in the row
        #Add code here
        
    #Go to next row at the first column
    #Add code here
        

# Wait for the user to close the window.
win.wait()

        
