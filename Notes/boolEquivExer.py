'''
boolEquivExer.py simple equivalence checking for boolean functions
D.Naumann Oct 2018
'''
from cs115 import *

# These examples are about functions intended to be applied to,
# and return, boolean values. 

def f0(x,y,z):
    return not x and not (y or z)

def f1(x,y,z):
    return not x and (not y and not z)

# Some inputs for testing
t0 = [0,0,0]
t1 = [1,1,1]

# TRY THIS in the shell:  f0(t0)  what goes wrong? why?







def test_f(trip):
    '''Assuming trip is a list of 3 booleans, check whether
    f0 and f1 give the same result on trip.'''
    return f0(*trip) == f1(*trip)     # use the unpacking operator 

def allTuples(n):
    '''Return a list of all n-lists of ones and zeros, in increasing
    order.  For example, allTuples(2) is [[0,0],[0,1], [1,0], [1,1]].
    Assume n>=0.
    Note: another option would be to use tuples.'''
    if n == None:
        return (())
    elif n == 0:
        return (0,0)
    else:
        return 

def test_f_all():
    return map(test_f, allTuples(3))
    
    
