#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:28:25 2022

@author: marciobernardo
"""

## FreeCodeCamp Tutorial - day 1

# Start at 6:41 End at 48:26
# Using Spyder IDE


# Methods can be used in conjunction with one another

phrase = 'Giraffe Academy'

phrase.upper().isupper() # two methods called on object phrase (str).

## Numbers

# scientific notation
print(1e+5 == 100000) # e+x = 10**5 (10 raised to x) and e-x is 10 raised to -x

# "//" floor division x//y divides x/y and raund down the result

print(5/2) # returns 2.5 a float

print(5//2) # returns 2 an int. floor division rounds down 2.5 to 2

print(-5//2) # returns -3, which is -2.5 rounded down to -3

# "%" Modulus operator. returns the remainder of dividing the left operand by the right operand

print(5%3) # returns 2

#modulos of negative number gets tricky. Python uses the funtion reminder = x-(y*(x//y))
print(-5%3) # returns 1  calculate as -5 - (3 * (-5 // 3)) 
print(5%-3) # returns -1
print(-5%-3) # returns -2 because (-5 // -3) = 1


# Math functions


abs(-19) # returns 19, absolute

heights = [1.76,1.80, 1.55,1.54]
min(heights) # minimum
max(heights) #maximum

pow(2,5) # returns 32 = 2**5 
pow(2,-5) # returns 0.03125 = 2**-5

round(2.25,1) #returns 2.2, round(x,n) rouds x to the nth decimal point

from math import * # imports math module but without the need to call the module before the function!

ceil(heights[0]) # returns 2. the smallest integer greater than or equal to x.
floor(heights[0]) # returns 1. the largest integer less than or equal to x.

sqrt(25) # Square root

#  https://docs.python.org/3/library/math.html has all the math module functions available

## List

friends = ['Rodrigo', 'Daniel', 'Alexandre', 'Monica', 'Adriana', 'Flavia', 'Silvia']

print(friends)
