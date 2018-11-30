'''
Author: Andrew Chinique @achiniqu
Instructor: Professor Naumann
Course: CS 115 Introduction to Computer Science
Due Date: 2018-11-15

I pledge my honor that I have abided by the Stevens Honor System.
                                            -- Andrew Chinique

Lab 11 - Quadratic Equation Class
'''
class QuadraticEquation:
    def __init__(self,a,b,c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c

    def discriminant(self):
        '''returns the discriminat of the quadratic equation'''
        return (self.__b * self.__b) - (4 * self.__a * self.__c)

    def root1(self):
        '''returns the first root of the quadratic equation'''
        if self.discriminant() < 0:
            return None
        return ((-1 * self.__b) + (self.discriminant() ** 0.5)) / (2 * self.__a)

    def root2(self):
        '''returns the second root of the quadratic equation'''
        if self.discriminant() < 0:
            return None
        return ((-1 * self.__b) - (self.discriminant() ** 0.5)) / (2 * self.__a)

    def __str__(self):
        '''displays the input coefficients as a quadratic equation'''
        if self.__a == 0:
            print("Coefficient 'a' cannot be 0 in a quadratic equation!")
            raise ValueError
        displayA = str(self.__a) + 'x^2'
        displayB = ' + ' + str(self.__b) + 'x'
        displayC = ' + ' + str(self.__c)
        if self.__a == -1:
            displayA = '-x^2'
        elif self.__a == 1:
            displayA = 'x^2'
        elif self.__a < 0:
            displayA = '-' + displayA
        if self.__b == 1:
            displayB = ' + x'
        elif self.__b == 0:
            displayB = ''
        elif self.__b == -1:
            displayB = ' - x'
        elif self.__b < 0:
            displayB = ' - ' + str(-1 * self.__b) + 'x'
        if self.__c == 0.0:
            displayC = ''
        elif self.__c < 0:
            displayC = ' - ' + str(-1 * self.__c)
        return displayA + displayB + displayC + ' = 0'
