# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:24:23 2019

@author: filip
"""

def find_me(f,limits):
    mid=(limits[0]+limits[1])//2
    if (f(mid)==0):
        return 0
    if (f(mid)==-1):
        return 1 + find_me(f,(limits[0],mid))
    return 1 + find_me(f,(mid,limits[1]))
        
    
print(find_me())