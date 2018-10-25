'''
Created on 2018-10-10
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def numToBinary(n):
    '''Returns the string with the binary representation of non-negative
    integer n. If n is 0, the empty string is returned.
    input n:: a whole number'''
    if n == 0:
        return ''
    else:
        return numToBinary(n//2) + str(n % 2)

def binaryToNum(s):
    '''Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    input s: a string consisting of zeros and ones.'''
    if s == '':
        return 0
    else:
        return binaryToNum(s[:-1])* 2 + int(s[-1:])

def numToBinaryPadded(n):
    '''Pads the binary number to be the length of the compressed block size.
    input n: a whole number'''
    s = numToBinary(n)
    return "0" * (COMPRESSED_BLOCK_SIZE - len(s)) + s


def prefixLen(s):
    if len(s) == 1:
        return 1
    elif s[1] == s[0]:
        return 1 + prefixLen(s[1:])
    else:
        return 1
    
def compress(S):
    '''Returns a run-length encoded version of string S.
    input S: a string consisting of ones and zeros of length 64.'''
    def compressHelp(S, b):
        if S == '':
            return ''
        elif S[0] != chr(b + ord('0')):
            return numToBinaryPadded(0) + compressHelp(S, 1-b)
        else:
            prefixLength = min(prefixLen(S), MAX_RUN_LENGTH)
            return numToBinaryPadded(prefixLength) + compressHelp(S[prefixLength:], 1-b)
    return compressHelp(S, 0)

def uncompress(C):
    '''Returns a 64-bit string binary string that is equivalent to the
    run-length encoded C.
    input C: a run-length encoded string'''
    def uncompressHelp(C, b):
        if C == '':
            return ''
        else:
            number = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])
            return (chr(b + ord('0')) * number + \
            uncompressHelp(C[COMPRESSED_BLOCK_SIZE:], 1-b))
    return uncompressHelp(C, 0)

# The largest number of bits that could be used to encode a 64-bit string would
# be 325 bits; if each bit is different from the last, it will take 64 5-bit
# blocks to compose the string, and if the string begins with 1, it will need an
# additional 5-bit string of 5 zeros to represent that there are zero zeros at
# the beginning of the string.

def compression(S):
    '''Returns the ratio between the length of compressed string S and the
    original string.
    Input S: a 64-bit string consisting of ones and zeros.'''
    return len(compress(S)) / len(S)

def testImages():
    penguin =  "00011000"+"00111100"*3 + \
    "01111110"+"11111111"+"00111100"+"00100100"
    smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + \
    "01000010" + "01111110"+ "0"*8
    five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + \
    "00000001"*2 + "1"*7 + "0"
    print(compress(penguin))
    print(compress(smile))
    print(compress(five))
    print(compression(penguin))
    print(compression(smile))
    print(compression(five))

# The images tested were penguin, smile, and five.
# compression(penguin) gave the result 1.484375
# compression(smile) gave the result 1.328125
# compression(five) gave the result 1.015625
# Because the ratio given by compression for each image was greater than one,
# it can be concluded that the images had greater disparities in the continuity
# of the ones and zeros composing them, resulting in the compressed version
# actually being larger in size than the uncompressed version.

# Professor Lai is wrong, and the algorithm she claims to have developed is
# impossible. If there is an alternating pattern of ones and zeros, each bit
# would require at least five bits for a run-length representation.
