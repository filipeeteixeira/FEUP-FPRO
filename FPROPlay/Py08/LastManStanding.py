# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:26:39 2019

@author: filip
"""

def last_man_standing(alist,step):
    if len(alist)==1:
        return alist[0]
    else:
        index=(0+step-1)%len(alist)
        return last_man_standing(alist[index+1:]+alist[:index],step)
    
print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))
    