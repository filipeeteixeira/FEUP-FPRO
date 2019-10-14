#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:19:46 2019

@author: filipe
"""

lower = int(input())
upper = int(input())

def is_prime(n):
    if n==1 or n<0 or n==0:
        return False
    else:
        for j in range(0,n):
            for k in range(0,n):
                if j*k==n:
                    return False
        return True

final = ""
for i in range(lower,upper+1):
    if is_prime(i):
        final+=str(i)+ " "

print("Prime numbers between " + str(lower) + " and " + str(upper) + " are: " + final)