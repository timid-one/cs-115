# Andrew Chinique
# Professor Naumann
# Introduction to Computer Science
# 13 September 2018
#                                   Lab 2
# I pledge my honor that I have abided by the Stevens Honor System.
#                                               --Andrew Chinique

#########################################################################

from cs115 import *


def myLen(L):
    '''Return the length of given sequence L
    input L: a sequence (list or string)'''
    if L == [] or L == '':
        return 0
    else:
        return 1 + myLen(L[1:])

def shorten(L, K):
    '''shortens the longer of sequence L and K to the length of the shorter sequence
    if both lists are of equal length, returns the first list. BE CAREFUL!
    input L: a sequence (list or string)
    input K: a sequence (list or string)'''
    if L == [] or K == []:
        return []
    elif myLen(L) == myLen(K):
        return 
    elif myLen(L) > myLen(K):
        return L[:myLen(K)]
    else:
        return K[:myLen(L)]
    
def dot(L, K):
    '''Returns the dot product of two numerical lists of equal length.
    If both lists are empty, returns zero. If the lists are of different lengths,
    prints an error message and returns nothing.
    input L: list of numbers
    input K: list of numbers'''
    if L == [] or K == []:
        return 0.0
    elif (myLen(L) != myLen(K)):
        J = shorten(L,K)
        if L[0] == J[0]:
            return J[0] * K[0] + dot(J[1:], K[1:])
        else:
            return L[0] * J[0] + dot(L[1:], J[1:])
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    '''Returns a list of all characters that make up a given string
    input S: a string'''
    if S == '':
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def ind(e, L):
    '''Returns the index at which element e FIRST occurs.
    If e is not an element of L, returns an integer equal to len(L).
    input e: an element
    input L: a sequence (list or string)'''
    counter = 0
    if L == [] or L == '':
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''Returns a list identical to list L without all top-level instances of e
    input e: an element
    input L: a list'''
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def even(X):
    if X % 2 == 0:
        return True
    else:
        return False

def myFilter(f, L):
    '''Replicates the built-in filter function
    returns a new list containing all elements L for which function f returns True
    input f: a function that returns a boolean
    input L: a list'''
    if L == []:
        return []
    elif f(L[0]) == True:
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])

def deepReverse(L):
    '''Returns a list identical to the reverse of given list L;
    this includes reversing the contents of any list elements within list L
    input L: a list'''
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
