#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:39:44 2019

@author: filipe
"""

def mastermind(g1,g2,g3,c1,c2,c3):
    points=0
    guess=[g1,g2,g3]
    r=[c1,c2,c3]
    for i in guess:
        for k in r:
            print("i:",i)
            print("k:", k)
            
            if i==k:
                if guess.index(i)==r.index(k):
                    points+=3
                    break
                else:
                    points+=1
                    break
        print(points)
    return points

print(mastermind("b","b","y","b","w","b"))