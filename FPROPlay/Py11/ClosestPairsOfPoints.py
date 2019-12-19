# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:18:55 2019

@author: filip
"""

import math 

def closest_pair(points):
    points.sort(key=lambda x: x[0])
    if len(points)==2:
        return math.sqrt((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
    
    mid = len(points) //2
    L = points[:mid]
    R = points[mid:]
    xdL = map()
    mL = closest_pair(L)
    mR = closest_pair(R)
    
    

print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))