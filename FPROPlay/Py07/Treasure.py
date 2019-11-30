# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:56:55 2019

@author: filip
"""

def treasure(clues):
    step=(0,0)
    listt=[]
    listt.append(step)
    while step in clues:
        step=clues[step]
        print(step)
        if step in listt:
            return step
        listt.append(step)
    return step

print(treasure({(-1, 1): (0, 0), (0, 0): (1, 0), (1, 0): (-1, 1)}))
        