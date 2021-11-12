## Lab Exercise 11/18/2021 Problem 4
## Author: nmessa
## Program to test if two balls have collided in 2D and 3D space
from distance import distance3D
from point3D import Point3D

def collide3D(t1, t2):
    # store center and radius of two circles
    #Add code here

    
    #Check for collision
    #Add code here

    

#ball set 1 for 3D space
t1 = (0,0,0, 1)
t2 = (3,3,3, 1)
print (collide3D(t1, t2)) #False

#ball set 2 for 3D space
t1 = (5,5,5,2)
t2 = (2,8,5,3)
print (collide3D(t1, t2))   #True
        
    
