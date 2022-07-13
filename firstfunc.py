#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:05:54 2022

@author: marciobernardo
"""

# Can run in any Python IDLE

def firstfunc():  #'def'  
    print('Hello, what is your name?\n')
    name = input()
    print(f'\n Hi {name}, which Springboard course are you doing?\n')
    course = input()
    print(f'\n {course} is challenging, but your efforts will be rewarded.\n Good luck with your studies {name}')
    
    
firstfunc()
