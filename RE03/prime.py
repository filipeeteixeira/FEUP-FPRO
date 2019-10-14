#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:31:43 2019

@author: filipe
"""

num=int(input())

def is_prime():
    if (num==1):
        return False
    for i in range(0,num):
        for k in range(0,num):
            if i*k==num:
                return False
    return True

print(is_prime())