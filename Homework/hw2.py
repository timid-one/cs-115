'''
Created on 2018-09-15
@author:   Andrew Chinique
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        --Andrew Chinique

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
import dict
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

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

##Dictionary = dict.Dictionary

# Implement your functions here

# Helper Functions

def appears(e, L):
    '''Returns a boolean whether or not element e appears in a sequence
    input e: an element
    input L: a sequence (list or string)'''
    if L == [] or L == '':
        return False
    elif L[0] == e:
        return True
    else:
        return appears(e, L[1:])

    
def breakdown(S):
    '''Returns a list of all characters that make up a given sequence
    input S: a sequence'''
    if S == '' or S == []:
        return []
    elif len(S) == 1:
        return [S]
    else:
        return S[0] + breakdown(S[1:])


def removeFirst(e, L):
    '''Returns a list identical to list L
    without the first top-level instance of e.
    input e: an element
    input L: a list'''
    if L == []:
        return []
    elif L == '':
        return ''
    elif L[0] == e:
        return L[1:]
    elif isinstance(L, list) == True:
        return [L[0]] + removeFirst(e, L[1:])
    else:
        return L[0] + removeFirst(e, L[1:])

    
def listCompose(Rack, S):
    '''Checks whether or not string S can be composed from list R.
    Returns the string if this is true; returns an empty string if false.
    input Rack: a list of lowercase letters
    input S: a string'''
    # in the case of this HW:
        # Rack would be the rack of Scrabble tiles
        # S is any word
    if S == [] or S == '':
        return ''
    elif (S[0] in Rack):
        trimmedRack = removeFirst(S[0],Rack)
        if (S[0] + listCompose(trimmedRack, S[1:])) == S:
            return(S[0] + listCompose(trimmedRack, S[1:]))
        else:
            return listCompose(trimmedRack, S[1:])
    else:
        return ''


def inDictionary(Words):
    '''Tests if string in list Words is a word, as defined by Dictionary.
    Returns the string if true.
    input S: a list of strings'''
    if Words == []:
        return []
    elif Words[0] in Dictionary:
        return [[Words[0]] + [wordScore(Words[0], scrabbleScores)]] + inDictionary(Words[1:])
    else:
        return inDictionary(Words[1:])
    

  
def possibleWords(Rack, Dictionary):
    '''Returns a list of all possible words in list Dictionary
    that can be made from a given list of lowercase characters.
    input L: a list of lowercase characters'''
    if Rack == []:
        print('Your rack is empty! Draw some tiles.')
        return []
    elif listCompose(Rack, Dictionary[0]) != '':
        return [listCompose(Rack, Dictionary[0])] + possibleWords(Rack, Dictionary[1:])
    elif Dictionary[1:] != []:
        return possibleWords(Rack, Dictionary[1:])
    else:
        return []


def highestScore(scoreList):
    '''Returns the highest scoring word and its point value given
    a list of words and their scores'''
    if len(scoreList) == 0:
        return ['', 0]
    elif len(scoreList) == 1:
        return scoreList[0]
    else:
        if(scoreList[1])[1] > (scoreList[0])[1]:
            (scoreList[0]) = (scoreList[1])
            return highestScore(scoreList[1:])
        else:
            (scoreList[1]) = (scoreList[0])
            return highestScore(scoreList[1:])
    

# Preliminary Functions
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


# Endgoal Functions
def scoreList(Rack):
    '''Returns a list of all possible words in list Dictionary that can be made
    from a given list of lowercase characters, and their Scrabble scores.
    input Rack: a list of lowercase characters'''
    words = possibleWords(Rack, Dictionary)
    if len(Rack) == 0 or '' in Rack:
        print('Your rack is invalid! Draw some tiles.')
        return []
    else:
        return inDictionary(possibleWords(Rack, Dictionary))
    

def bestWord(Rack):
    '''Returns a list of two elements: the highest scoring word possible
    made from the characters in list Rack, and that word's score
    input Rack: a list of lowercase letters'''
    if len(Rack) == 0 or '' in Rack:
        print('Your rack is invalid! Draw some tiles.')
        return []
    else:
        return highestScore(scoreList(Rack))
            
    
    

