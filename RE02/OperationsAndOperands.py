#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:20:51 2019

@author: filipe
"""
#   P= principal amount(initial investment)
#   r= annual nominal interest rate(as a decimal)
#   n= number of times the interest is compounded per year
#   t= number of years
#   A= new principal amount(final result)

t = 2

P = float(input("Insert the principal amount: "))

n = int(input("number of times the interest is compounded per year: "))

r = float(input("Annual nominal interest rate(as decimal): "))
#t=int(input("number of years: "))

A = P * ((1 + (r/n)) ** (n*t))

A = round(A,3)

print(A)