"""
w3resource:
Write a Python program that calculates the area of a circle based on the radius entered by the user. 

Sample Output : 
r = 1.1
Area = 3.8013271108436504

Date: Sat 27 May 2023
"""

import math as m
r=float(input("Enter the radius: " ))
a=m.pi*(r**2)
print("Area= ",a)
