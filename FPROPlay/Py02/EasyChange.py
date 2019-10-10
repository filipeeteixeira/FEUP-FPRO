#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:01:11 2019

@author: filipe
"""

price= int(input())
received = int(input())

to_give= received-price

notes50=0
notes20=0
notes10=0
notes5=0

while(to_give-50>=0):
        notes50+=1
        to_give-=50
while(to_give-20>=0):
    notes20+=1
    to_give-=20
while(to_give-10>=0):
    to_give-=10
    notes10+=1
while(to_give-5>=0):
    to_give-=5
    notes5+=1

string = str(notes50) + " " + str(notes20) + " " + str(notes10) + " " + str(notes5)
print(string)

#better code 
#def easy_change(price, received):
#    received -= price
#    notes = [50,20,10,5]
#    amount = ""
#    for note in notes:
#        amount += " %d" %(received // note)
#        received = received % note
#    return amount