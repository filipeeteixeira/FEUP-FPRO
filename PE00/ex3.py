#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:41:29 2019

@author: filipe
"""

integers = [0, 2, 9, 15, 64]
reals = [0.0, 3.2, 8.4, 15.5, 128.0]

counter=0
for i in reals:
    counter+=1

string=""
for k in range(0,counter):
    if integers[k]>reals[k]:
        string+= str(integers[k]) + " "
    elif integers[k]<reals[k]:
        string+= str(reals[k]) + " "
    elif type(integers[k])==float:
        string+= str(reals[k]) + " "
    else:
        string+= str(int(reals[k])) + " "

string=string[:len(string)-1]

print(string)
            