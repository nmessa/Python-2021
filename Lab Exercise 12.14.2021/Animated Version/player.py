## Lab Exercise 12/14/2021
## Author: 
## This implements the Player class
## player.py

from die import Die
from rolldice import *
from time import sleep

class Player():
    def __init__ (self):
        #Add code here
        

    def getNumberOfRolls(self):
        #Add code here
        

    def play(self, canvas):
        #Add code here

        

    def __str__(self):
            result = ""
            for (d1, d2) in self.rolls:
                result += str((d1, d2)) + "\t" + str(d1 + d2) + '\n'
            return result
#end of player class