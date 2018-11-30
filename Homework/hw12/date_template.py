'''
Created on 2018-11-25 (Happy birthday dad!)
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                                                        -- Andrew Chinique

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''Updates the callinh object to represent the date one calendar day
        after the date it originally represented.'''
        if DAYS_IN_MONTH[self.month] > self.day:
            self.day += 1
        else:
            if self.day == 28 and self.month == 2 and self.isLeapYear():
                self.day += 1
            self.day = 1
            if self.day == 31 and self.month == 12:
                self.month = 1
                self.year += 1
            self.month += 1
