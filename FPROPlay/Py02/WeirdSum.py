#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 01:11:10 2019

@author: filipe
"""

a= int(input())
b= int(input())

prod=a*b

while( (a-b)%2==0):
    result=(a+b)*2
    break
while((a-b)%2!=0):
    result=prod+a+b
    break

print(result)