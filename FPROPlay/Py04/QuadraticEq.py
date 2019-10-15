#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:41:37 2019

@author: filipe
"""

import math

def solver(a, b, c):
    result= []
    if (b**2-4*a*c<0):
        return result
    elif (b**2-4*a*c==0):
        return [-b/(2*a)]
    elif (a==0):
        result.append(-c/b)
    else:
        result.append((-b+math.sqrt(b**2-4*a*c))/(2*a))
        result.append((-b-math.sqrt(b**2-4*a*c))/(2*a))
        result.sort()
    return result