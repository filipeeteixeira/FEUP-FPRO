# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:56:37 2019

@author: filip
"""

def sum_digits_rec(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sum_digits_rec(number//10)
    

print(sum_digits_rec(12))