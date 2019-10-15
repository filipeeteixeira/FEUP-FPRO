#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:32:38 2019

@author: filipe
"""


def dogs(h_age):
    dog_age = 0
    for i in range(1, h_age+1):
        if(i < 3):
            dog_age+=10.5
        else:
            dog_age+=4
    return dog_age
            