#
# life.py - Game of Life lab
#
# Name: Andrew Chinique @achiniqu
# Pledge: 
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function.
       input width: a whole number"""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols
    input width: a whole number
    input height: a whole number"""
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def printBoard(A):
    """this function prints the 2d list-of-lists A without spaces
    (using sys.stdout.write)
    input A: a list of lists"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width,height):
    """ creates an empty board and then modifies it so that it has a diagonal
    strip of "on" cells.
    input width: a whole number
    input height: a whole number"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width,height):
    """ creates an empty board and then modifies it so that it has a diagonal
    strip of "on" cells.
    input width: a whole number
    input height: a whole number"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(width,height):
    """ creates an empty board and then modifies it so that it has a diagonal
    strip of "on" cells.
    input width: a whole number
    input height: a whole number"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    '''creates a deep copy of A
    input A: a 2d array defined as a list of lists'''
    numRows = len(A)
    numCols = len(A[0])
    B = createBoard(numRows, numCols)
    for row in range(numRows):
        for col in range(numCols):
            B[row][col] = A[row][col]
    return B

def innerReverse(A):
    '''changes all ones in a 2D array into zeros and all zeros into ones; sets
    all numbers on the borders to be zeros.
    input A: a 2d array defined as a list of lists'''
    B = copy(A)
    heightB = len(B)
    widthB = len(B[0])
    for row in range(heightB):
        for col in range(widthB):
            if row == 0 or row == heightB-1 or col == 0 or col == widthB-1:
                pass
            else:
                B[row][col] = 1-(B[row][col])
    return B

def countNeighbors(row, col, A):
    count = 0
    for r in range(row-1, row + 2):
        for c in range(col-1, col + 2):
            if r == row and c == col:
                pass
            elif A[r][c] == 1:
                count +=1
    return count

def next_life_generation(A):
    '''makes a copy of A and then advances one generation of Conway's game of
    life within the inner cells (i.e. not the cells on the outside edges of the
    array) of the copy.
    input A: a 2d array defined as a list of lists
    RULES:
    Outer edges always stay at zero.
    A cell with fewer than two live neighbors dies (goes to zero)
    A cell with more than 3 live neighbors dies (goes to zero)
    A dead cell with exactly 3 live neighbors comes to life (goes to one)
    All other cells maintain their state'''
    B = copy(A)
    heightB = len(B)
    widthB = len(B[0])
    for row in range(heightB):
        for col in range(widthB):
            if row == 0 or row == heightB-1 or col == 0 or col == widthB-1:
                B[row][col] = 0
            elif countNeighbors(row,col,A) < 2 or countNeighbors(row,col,A) > 3:
                B[row][col] = 0
            elif countNeighbors(row,col,A) == 3:
                B[row][col] = 1
    return B
