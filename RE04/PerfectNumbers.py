#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:46:56 2019

@author: filipe
"""

def is_perfect(n):
    soma=0
    for i in range(1,n):
        if(n%i==0):
            soma+=i
            print(soma)
    if soma==n:
        return True
    else:
        return False

print(is_perfect(6))