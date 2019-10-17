#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:29:28 2019

@author: filipe
"""

num=input()

soma=0
for i in num:
    soma+=int(i)*int(i)*int(i)

print(soma)
if soma==int(num):
    flag=True
else:
    flag=False

print(flag)