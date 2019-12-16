# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:05:04 2019

@author: filip
"""

def binary_tree(key,tree):
    if key == tree[0]:
        return tree[1]
    else:
        if key < tree[0]:
            return binary_tree(key,tree[2]())
        else:
            return binary_tree(key,tree[3]())

print(binary_tree('a',('m',1,lambda: ('b',2,lambda: ('a',1,lambda:1/0,lambda:1/0),lambda:1/0),lambda:('o',3,lambda:1/0,lambda:1/0))))
