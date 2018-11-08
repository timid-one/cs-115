# mandelbrot.py
# Lab 9
#
# Name:

# keep this import line...
from cs5png import PNGImage
from cs115 import *

# start your Lab 9 functions here:
def mult(c,n):
    '''Returns the product of c and n, without utilizing the multiplication
    operator.
    input c: a number
    input n: a whole number'''
    result = 0
    for i in range(n):
        result = result + c
    return result

def update(c, n):
    '''update starts with z= 0 and runs z = z**2 + c for a total of n times.
    It returns the final z.
    input c: a number
    inputer n: a whole number'''
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    '''inMSet takes in: c for the update step of z = z**2+c; and n, the maximum
    number of times to run that step. Then, it should return: False as soon as
    abs(z) gets larger than 2; or True if abs(z) never gets larger than 2 (for n
    iterations).'''
    z = 0 + 0*1j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col,row):
    '''function that returns True if we want the pixel at col, row and False
    otherwise'''
    if col%10 == 0 or row%10 == 0:
        return True
    return False

def test():
    '''function that demonstrates how to create and save a .png image'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width): # creates a loop that draws pizels
        for row in range(height):
            if weWantThisPixel(col,row) == True:
                image.plotPoint(col,row)
    image.saveFile()

# if you were to change the if statement in the weWantThisPixel function to
# contain an or instead of an and, then the resulting image would plot all the
# points in between the listed points, since all those points have either a zero
# value when the modulus is performed on their col value OR their row value. In
# short, it would create a grid image.

def scale(pix, pixMax, floatMin, floatMax):
    '''scale takes in: pix, the CURRENT pixel column or row; pixMax, the total
    number of pixel columns; floatMin, the minimum floating-point value; and
    floatMax, the max floating-point value. Scale returns the floating-point
    value that corresponds to pix.'''
    pixRatio = 1.0*pix / pixMax
    return ((floatMax-floatMin)*pixRatio) + floatMin

def mset():
    '''creates a 300x200 image of the Mandelbrot'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width): # creates a loop that draws pizels
        for row in range(height):
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            n = 25
            if inMSet(c,n) == True:
                image.plotPoint(col,row)
    image.saveFile()
    
    
