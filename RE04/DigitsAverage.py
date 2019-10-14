#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:02:55 2019

@author: filipe
"""
import math

def roundd(n):
    if(n%1>=0.5):
        return math.ceil(n)
    else:
        return math.floor(n)

def num_digits(m):
    digits=1
    while(m//10!=0):
        digits+=1
        m=m/10
    return digits

def next_line(n):
    p=0
    NextLine=0
    while(n//10!=0):
        n1=n%10
        n=n//10
        NextLine+=roundd((n1+(n%10))/2)*10**p
        p+=1
    return NextLine

def digits_average(n):
    while (num_digits(n)!=1):
        newLine=next_line(n)
        n=newLine
    return n
print(digits_average(158))