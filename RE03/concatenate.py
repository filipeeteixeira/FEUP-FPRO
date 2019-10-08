#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:09:42 2019

@author: filipe
"""

n1=int(input())
n2=int(input())

save_n2=n2

n2_digits=1
while n2//10 != 0:
    n2_digits+=1
    n2=n2//10
    
concat1 = n1 * 10**n2_digits
concat2 = save_n2

result= concat1+concat2
print(result)