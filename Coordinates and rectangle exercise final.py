# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:20:41 2022

@author: Beth_El 2
"""

# geometry module: geom.py
class Rectangle: # rectangle class
    # make a rectangle using top left and bottom right coordinates
    def __init__(self,tl,br):
        self.tl=tl
        self.br=br
        self.width=abs(tl.x-br.x)  # width
        self.height=abs(tl.y-br.y) # height
    def area(self): # gets area of rectangle
        return self.width*self.height

class Coordinate: # coordinate class
     def __init__(self,x,y):
        # make coordinate obj with a reference (self), an x and a y
        self.x=x
        self.y=y
     def distance(self,another): # distance between 2 coordinates
        import math
        xdist=abs(self.x-another.x)
        ydist=abs(self.y-another.y)
        return math.sqrt(xdist**2+ydist**2) # pythagoras theorem

    # def test_rectangle():
       # print("Testing the rectangle area")
       # rect = Rectangle(12, 4)
       # actual = rect.area()
      #  print("Actual area of rectangle %d" %actual)

    # def test_coordinate():
      #  print("Testing the distance between tl and br")
    #xdist = 12
    #ydist = 4
        
#def main():
 #   tl = Coordinate(3, 10)
 #   br = Coordinate(15, 14)
 #   rect = Rectangle (tl, br)
  #  actual = rect.area()
  #  print("Area of the rectangle %d " %actual)


def main():
    tl_x=int(input("Enter the tl_x value: "))
    tl_y=int(input("Enter the tl_y value: "))
    tl = Coordinate(tl_x,tl_y)
    br_x=int(input("Enter the br_x value: "))
    br_y=int(input("Enter the br_y value: "))
    br = Coordinate((br_x), br_y)
    
    
    rect = Rectangle(tl, br)
    actual = rect.area()
    print("Area of the rectangle %d " %actual)

    
    
main()