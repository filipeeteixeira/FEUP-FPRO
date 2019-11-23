#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:10:40 2019

@author: filipe
"""

def count_until(tup):
    count=0
    for i in tup:
        if (type(i)==tuple):
            return count
        if (type(i)!=tuple):
            count+=1
    if(tup==() or count==len(tup)):
        return -1
        
