'''
Created on 2018-10-23
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Hw 7
'''
from cs115 import *

def numToBaseB(N, B):
    '''Converts a given number N from base 10 to given base B. Returns the
    output as a string.
    input N: a whole number
    input B: an integer ranging from 2 to 10, inclusive'''
    def nTBB(N,B):
        if N == 0:
            return ''
        elif B == 10:
            return str(N)
        else:
            return nTBB(N//B, B) + str(N%B)
    if N == 0:
        return '0'
    return nTBB(N, B)

def baseBToNum(S, B):
    '''Returns the integer corresponding to the base 10 representation of
    string S. Note: the empty string represents 0.
    input S: a string representative of a number in base B
    input B: an integer ranging from 2 to 10, inclusive'''
    if S == '':
        return 0
    else:
        return baseBToNum(S[:-1], B) * B + int(S[-1:])

def baseToBase(B1, B2, SinB1):
    '''Converts given string SinB1 from base B1 to base B2 and returns this as
    a string.
    input B1: an integer ranging from 2 to 10, inclusive.
    input B2: an integer ranging from 2 to 10, inclusive
    input SinB1: a string representative of a number in base B1'''
    if B2 == B1:
        return SinB1
    elif SinB1 == '0':
        return SinB1
    else:
        return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    '''Returns the sum of two binary strings as a binary string.
    input S: a string consisting of ones and zeros
    input T: a string consisting of ones and zeros'''
    SinDec = baseBToNum(S, 2)
    TinDec = baseBToNum(T, 2)
    sumInDec = SinDec + TinDec
    return numToBaseB(sumInDec, 2)

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = { ('0','0','0') : ('0','0'), ('0','0','1') : ('1','0'), \
              ('0','1','0') : ('1','0'), ('0','1','1') : ('0','1'), \
              ('1','0','0') : ('1','0'), ('1','0','1') : ('0','1'), \
              ('1','1','0') : ('0','1'), ('1','1','1') : ('1','1') }

def addB(S,T):
    '''Returns the sum of two binary strings as a binary string,
    without using base conversion.
    input S: a string consisting of ones and zeros
    input T: a string consisting of ones and zeros'''
    if T == '' or int(T) == 0:
        return S
    elif S == '' or int(S) == 0:
        return T
    elif len(T) < len(S):
        paddedT = '0'*(len(S)-len(T)) + T
        return addB(S, paddedT)
    elif len(S) < len(T):
        paddedS = '0'*(len(T)-len(S)) + S
        return addB(paddedS, T)
    def addBwithCarry(S,T,C):
        if S == '':
            if C == '1':
                return '1'
            return ''
        answer = addBwithCarry(S[:-1], T[:-1], FullAdder[(S[-1], T[-1], C)][1]) + \
        FullAdder[(S[-1], T[-1], C)][0]
        return str(int(answer))
    return addBwithCarry(S,T,'0')
