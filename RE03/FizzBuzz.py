#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:45:56 2019

@author: filipe
"""

num=int(input())

final_string=''

for i in range(1,num+1):
    if (i%3==0):
        final_string+= 'Fizz '
    elif(i%5==0):
        final_string+= 'Buzz '
    else:
        final_string+= str(i) + ' '
print(final_string)
    