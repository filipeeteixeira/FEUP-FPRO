#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:59:59 2019

@author: filipe
"""

side1=int(input())
side2=int(input())
side3=int(input())

if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
    if side1==side2 and side2==side3:
        print("Equilateral")
    elif side1==side2 or side1==side3 or side2==side3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")
