#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:22:04 2019

@author: filipe
"""

n = int(input())

def looping_number(n):
    while (n > 0):
        if(n>=100 and (abs((n % 10)-(n//10)%10)==1 or abs((n % 10)-(n//10)%10)==9)):
            n = n // 10
            continue
        elif (n<100 and (abs((n % 10)-(n//10))==1 or abs((n % 10)-(n//10))==9)):
            return "Looping number"
        else:
            return "Not a looping number"
