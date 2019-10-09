#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:55:22 2019

@author: filipe
"""



def add(a,b):
    if a!=b:                    
        return (a*a-b*b)/(a-b)
    else:
        return 2*a      

a=int(input())
b=int(input())
print(int(add(a,b)))
    
#print(a-(-b))
