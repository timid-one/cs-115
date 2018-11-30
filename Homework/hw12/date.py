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
        '''Updates the calling object to represent the date one calendar day
        after the date it originally represented.'''
        if DAYS_IN_MONTH[self.month] > self.day:
            self.day += 1
        else:
            if self.day < 29 and self.month == 2 and self.isLeapYear():
                self.day += 1
            elif self.month == 2:
                self.day = 1
                self.month = 3
            elif self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
                
    def yesterday(self):
        '''Updates the calling object to represent the date one calendar day
        before the date it originally represented.'''
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            elif self.month == 3 and self.isLeapYear() == True:
                self.day = 29
                self.month -= 1
            elif self.month == 3 and self.isLeapYear() == False:
                self.day = 28
                self.month -= 1
            else:
                self.day = DAYS_IN_MONTH[self.month -1]
                self.month -=1
        else:
            self.day -= 1

    def addNDays(self, N):
        '''Updates the calling object to represent the date N calendar days
        after the date it originally represented.
        input N: a whole number'''
        if N == 0:
            return
        else:
            for i in map(lambda x: x + 1, range(N)):
                print(self)
                self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''Updates the calling object to represent the date N calendar days
        before the date it originally represented.
        input N: a whole number'''
        if N == 0:
            return
        else:
            for i in map(lambda x: x + 1, range(N)):
                print(self)
                self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        '''Compares the calling object with another calendar date. Returns True
        if the calling object is before d2, and False otherwise.
        input d2: an object of type Date'''
        if self.year == d2.year:
            if self.month ==  d2.month:
                if self.day >= d2.day:
                    return False
            elif self.month > d2.month:
                return False
        elif self.year > d2.year:
            return False
        return True

    def isAfter(self, d2):
        '''Compares the calling object with another calendar date. Returns True
        if the calling object is after d2, and False otherwise.
        input d2: an object of type Date'''
        if self.year == d2.year:
            if self.month ==  d2.month:
                if self.day <= d2.day:
                    return False
            elif self.month < d2.month:
                return False
        elif self.year < d2.year:
            return False
        return True

    def diff(self, d2):
        '''Returns an integer representing the number of days between the
        calling object and another calendar date. If the calling object is
        before the other calendar date, the difference will be negative; if
        it is after, the difference will be positive.
        input d2: an object of type Date'''
        if self.isBefore(d2):
            selfCopy = self.copy()
            counter = 0
            while selfCopy.isBefore(d2):
                counter -= 1
                selfCopy.tomorrow()
            return counter
        elif self.isAfter(d2):
            selfCopy = self.copy()
            counter = 0
            while selfCopy.isAfter(d2):
                counter += 1
                selfCopy.yesterday()
            return counter
        else:
            return 0

    def dow(self):
        DAYS_OF_WEEK = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                        'Monday', 'Tuesday',]
        REF_DATE = Date(11, 9, 2011) # REF_DATE was a Wednesday 
        return DAYS_OF_WEEK[self.diff(REF_DATE) % 7]
