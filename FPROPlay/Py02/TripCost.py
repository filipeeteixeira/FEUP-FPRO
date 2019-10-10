#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:47:53 2019

@author: filipe
"""

def trip_cost(distance, litres_100km, price): 
    distance_100km = distance/100
    litres = distance_100km*litres_100km
    total_price=price*litres
    return  total_price