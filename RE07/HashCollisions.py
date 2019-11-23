#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:34:07 2019

@author: filipe
"""

def sumN(n):
    n=str(n)
    soma=0
    for x in n:
        soma+=int(x)
    return soma

def collisions(alist):
    dictionary={}
    for i in range(0,len(alist)):
        newkey=sumN(alist[i])%8
        if newkey not in dictionary:
            dictionary[newkey]=1
        elif newkey in dictionary:
            dictionary[newkey]+=1
    return dictionary

print(collisions([1, 789, 100, 9807, 1208, 92, 101]))