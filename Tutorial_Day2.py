#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 01:41:24 2022

@author: marciobernardo
"""

## FreeCodeCamp Tutorial - day 2

# Start at 1:03:10 End at 1:40:06
# Using Spyder IDE


## Lists

cities = ['gotham', 'themyscira','central city','krypton', 'gotham', 'atlantis'] # declared with a square bracket "[]". List can have all types of data

print(cities) 

cities[0:4] # List index start with a 0. indexing uses a bracket [x:y] - x inclusive, y exclusive. 

cities[-1] = 'maine' # changes the value of index -1 (last object)

# list methods

heroes = ['batman', 'wonder women', 'flash', 'super man', 'cyborg', 'aquaman']

heroes.extend(cities) # add the whole list "cities" to the heroes list

print(heroes)

print(f'{heroes[0:6]}\n {heroes[6:]}')

heroes.append('coast city') #include 'coast city' as the last item in heroes list

heroes.insert(6, 'green lantern')

print(f'{heroes[0:7]}\n {heroes[7:]}')

heroes.index("hawk")

heroes.index('green lantern')

heroes.count('gotham')

cities.sort()

print(cities)


## Tuple - container of values, similar to list but tuples do not change (immutable)
# Use tuple when a data does not change, like a constant or a factor

coordinates = (22.9,43.1) # Tuples as declare with parenthesis.

print(f'coordinate: {coordinates[0]} S\n            {coordinates[1]} W') # can acess the values of a tuple

# You can have a list of tuples

cities_coordinates = [(22.9,43.1), (40.7,74.0), (25.8,80.1)] #can change the list cities_coordinates but not the values of tuples

print(cities_coordinates)

cities_coordinates.append((50.9,1.4))

print(cities_coordinates)



## Funtions   Spyder doesn't support user input. Do not run on Spyder

def firstfunc(): # 'def' declare a function - name() of the function and parameters it will need
    print('Hello, what is your name?\n') #indented coding belong to the function
    name = input(':')
    print(f'\n Hi {name}, which Springboard course are you doing?\n')
    course = input(':')
    print(f'\n {course} is challenging, but your efforts will be rewarded.\n Good luck with your studies {name}')
    
    
# firstfunc() don't run in Spyder IDE. name() calls the function

def say_hello(name,language="english"): # functions parameters can have default values.
    if language == 'english':
        print(f'Hello {name}')
    elif language == 'portuguese':
        print(f'Oi {name}')
    elif language == 'spanish':
        print(f'Hola {name}')
    else:
        print(f'Sorry {name}, language not supported')
    
    
say_hello(name = 'Marcio', language = 'portuguese')
say_hello('Marcio', 'spanish')
say_hello("John")

say_hello('naruto', language="japanese")



## Return Statement - getting information from a function

def cube(x):
    return x*x*x # return statement allows the function to return the task the function did
                 # after return the function breakes, so nothing bellow return will run.
                 
print(cube(3))

result = cube(4)

result





