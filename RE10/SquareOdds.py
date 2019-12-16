# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:17:55 2019

@author: filip
"""

def square_odds(values):
    return [int(i)*int(i) for i in values.split(',') if int(i)%2!=0]

print(square_odds('8,9,11'))