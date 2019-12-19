# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:56:40 2019

@author: filip
"""
def sort_rule(item):
    return item[1]

def make_wishlist(products,wishlist):
    wish={}
    for i in products:
        if i in wishlist:
            wish.update({i:products[i]})
    return sorted(wish.items(),key=sort_rule,reverse=False)


def budgeting(budget,products,wishlist):
    money_needed=0
    for i in wishlist:
        money_needed+=products[i]*wishlist[i]
        
    if money_needed<=budget:
        return wishlist
    else:
        list_prices=make_wishlist(products,wishlist)
        while money_needed>budget:
            wishlist[list_prices[0][0]]-=1
            if wishlist[list_prices[0][0]]==0:
                del wishlist[list_prices[0][0]]
                money_needed-=list_prices[0][1]
                list_prices.remove(list_prices[0])
                continue
            money_needed-=list_prices[0][1]
    return wishlist

print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
        
        