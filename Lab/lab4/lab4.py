'''
Created on 2018-09-26
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Hw 3
'''
from cs115 import *

# knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]])
def knapsack(capacity, itemList):
    '''returns a list containing the maximum possible sum of values
    limited by the capacity, as well as a list of lists denoting the
    weights and values of the items composing the max value.
    input capacity: a whole number
    input itemList: a list of two-element lists, each of which contains
    a whole number integer'''
    #ex: [[1,33], [4,66], [2,77] weights are 1,4,2; values are 33, 66, 77
    if capacity == 0 or itemList == []:
        return [0, []]
    elif capacity - (itemList[0])[0] < 0:
        return knapsack(capacity, itemList[1:])
    else:
        loseIt = knapsack(capacity, itemList[1:])
        useIt = knapsack(capacity - (itemList[0])[0], itemList[1:])
        useIt2 = [useIt[0] + (itemList[0])[1], [itemList[0]] + useIt[1]]
        if loseIt[0] > useIt2[0]:
            return loseIt
        else:
            return useIt2
