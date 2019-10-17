#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:51:47 2019

@author: filipe
"""

L = int(input())
S = int(input())

R=L

if(R>S):
    while(S<=R):
        R=R-S
        if S>R:
            if R!=0:
                L=R
                R=S
                S=L
else:
    L=R
    R=S
    S=L
    while(S<=R):
        R=R-S
        if S>R:
            if R!=0:
                L=R
                R=S
                S=L
print(S)