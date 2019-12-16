# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:25:10 2019

@author: filip
"""

def bubble_sort(alist):
    flag=True
    while flag==True:
        flag=False
        for i in range(0,len(alist)-1):
            if alist[i+1]<alist[i]:
                tmp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=tmp
                flag=True
            else:
                continue
    return alist

print(bubble_sort([5, 1, 2, 8, 2.5]))
            