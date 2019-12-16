# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:14:15 2019

@author: filip
"""
def pref(str1,str2):
    while(len(str1)!=len(str2)):
        if len(str1)>len(str2):
            str1=str1[:len(str1)-1]
        else:
            str2=str2[:len(str2)-1]

    while(str1!=str2):
        str1=str1[:len(str1)-1]
        str2=str2[:len(str2)-1]
    return str1

def commonPrefix(arr, low, high):  
  
    if low == high: 
        return arr[low]
  
    if high > low:
        mid = low + (high - low) // 2
  
        str1 = commonPrefix(arr, low, mid)  
        str2 = commonPrefix(arr, mid + 1, high)  
  
        return pref(str1, str2)

def longest_prefix(words):
    n = len(words)
    ans = commonPrefix(words, 0, n - 1)
    return ans

print(longest_prefix(['apple', 'apply', 'ape', 'april']))
    