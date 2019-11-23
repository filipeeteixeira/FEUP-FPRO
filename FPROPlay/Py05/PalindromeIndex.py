#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:40:31 2019

@author: filipe
"""

def is_palindrome(m):
    s=m[::-1]
    if m!=s:
        return False
    else:
        return True

def palindrome_index(s):
    if (is_palindrome(s)):
        return -1
    for i in range(0,len(s)):
        m=s[:i]+s[i+1:]
        if (is_palindrome(m)):
            return i
    return -1
