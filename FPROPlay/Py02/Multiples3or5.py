#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:55:13 2019

@author: filipe
"""

def sum_multiples(n):
    soma=0;
    for i in range(1,n+1):
        if (i%3==0 or i%5==0):
            soma+=i
    return soma

print(sum_multiples(5))