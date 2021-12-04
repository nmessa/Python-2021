## Graphics Drawing Package
## Author: 
## Date: 12/9/2021
## This package consists of a variety of classes that will allow the user
## to easily draw points, lines, rectangles, circles, and polygons.
## A Canvas class is defined that has a draw method which uses the _draw method
## in each GeometricObject class.  Each geometric object (Point, Line, Circle,
## Rectangle, and Polygon) uses the GeometricObject as the base class.

import turtle, math

class Canvas:
    def __init__(self,w,h):
        #Add coded here
        

    def draw(self,gObject):
        #Add coded here
        
        
    def freeze(self):
        #Add coded here
        

class GeometricObject:
    def __init__(self):
        #Add coded here
        

    def getColor(self):
        #Add coded here
        

    def getWidth(self):
        #Add coded here
        

    def setColor(self,color):
        #Add coded here
        

    def setWidth(self,width):
        #Add coded here
        

    def _draw(self,someturtle):
        #Add coded here
        

class Point(GeometricObject):
    def __init__(self, x,y):
        #Add code here
        

    def getCoord(self):
        #Add code here

    def getX(self):
        #Add code here

    def getY(self):
        #Add code here

    def _draw(self,aturtle):
        #Add code here


class Line(GeometricObject):
    def __init__(self, p1,p2):
        #Add code here
    
    def getP1(self):
        #Add code here
        
    def getP2(self):
        #Add code here
        
    def _draw(self,aturtle):
        #Add code here

class Rectangle(GeometricObject):
    def __init__(self, p1,p2):
        #Add code here
        
    def _draw(self,aturtle):
        #Add code here

class Circle(GeometricObject):
    def __init__(self, p1,r):
        #Add code here
        
        
    def _draw(self,aturtle):
        #Add code here
        

class Polygon(GeometricObject):
    def __init__(self, p1, sides,length):
        #Add code here
        
        
    def _draw(self,aturtle):
        #Add code here

