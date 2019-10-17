#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 00:19:18 2019

@author: filipe
"""

dec=input()

string=""
while(int(dec)//2!=0):
    string+=str(int(dec)%2)
    dec=int(dec)//2
string+=str(int(dec)%2)
string=string[::-1]
print(string)



