#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:57:18 2019

@author: filipe
"""

def knapsack(money,products,wishlist):
    new_money=0
    while(new_money<money):
        for i in products.keys():
            if i in wishlist.keys():
                new_money=money-products[i]*wishlist[i]
