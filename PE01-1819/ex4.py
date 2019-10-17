#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:07:21 2019

@author: filipe
"""

tS=float(input())
tC=float(input())
tR=float(input())

vS=1.5/tS
vC=40/tC
vR=10/tR

time=tS+tC+tR

if (vS>=2.0 and vC>=20.0 and vR>=8.0 and time<=4.0):
    print(time)
elif time>4:
    print("Time")
elif vS<2:
    print("Swimming")
elif vC<20:
    print("Cycling")
elif vR<8:
    print("Running")