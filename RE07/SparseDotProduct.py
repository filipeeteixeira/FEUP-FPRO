#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:04:59 2019

@author: filipe
"""

def sparse_dot_product(dict1,dict2):
    dot=0
    for i in dict1.keys():
        for k in dict2.keys():
            if i==k:
                dot+=dict1[i]*dict2[k]
    return dot

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))