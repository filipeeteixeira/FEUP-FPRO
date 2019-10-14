#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:11:52 2019

@author: filipe
"""


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def C(n,r):
    result=factorial(n)/(factorial(r)*factorial(n-r))
    return int(result)

