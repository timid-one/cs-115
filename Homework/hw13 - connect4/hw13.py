'''
Author: Andrew Chinique @achiniqu
Instructor: Professor Naumann
Course: Introduction to Computer Science
Due Date: 5 December 2018

I pledge my honor that I have abided by the Stevens Honor System.
                                                -- Andrew Chinique
Homework 13 - Connect 4
'''
def createOneRow(width):
    """Returns one row of zeros of width "width"...
    You should use this in your
    createBoard(width, height) function.
   input width: a whole number"""
    row = []
    for col in range(width):
        row += [' ']
    return row
def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols
    input width: a whole number
    input height: a whole number"""
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

class Board:
    def __init__(self, width=7, height=6):
        '''The constructor. It creates a board for Connect 4. If unspecified, it
        will use 7 columns and 6 rows by default. Assumes the user will enter
        a positive, non-zero integer.
        input width: a natural number
        input height: a natural number'''
        self.width = width
        self.height = height
        self.data = createBoard(width, height)

    def __str__(self):
        '''Replaces the string method for this object. Returns a string
        representative of the calling object.'''
        board = ''
        for row in self.data:
            for col in row:
                board += '|' + col # creates a divider between each play column
            board += '|\n'
        return board
                
    
