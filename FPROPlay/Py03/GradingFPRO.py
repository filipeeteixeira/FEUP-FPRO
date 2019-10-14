#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:36:09 2019

@author: filipe
"""

import math

LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

def fproGrade(LE,RE,PE,TE):
    if (LE>=0 and LE<=100 and RE>=0 and RE<=100 and PE>=0 and PE<=100 and TE>=0 and TE<=100):
        grade = (LE + RE + 5*PE + 3*TE)/50
    else:
        return "Input error"
    
    if (PE<40 or TE<40):
        return "RFC"
    elif(grade%1>=0.5):
        return math.ceil(grade)
    else:
        return math.floor(grade)
    
print(fproGrade(LE,RE,PE,TE))