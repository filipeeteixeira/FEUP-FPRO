#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:20:07 2019

@author: filipe
"""

num=int(input())

x0=num/2

x1=(x0+num/x0)/2

while (round(x1,2)!=round(x0,2)):
    x0=x1
    x1=(x0+num/x0)/2

print(round(x1,3))