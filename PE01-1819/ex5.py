#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:38:03 2019

@author: filipe
"""

dec=input()


num=""

while(int(dec)//8!=0):
    num+=str(int(dec)%8)
    dec=int(dec)//8

num+=str(int(dec)%8)

num=num[::-1]

print(int(num))
    