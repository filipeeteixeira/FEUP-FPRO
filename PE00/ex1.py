#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:32:05 2019

@author: filipe
"""

num = int(input())

ints = [1, 2, 2, 3, 5, 9, 13, 21, 34]

string1="Less:"
string2="Greater:"
for i in ints:
    if i < num:
        string1+= " " + str(i)
    elif (i>num):
        string2+= " " + str(i)

print(string1 + "\n" + string2)