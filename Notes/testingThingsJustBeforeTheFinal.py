from cs115 import *
import copy

print(reduce(lambda x,y: x+y, [200,300,400]))
def fail():
    for i in range(10):
        return i


def factorial(n):
    '''Recursive function for computing
    the factorial of n.'''
    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

print (factorial(4))


def subset(capacity, items):
    if capacity <= 0 or items == []:
        return 0
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        loseIt = subset(capacity, items[1:])
        useIt = items[0] + subset(capacity - items[0], items[1:])
        return max(loseIt, useIt)


print (subset(4, [1, 2]))

listA = ['a','b','c','d','e']
listB = list(listA)
listC = [['a','b'],['c','d']]
listD = list(listC)
