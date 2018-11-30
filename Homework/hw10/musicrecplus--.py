'''
Author: Andrew Chinique @achiniqu
Instructor: Professor Naumann
Course: Introduction to Computer Science
Created On: 2018-11-09

Homework 10
'''
from cs115 import *

def intersect(L, M):
    '''returns a list containing the common items within each given list
    INPUT L: a list
    INPUT M: a list'''
    result = []
    for x in L:
        for y in M:
            if x==y:
                result = result + [x]
    return result

def intersect2(L,M):
    return filter(lambda x: x in M, L)

def intersect3(L,M):
    result = []
    indexL = 0
    indexM = 0
    while i < len(L) and j < len(M):
        if L[i] == M[j]:
            result = result + [L[i]]
        elif L[i] < M[j]:
            i += 1
        else:
            j+=1
