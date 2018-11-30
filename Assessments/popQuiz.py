# popQuiz - Nov 30, 2018 

from cs115 import *

'''
These exercises give you practice writing code with loops and practice reading code.
Read the instructions and the code carefully.  
'''

'''
Here is a variation on the Car class. 
'''
class Car(object):
    def __init__(self, make: str, model: str, mpg: float, tank_capacity: float):
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def __le__(self, other):
        '''self <= other by make and model, assuming other is also a Car'''
        assert isinstance(other, Car)
        return self.__make < other.__make or (self.__make == other.__make and self.__model <= other.__model)
    def __eq__(self, other):
        return self.__make == other.__make and self.__model == other.__model
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self,other):
        return self.__make < other.__make or self.__make == other.__make and self.__model < other.__model
    def __str__(self):
        return "Car(" + self.__make + ", " + self.__model + ")"
    
'''
Read this function, think about what it will print, and then run it to check your thinking.
'''

def demo1():
    c1 = Car('Toyota', 'Prius', 50.2, 8.8)
    c2 = Car('Honda', 'Civic', 29.5, 13)
    c3 = Car('Honda', 'Accord', 21.5, 18)
    c4 = Car('Tesla', 'Model 3', 60.0, 10.0)
    cs = [c1, c2, c3, c4]
    print(map(str,cs))

'''
Here is some code similar to lab 11.  Read the docstrings and comments, at least.
'''

def insertSort(L): 
    '''Sort L in place, using insertV1.'''
    for i in range(1,len(L)):
        insert(L,i)

def insert(L, i):
    '''Assume L[0:i] is sorted and 0 < i < len(L).
       Shift elements of the list as needed to swap L[i] into 
       position so that L[0:i+1] is sorted.'''
    x = L[i]
    j = search(L, i, x)        # find where to insert x
    for k in range(i, j, -1):  # shift elements out of the way
        swap(L, k, k-1)     
    L[j] = x                   # insert x

def search(L, i, x):
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''
    # Linear search: try successive indexes, starting with 0.
    j = 0
    while j < i and L[j] <= x:    # Invariant: L[0:j] <= x and j <= i
        j += 1
    return j

def swap(aList, i, j):
    '''swaps the values of aList[i] and aList[j]'''
    temp = aList[i]       
    aList[i] = aList[j] 
    aList[j] = temp

'''
Read this function, think about what it will do, and then run it to check your thinking.
'''
def demo2():
    c1 = Car('Toyota', 'Prius', 50.2, 8.8)
    c2 = Car('Honda', 'Civic', 29.5, 13)
    c3 = Car('Honda', 'Accord', 21.5, 18)
    c4 = Car('Tesla', 'Model 3', 60.0, 10.0)
    cs = [c1, c2, c3, c4]
    insertSort(cs)
    print("should be sorted: ", map(str,cs))
    
'''
TODO: replace None at two places in this function, so that it works as specified.
Check your work using test_find().
'''
def find(L,x):
    '''Assuming L is sorted, return i such that L[i] == x, if x is in L.
       Return -1 if x does not occur in L.'''
    i = search(L, len(L), x) 
    if i == 0 or L[i-1] != x: 
        return -1
    else:
        return i-1

def test_find():
    a = Car('Honda', 'Accord', 21.5, 18)    
    b = Car('Honda', 'Civic', 29.5, 13)
    c = Car('Tesla', 'Model 3', 60.0, 10.0)
    d = Car('Toyota', 'Prius', 50.2, 8.8)
    e = Car('Maserati', 'Alfieri', 35.0, 10.0)
    cs = [a, b, c, d] # note that it's sorted
    assert find(cs, c) == 2
    assert find(cs, e) == -1
    print("test_find succeeded")

'''
Now comes the interesting part.  You will implement the search specification
using the binary search algorithm instead of linear search.
Do not change the given code, except for filling the missing loop body.
Follow the hints.  Use test_bfind() to check your work.
'''
#########################################################################
# The idea is to use two variables, j and hi,  narrowing the search range 
# with j on the low side and hi on the high side.
# Each iteration should decrease hi - j .
##########################################################################

def binsearch(L, i, x):
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''
    
    j = 0   # now L[0:j] is []
    hi = i  # now L[hi,i] is []
    
    # invariant: L[0:j] <= x < L[hi:i] and j <= hi
    while j != hi:
        # There's at least one element in L[j:hi]. 
        # Set mid to one of the indexes j,...,hi-1
        # Then update j or hi accordingly.
        mid = (hi-j)//2 + j
        if L[mid] > x:
            hi = mid
        elif L[mid] < x:
            j = mid
        else:
            hi = mid + 1
            j = mid + 1
        
    
    # now j==hi and the invariant holds
    return j


def bfind(L,x):
    '''Like find but using binsearch.'''
    i = binsearch(L, len(L), x) 
    if i == 0 or L[i-1] != x: 
        return -1
    else:
        return i - 1

def test_bfind():
    # at start
    assert bfind([3,6,20], 3) == 0
    # at end
    assert bfind([2,6,20], 20) == 2
    # in middle, odd position
    assert bfind([2,6,20,25,30], 25) == 3
    # in middle, even position
    assert bfind([2,6,20,25,30], 20) == 2
    # in middle, odd position, even list
    assert bfind([2,6,20,25], 25) == 3
    # in middle, even position, even list
    assert bfind([2,6,20,25], 20) == 2
    print("test_bfind successful")
    


   
    
        
        
