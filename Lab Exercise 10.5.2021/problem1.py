## Lab Exercise 10/5/2021 Problem 1
## Author: 
## This program will use functions to calculate the surface
## area and volume for several geometric shapes
from math import *

def  sphereVolume(r):
    #Add code here
    
    
def  sphereSurface(r):
    #Add code here

def  cylinderVolume(r, h):
    #Add code here
    
def  cylinderSurface(r, h):
    #Add code here
    
def  coneVolume(r, h):
    #Add code here

def  coneSurface(r, h):
    r#Add code here

#Get radius and height of geometric shape as a floating point number
radius = float(input("Enter the radius of the geometric shape: "))
height = float(input("Enter the height of the geometric shape: "))

#Call each function and print the results
print ("Sphere volume =", sphereVolume(radius))
print ("Sphere surface area =", sphereSurface(radius))
print ("Cylinder volume =", cylinderVolume(radius, height))
print ("Cylinder surface area =", cylinderSurface(radius, height))
print ("Cone volume =", coneVolume(radius, height))
print ("Cone surface area =", coneSurface(radius, height))

##Sample Output
##Enter the radius of the geometric shape: 2
##Enter the height of the geometric shape: 4
##Sphere volume = 33.510321638291124
##Sphere surface area = 50.26548245743669
##Cylinder volume = 50.26548245743669
##Cylinder surface area = 75.39822368615503
##Cone volume = 16.755160819145562
##Cone surface area = 96.86414738684789

