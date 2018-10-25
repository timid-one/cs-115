# two-part exercise

from cs115 import map

'''
Part 0
Here is a memoized version of edit distance.
Your task: make it trace the calls to fastED_help, indented
according to recursion depth.  Hint: add a parameter to fastED_help.
'''
def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    depth = 0
    memo = {}
    def fED (first, second, depth):
        if first == '' or second == '':
            depth += 1
            print(depth * '    ' + str((first, second)))
            if second == '':
                return len(first)
            return len(second)
        elif (first, second) in memo:
            depth += 1
            print(depth * '    ' + str((first, second)))
            return memo[(first, second)]
        elif first[0] == second[0]:
            depth += 1
            answer = fED(first[1:], second[1:], depth)
            memo[(first, second)] = answer
            print(depth * '    ' + str((first, second)))
            return answer
        else:
            depth += 1
            substitution = 1 + fED(first[1:], second[1:], depth)
            deletion = 1 + fED(first[1:], second, depth)
            insertion = 1 + fED(first, second[1:], depth)
            answer = min(substitution, deletion, insertion)
            memo[(first, second)] = answer
            print(depth * '    ' + str((first, second)))
            return answer
    return fED(first, second, depth)


'''
Part 1
Complete the following function.  You may use the functions
numToBinary and increment from lab 6, provided below.
Start by sketching your design in psuedo-code.
'''

def numToTC(N):
    '''Assume N is an integer.
    If N can be represented in 8 bits using two's complement, return
    that representation as a string of exactly 8 bits.  
    Otherwise return the string 'Error'.
    '''
    if N > 127 or N < -128:
        return 'Error'
    elif N >= 0:
        return (8 - len(numToBinary(N))) * str(0) + numToBinary(N)
    else:
        N = N * -1
        
        

'''
Examples:
   NumToTc(1) ---> '00000001'
   NumToTc(-128) ---> '10000000'
   NumToTc(200) ---> 'Error'
'''


def numToBinary(N):
    '''Assuming N is a non-negative integer, return its base 2
    representation as a string of bits.'''
    if N == 0:
        return ''
    if isOdd(N):
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

def increment(s):
    '''Assuming s is a string of 8 bits, return the binary representation 
    of the next larger number takes an 8 bit string of 1's and 0's and 
    returns the next largest number in base 2'''
    num = binaryToNum(s) + 1
    if num == 256:
        return '00000000'
    zeros = (len(s)-len(numToBinary(num))) * '0'
    return zeros + numToBinary(num)

def binaryToNum(s):
    '''Assuming s is a string of bits, interpret it as an unsigned binary
    number and return that number (as a python integer).
    '''
    def binaryToNumHelp(s, index):
        if s == '':
            return 0
        elif s[0] == '0':
            index -= 1
            return 0 + binaryToNumHelp(s[1:], index)
        else:
            index -= 1
            return 2**index + binaryToNumHelp(s[1:], index)
    return binaryToNumHelp(s, len(s))

def isOdd(n):
    '''returns whether a number is odd or not'''
    if n % 2 == 0:
        return False
    else:
        return True

