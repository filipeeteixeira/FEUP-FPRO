# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:01:17 2019

@author: filip
"""

def mapp(pos,steps):
    if steps==[]:
        return pos
    if steps[0]=='up':
        return mapp((pos[0],pos[1]+1),steps[1:])
    elif steps[0]=='down':
        return mapp((pos[0],pos[1]-1),steps[1:])
    elif steps[0]=='left':
        return mapp((pos[0]-1,pos[1]),steps[1:])
    elif steps[0]=='right':
        return mapp((pos[0]+1,pos[1]),steps[1:])
    
print(mapp((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))