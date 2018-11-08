from cs115 import *
from math import *

def mapSqr(L):
    '''return map(sqr, L)'''
    m = []
    for i in L:
        iSqr = i**2
        m = m + [iSqr]
    return m

def factorial(n):
    if n < 0:
        return None
    result = 1
    if n == 0 or n == 1:
        return result
    for i in range(1, n+1):
        result = result * i
    return result
