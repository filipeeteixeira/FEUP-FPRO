#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:56:33 2019

@author: filipe
"""

        
def collatz(n):
    string=str(n)
    while(n!=1):
        if (n%2==0):
            string+=","+str(n//2)
            n=n//2
        else:
            string+=","+str(n*3+1)
            n=n*3+1
    return string
        
print(collatz(3))