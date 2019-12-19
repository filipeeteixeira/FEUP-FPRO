# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:57:56 2019

@author: filip
"""

def fight(heroes,villain):
    for i in heroes:
        if i['category']==villain['category']:
            if i['health']>villain['health']:
                i['score']+=1
                return "{h} defeated the villain and now has a score of {s}".format(h=i['name'],s=i['score'])
            elif i['health']<villain['health']:
                villain['health']-=round(i['health']/2,1)
            elif i['health']==villain['health']:
                i['score']+=1
    return "{v} prevailed with {hp}HP left".format(v=villain['name'],hp=villain['health'])

print(fight([{'name': 'Genos', 'health': 5500, 'category': 'S', 'score': 0}, {'name': 'King', 'health': 7000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))