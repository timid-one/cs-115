'''
Created on 2018-10-01
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - hw4
'''
from cs115 import *

pascal_zero = [1]

def pascal_help(num_row):
    '''Returns a llist of sum of the adjacent elements of a given row of
    Pascal's triangle.
    input num_row: a whole number'''
    if len(num_row) < 2:
        return []
    else:
        return [num_row[0] + num_row[1]] + pascal_help(num_row[1:])

def pascal_row(num_row):
    '''Returns a list of integers in the given row of Pascals's triangle, where
    row 0 is the first row, [1].
    input num_row: a whole number'''
    if num_row == 0:
        return pascal_zero
    else:
        return pascal_zero + pascal_help(pascal_row(num_row-1)) + pascal_zero

def pascal_triangle(num_row):
    '''Returns a list of lists representing the rows of Pascal's triange, where
    row 0 is the first row, [1], and numRow represents the row to stop at.
    input num_row: a whole number'''
    if num_row == 0:
        return [pascal_zero]
    else:
        return pascal_triangle(num_row-1) + [pascal_row(num_row)]

def test_pascal_row():
    assert pascal_row(0)== [1]
    assert pascal_row(1)== [1, 1]
    assert pascal_row(2)== [1, 2, 1]
    assert pascal_row(5)== [1, 5, 10, 10, 5, 1]
    print('pascal_row works!')

def test_pascal_triangle():
    assert pascal_triangle(0)== [[1]]
    assert pascal_triangle(1)== [[1], [1, 1]]
    assert pascal_triangle(2)== [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5)== [[1], [1, 1], [1, 2, 1],
    [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    print('pascal_triangle works!')

test_pascal_row()
test_pascal_triangle()
