'''
Author: Andrew Chinique @achiniqu
Instructor: Professor Naumann
Course: Introduction to Computer Science
Due Date: 6 December 2018

I pledge my honor that I have abided by the Stevens Honor System.
                                                -- Andrew Chinique
Homework 13 - Connect 4
'''
from cs115 import *

class Board:
    def __init__(self, width=7, height=6):
        '''The constructor. It creates a board for Connect 4. If unspecified, it
        will use 7 columns and 6 rows by default. Assumes the user will enter
        a positive, non-zero integer.
        input width: a natural number
        input height: a natural number'''
        self.width = width
        self.height = height
        self.data = [[' ' for col in range(width)] for row in range(height)]


    def __str__(self):
        '''Replaces the string method for this object. Returns a string
        representative of the calling object.'''
        board = ''
        for row in self.data:
            for col in row:
                board += '|' + col # creates a divider between each play column
            board += '|\n'
        board += '-' * (self.width * 2 + 1) + '\n'
        for i in range(self.width):
            board += " " + str(i)
        return board

    def allowsMove(self, col):
        '''returns a boolean whether or not the input column can receive a game
        piece.
        input column: an integer'''
        if col > self.width and col < -1:
            return False
        space = 0
        for row in range(self.height):
            space += 1 if self.data[row][col] == ' ' else 0
        return space > 0

    def addMove(self, col, ox):
        '''adds a piece into the specified column, if possible.
        input col: an integer.
        input ox: a string representing the piece, preferably X or O.'''
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != ' ':
                    self.data[row - 1][col] = ox
                    return
            self.data[self.height - 1][col] = ox

            
    def setBoard(self, moveString):
         """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'. DOES NOT REPLACE
         CHECKERS ALREADY PRESENT.

         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         moveString must be a string of integers
         """
         nextCh = 'X' # start by playing 'X'
         for colString in moveString:
             col = int(colString)
             self.addMove(col, nextCh)
             if nextCh == 'X':
                 nextCh = 'O'
             else:
                 nextCh = 'X'
         print(self)

    def delMove(self,col):
        '''This method removes the top checker from the column col. If the column
        is empty, then delMove does nothing.'''
        if -1 < col < self.width:
            for row in range(self.height):
                if self.data[row][col] != ' ':
                    self.data[row][col] = ' '
                    return
            
    def winsFor(self, ox):
        '''This method should return True if the given checker, 'X' or 'O', held
        in ox, has won the calling Board. It should return False otherwise.'''
        def horizWin(ox):
            '''returns true if the placed checker yields a horizontal win.'''
            for row in range(self.height):
                for col in range(self.width - 3):
                    if self.data[row][col] == ox and \
                            self.data[row][col + 1] == ox and \
                            self.data[row][col + 2] == ox and \
                            self.data[row][col + 3] == ox:
                        return True
                                
        def vertWin(ox):
            '''returns true if the placed checker yields a vertical win.'''
            for row in range(self.height - 3):
                for col in range(self.width):
                    if self.data[row][col] == ox and \
                            self.data[row + 1][col] == ox and \
                            self.data[row + 2][col] == ox and \
                            self.data[row + 3][col] == ox:
                        return True

        def ascendDiagonal(ox):
            '''returns true if the placed checker yields an ascending diagonal
            win (from the lower left towards the upper right).'''
            for row in range(self.height):
                for col in range(self.width - 3):
                    if self.data[row][col] == ox and \
                            self.data[row - 1][col + 1] == ox and \
                            self.data[row - 2][col + 2] == ox and \
                            self.data[row - 3][col + 3] == ox:
                        return True
                                
        def descendDiagonal(ox):
            '''returns true if the placed checker yields a descending diagonal
            win (from the upper left towards the bottom right).'''
            for col in range(self.width - 3):
                for row in range(self.height - 3):
                    if self.data[row][col] == ox and \
                            self.data[row + 1][col + 1] == ox and \
                            self.data[row + 2][col + 2] == ox and \
                            self.data[row + 3][col + 3] == ox:
                        return True

        if horizWin(ox) == True or vertWin(ox) == True or ascendDiagonal(ox) == True or descendDiagonal(ox) == True:
            return True
        else:
            return False
                                
    def hostGame(self):
        '''This is a method that, when called from a connect four board object, will
        run a loop allowing the user(s) to play a game.'''
        print('Wanna play Connect Four? Sure you do!')
        currentPlayer = 'X'
        while True:
            boolList = []
            for col in range(self.width):
                boolList = boolList + [self.allowsMove(col)]
            if sum(boolList) == 0:
                print('The game is a draw!')
                break
            print(self)
            turn = int(input('Player ' + currentPlayer + ' turn: '))
            while self.allowsMove(turn) == False:
                turn = int(input('Invalid choice! Try again. '))
            self.addMove(turn, currentPlayer)
            if self.winsFor(currentPlayer):
                print(self)
                print('Congrations! You\'re winner, player ' + currentPlayer + '!')
                break
            if  currentPlayer == 'X':
                currentPlayer = 'O'
            else:
                currentPlayer = 'X'

# for test purposes
yeet = Board() # initializes a Board object for testing
yeet.hostGame() # begins the game
