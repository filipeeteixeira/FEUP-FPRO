#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:36:09 2019

@author: filipe
"""
d=input()
num=input()

soma=0
for i in num:
    if int(i)>int(d):
        soma+=2*int(i)

print(soma)
        

