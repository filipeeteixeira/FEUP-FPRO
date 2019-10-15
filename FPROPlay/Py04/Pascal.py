#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 00:52:10 2019

@author: filipe
"""

import math

def pascal(n):
    line=""
    for i in range(0,n):
        for j in range(0,i+1):
            line+=str(math.factorial(i)//(math.factorial(j)*(math.factorial(i-j))))
            if (j==i and i!=n-1):
                line+="\n"
            else:
                line+=" "
    return line

print(pascal(5))
        