#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:38:42 2019

@author: filipe
"""

num=input()

counter=0
for i in range(0,len(num)-1):
    if num[i]==num[i+1]:
        counter+=1

print(counter)

