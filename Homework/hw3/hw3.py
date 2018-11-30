'''
Created on 2018-09-26
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Hw 3
'''
from cs115 import *
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == [] or scores == []:
        return []
    else:
        scoresOfWords = listOfScores(dct, scores)
        return [[dct[0], scoresOfWords[0]]] + wordsWithScore(dct[1:], scores)

    
def letterScore(letter, scorelist):
    '''Returns a list containing the given character and the
    Scrabble score for the given letter
    input letter: a character
    input scorelist: a list of letters and their Scrabble scores'''
    # I recognize that the function is allowed to crash if the given
    # letter is not in scorelist, but I wanted to be able to catch that
    if letter == [] or letter == '':
        return 0
    elif letter not in alphabet:
        print("You entered an invalid character! Try again.")
        return 0
    elif (scorelist[0])[0] == letter:
        return (scorelist[0])[1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    '''Returns the Scrabble score of a given string
    input S: a string
    input scorelist: a list of letters and their Scrabble scores'''
    if S == '' or S == []:
        print("You didn't enter a word! That's zero points.")
        return 0
    elif len(S) == 1:
        return letterScore(S, scorelist)
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def listOfScores(words, scorelist):
    '''Returns a list of scores for a given list of words
    input words: a list of words
    input scorelist: a list of letter, number pairs'''
    if words == [] or scorelist == []:
        return []
    else:
        return [wordScore(words[0], scorelist)] + listOfScores(words[1:], scorelist)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 or L == []:
        return []
    elif n == 1:
        return [L[0]]
    else:
        return [L[0]] + take(n-1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L == []:
        return []
    elif n == 0:
        return L
    else:
        return drop(n-1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 4
' Write another version of the change function called giveChange
' that takes the same kind of input as change but returns a list
' whose first item is the minimum number of coins and whose second
' item is a list of the coins in that optimal solution.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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


def giveChange(amount, coins):
    '''Returs a list consisting of the minimum number of coins required
    to achieve the given amount and the values of the coins used to achieve
    the given amount.
    input amount: an whole number
    input coins: a list of whole numbers, where coins[0] == 1'''
    if amount == 0:
        return [0, []]
    elif amount < 0 or coins == []:
        return [float("inf"), []]
    elif coins == []:
        return [float("inf"), []]
    elif (amount-coins[0] < 0):
        return giveChange(amount, coins[1:])
    else:
        useIt = giveChange(amount - coins[0], coins)
        useIt = [useIt[0] + 1,[coins[0]] + useIt[1]]
        loseIt = giveChange(amount, coins[1:])
        if loseIt[0] < useIt[0]:
            return loseIt
        else:
            return useIt
