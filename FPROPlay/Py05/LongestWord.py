#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:27:04 2019

@author: filipe
"""

def longestInlist(alist):
    longest=alist[0]
    for i in alist:
        if(len(i)>=len(longest)):
            longest=i
    return longest

def longest(s):
    lista=[]
    s=s+" "
    
    for i in s:
        if(i==" "):
            lista.append(s[0:s.index(i)])
            s=s[s.index(i)+1:]
    return len(longestInlist(lista))

print(longest("A list with some words"))