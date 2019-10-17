#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 00:10:07 2019

@author: filipe
"""

inputA=input()
inputB=input()

if inputA==inputB:
    print("That's a draw")
elif inputA=="rock" and inputB=="scissors":
    print("The winner is A")
elif inputA=="rock" and inputB=="paper":
    print("The winner is B")
elif inputA=="scissors" and inputB=="paper":
    print("The winner is A")
elif inputA=="scissors" and inputB=="rock":
    print("The winner is B")
elif inputA=="paper" and inputB=="rock":
    print("The winner is A")
elif inputA=="paper" and inputB=="scissors":
    print("The winner is B")