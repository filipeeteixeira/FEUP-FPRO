#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:51:52 2019

@author: filipe
"""

def min_path(path):
    i=0
    while i<len(path):
        tmp=path[i:i+2]
        if 'UP' in tmp and 'DOWN' in tmp:
            path=path[:i]+path[i+2:]
            i-=1
        elif 'LEFT' in tmp and 'RIGHT' in tmp:
            path=path[:i]+path[i+2:]
            i-=1
        else:
            i+=1
        
    return path

print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))