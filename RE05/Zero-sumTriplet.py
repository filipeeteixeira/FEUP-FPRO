#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:48:11 2019

@author: filipe
"""

def minorTriplet(lista):
    minorTriplet=lista[0]
    for i in lista:
        if i<minorTriplet:
            minorTriplet=i
    return minorTriplet

def is_inlist(lista,tuplee):
    tuplee=sorted(tuplee)
    for i in lista:
        if (tuplee==sorted(i)):
            return True
    return False

def triplet(atuple):
    list1=[]
    for i in range(0,len(atuple)):
        for k in range(0,len(atuple)):
            for j in range(0,len(atuple)):
                if (atuple[i]+atuple[k]+atuple[j]==0):
                    if is_inlist(list1,(atuple[i],atuple[k],atuple[j])):
                        continue
                    else:
                        list1.append((atuple[i],atuple[k],atuple[j]))
                    
    print(list1)
    return minorTriplet(list1)

print(triplet((-8, 0, 4, -2, -1, 1, 2)))


        