# Andrew Chinique
# [teacher name]
# [class name]
# [due date]
#                                   Lab 3
# I pledge my honor that I have abided by the Stevens Honor System.
#                                               -- Andrew Chinique

#########################################################################
from cs115 import *

def change(amount, coins):
    '''returns a non-negative integer indicating the minimum number
    of coins required to make up the given amount
    input amount: a non-negative integer
    input coins: a list of coin values, where coins[0] == 1'''
    if amount == 0:
        return 0
    elif amount < 0 or coins == []:
        return float("inf")
    elif coins == []:
        return float("inf")
    else:
        useIt = 1 + change(amount-coins[0], coins)
        loseIt = change(amount, coins[1:])
        return min(useIt, loseIt)
        
