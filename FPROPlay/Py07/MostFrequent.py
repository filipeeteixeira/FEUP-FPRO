#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:34:43 2019

@author: filipe
"""

def most_frequent(alist):
    dicto={}
    for i in alist:
        if i in dicto:
            dicto[i]+=1
        else:
            dicto.update({i:1})
    print(dicto)
    maxi=0
    value=0
    for i in dicto.keys():
        print(dicto[i])
        if dicto[i]>maxi:
            maxi=dicto[i]
            value=i
        elif dicto[i]==maxi:
            if i>value:
                value=i
            else:
                value=value
    return value

print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))