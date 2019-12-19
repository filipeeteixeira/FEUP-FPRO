# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:47:13 2019

@author: filip
"""

def invoice_totals(orders,minn):
    return list(map(lambda x: (x[0],x[2]*x[3]+10) if x[2]*x[3] < minn else (x[0],x[2]*x[3]),orders))
    

print(invoice_totals([[32341, 'The Adventures of Augie March, Saul Bellow', 4, 40.95], [45432, "All the King's Men, Robert Penn Warren", 5, 56.8], [93834, 'American Pastoral, Philip Roth', 3, 32.95], [35322, 'An American Tragedy, Theodore Dreiser', 3, 24.99]], 500))