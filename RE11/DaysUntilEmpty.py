# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:53:09 2019

@author: filip
"""

def days_until_empty(c, l):
    day=0
    tank=c
    while (tank>0):
        day+=1
        tank+=l
        if (tank>c):
            tank=c  
        tank-=day
    return day
        