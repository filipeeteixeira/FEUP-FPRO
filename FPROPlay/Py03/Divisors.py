#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:19:21 2019

@author: filipe
"""

num = int(input())

soma=0

for i in range(1,num+1):
    if(num%i==0):
        soma+=i
print(soma)