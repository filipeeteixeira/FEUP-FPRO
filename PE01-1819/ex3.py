#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:00:18 2019

@author: filipe
"""

names=["bart","marie","jo"]
ages=["23","75","19"]

string=""
for i in range(0,len(names)):
   string+=names[i]+"-"+ages[i]+" "

string=string[:len(string)-1]
print(string)
    