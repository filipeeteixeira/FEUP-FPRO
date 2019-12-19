#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:17:22 2019

@author: filipe
"""

def gcd(a, b):
    if a>b:
        rem=a%b
        if rem==0:
            return min(a,b)
        else:
            return gcd(rem,b)
    else:
        rem=b%a
        if rem==0:
            return min(a,b)
        else:
            return gcd(a,rem)

print(gcd(65,26))
    