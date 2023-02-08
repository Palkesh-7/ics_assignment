# 3. Write a Python program to print the square and cube symbols in the area of a rectangle and the 
# volume of a cylinder. 
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

import math

def area_of_rectangle(a,b):

    print("Area of Rectangle : ",(a*b),"cm\u00b2")

def volume_of_cylinder(r,h):

    print("Volume of cylender :",(math.pi*r*r*h),"cm\u00b3")


if __name__ =="__main__":
    
    a = int(input("Enter width of cylinder in cm : "))
    b = int(input("Enter hight of cylinder in cm : "))

    r = int(input("Enter redius of cylender in cm : "))
    h = int(input("Enter hight of cylender in cm : "))


    area_of_rectangle(a,b)

    volume_of_cylinder(r,h)

