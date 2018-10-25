'''
Created on 2018-10-10
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.
    input n: an integer'''
    if n % 2 == 0:
        return False
    return True

    # 42 in base 2 is 1010100

def numToBinary(n):
    ''' Returns the string with the binary representation of non-negative
    integer n. If n is 0, the empty string is returned.
    input n:: a whole number'''
    if n == 0:
        return ''
    else:
        return numToBinary(n//2) + str(n % 2)
    
    # The rightmost bit of an odd base ten number will always be a 1,
    # because it is the only bit that represents an odd base ten number;
    # when it is present in the ones place, it represents the presence of the
    # base ten number 1. The rest of the bits represent even base ten numbers
    # (2, 4, 8, 16, 32, etc.). Thus, when it is present, an odd number is added
    # to the sumrepresented by the preceding bits of the binary number, making
    # the entire number odd. The converse is true for an even base ten number;
    # the rightmost bit will always be a 0 when converted to binary because it
    # represents the absence of the base ten number 1 in the sum of the base ten
    # numbers represented by the bits of the binary number.

    # The value of the original number is being integer divided by two: that is,
    # the original number is divided by two, and rounded down to the nearest
    # integer.

    # When N is even, the base two representation of N will end with zero.
    # Wehn N is odd, the base two representation of N will end with a one.

def binaryToNum(s):
    '''Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    input s: a string consisting of zeros and ones.'''
    if s == '':
        return 0
    else:
        return binaryToNum(s[:-1])* 2 + int(s[-1:])

def increment(s):
    '''Returns the binary representation of binaryToNum(s) + 1.
    input s: an 8-bit string consisting of ones and zeros.'''
    if s == '11111111':
        return '00000000'
    elif len(s) == 8:
        incremented = numToBinary(binaryToNum(s) + 1)
        return '0'*(8-len(incremented)) + incremented
    else:
        return increment(('0'*(8-len(s))) + s)

def count(s, n):
    '''Prints s and its n successors.
    input s: an 8-bit string consisting of ones and zeros.
    input n: a whole number.'''
    if n == 0:
        print(s)
    else:
        print(s)
        return count(increment(s), n - 1)

def numToTernary(n):
    '''Returns the string with the ternary representation of non-negative
    integer n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return numToTernary(n//3) + str(n % 3)

    # The ternary representation of base ten number 59 is 2012. It is equivalent
    # to 2*1 + 1*3 + 0*9 + 2*27.
    
def ternaryToNum(s):
    '''Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.
    input s: a string consisting of zeros, ones, and twos.'''
    if s == '':
        return 0
    else:
        return ternaryToNum(s[:-1])* 3 + int(s[-1:])
