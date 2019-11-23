#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:02:00 2019

@author: filipe
"""

def get_left(alist,n,index):
    if index<n-3:
        leftList=alist[:index]
    else:
        leftList=alist[index-n//2:index]
    return leftList

def get_right(alist,n,index):
    if index>len(alist)-3:
        leftList=alist[index+1:]
    else:
        leftList=alist[index+1:index+n//2+1]
    return leftList

def is_local_minima(left,right,n):
    for i in left:
        if n<=i:
            continue
        else:
            return False
    for k in right:
        if n<=k:
            continue
        else:
            return False
    return True
        
def local_minima(alist,n):
    resultList=[]
    for i in range(0,len(alist)):
        left=get_left(alist,n,i)
        right=get_right(alist,n,i)
        if (is_local_minima(left,right,alist[i])):
            resultList.append((alist[i],i))
    return resultList
        
print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))