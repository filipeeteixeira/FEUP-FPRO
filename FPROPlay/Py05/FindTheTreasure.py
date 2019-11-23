#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:24:14 2019

@author: filipe
"""

def map(pos,steps):
    cordX=pos[0]
    cordY=pos[1]
    steps=steps.split("-")
    for i in steps:
        if i=="up":
            cordY+=1
        elif i=="left":
            cordX+=-1
        elif i=="right":
            cordX+=1
        elif i=="down":
            cordY+=-1
    return (cordX,cordY)
            
    
