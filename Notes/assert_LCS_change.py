# assert_LCS_change - DN Sept 21, 2018
from cs115 import *

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  # do the first symbols match?
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def testLCS():
    assert LCS("spam","sam!") == 3
    assert LCS("spam","xsam") == 3
    
def knapsack(capacity, items):
    """Max value possible within capacity, assuming capacity >= 0,
    given list of items [weight,value]"""
    if items == []: return 0
    elif items[0][0] > capacity: # check weight of first item
        return knapsack(capacity, items[1:])
    else: return None
        
def testKnap():
    assert knapsack(7, []) == 0
    assert knapsack(7, [ [2, 100], [3, 112], [4, 125] ]) == 237

infty = float('inf')

def change(amt, coins):
    """Assuming amt>=0 and coins is a list of positive numbers
that represent coin values, return the smallest number of coins
that sum to amt.  Return infty if not possible.
Note: if coins includes the value 1, it is always possible."""
    if amt == 0: return 0
    elif coins == []: return infty
    elif coins[0] > amt: return change(amt, coins[1:])
    else:
        use = 1 + change(amt-coins[0], coins)
        lose = change(amt, coins[1:])
        return min(use,lose)

def testChange():
    assert change(48, [1, 5, 10, 25, 50]) == 6
    assert change(48, [1, 7, 24, 42]) == 2

def coinNames(coinInfo):
    """assume coinInfo is a non-empty list of pairs [value,name].
    Return the names, as a string.  For example,
    coinNames([[1,'penny'],[5,'nickel'],[10,'dime']]) should return
    'penny nickel dime'.  """
    return reduce(lambda st1, st2: st1 + ' ' + st2,
                  map(lambda pair: pair[1], coinInfo))

def exp(n,k):
    """n**k, assuming k>=0 and n is a number"""
    if k == 0: return 1
    else: return n * exp(n,k-1)

def expfast(n,k):
    if k == 0: return 1
    elif k%2==0:
        t = expfast(n, k//2)
        return t*t
    else: return n * expfast(n,k-1)

def testExp():
    assert exp(3,5) == 3**5
    assert exp(2,0) == 2**0
    assert expfast(3,5) == 3**5
    assert expfast(2,0) == 2**0

def exptail(n, k):
    """n**k, computed using tail recursion. Trace this!"""
    def ext(accumulator, n, k):
        if k == 0: return accumulator
        else: return ext(n * accumulator, n, k-1)
    return ext(1, n, k)

def reverse(L):
    if L == []:
        return []
    else: return reverse(L[1:]) + [L[0]]

# # exercise: tail recursive version
# def reverse2(L):
#     def rev(acc, L):
#         .....define this using recursion on L,
#         so we can use L==[], L[0], and rev(...,L[1:])

#     return rev( ......, L)

#     My thinking: I want to define rev so that a trace will
#     look like this:
#         reverse2([a,b,c,d])
#           rev([], [a,b,c,d])
#             rev([a], [b,c,d])
#               rev([b,a],[c,d])
#                 rev([c,b,a],[d])
#                   rev([d,c,b,a],[])
                  

# def testReverse():
#     assert reverse(['hi','there']) == reverse2(['hi','there'])
#     assert reverse(range(10)) == reverse2(range(10))
#     assert reverse([]) == reverse2([])

















    

    
    
    
