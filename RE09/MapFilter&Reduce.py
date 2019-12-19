# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:50:16 2019

@author: filip
"""
from functools import reduce

def reduce_map_filter(args):
    if type(args[2])!= list:
        args = (args[0],args[1],reduce_map_filter(args[2]))
    if args[0] == 'map':
        return list(map(args[1],args[2]))
    elif args[0] == 'filter':
        return list(filter(args[1],args[2]))
    elif args[0] == 'reduce':
        return reduce(args[1],args[2])
    
print(reduce_map_filter(('filter', lambda x: x%2 == 0, ('filter', lambda x: x >= 0, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10]))))