#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:19:16 2019

@author: filipe
"""

def jump(l):
    jumps=0
    index=0
    while(l[index]!=-1):
        index=l[index]
        jumps+=1
    return jumps
        