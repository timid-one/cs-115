# loop invariant examples: intersect, fib

from cs115 import *

def intersect(L,M):
    '''The common elements of lists L,M,
       (ordered as they appear in L).'''
    return filter(lambda x: x in M, L)

def intersectSorted(L,M):
    '''assuming L and M are sorted, intersect(L,M)'''
    res = []
    i = 0 # index for L
    j = 0 # index for M
    while i < len(L) and j < len(M):
        assert res == intersect(L[:i],M[:j])
        if L[i]==M[j]:
            res = res + [L[i]]
            i+=1
            j+=1
        elif L[i] < M[j]:
            i +=1
        else:
            j += 1
    assert res == intersect(L,M)
    return res

def testIntersectSorted():
    A = ["Kendrick L", "Alanis Morrisset", "Khaled", "Los Fabulosos C"]
    B = ["Macklemore", "Alanis Morrisset", "Lila Downs", "Kendrick L", "Alicia Keys"]
    C = list(A)
    D = list(B)
    C.sort()
    D.sort()
    print(intersectSorted(C,D))

# iFib is an imperative implementation of fib,
# with assertions to check the loop invariant.
# This shows that a "loop invariant" is a condition that is
# supposed to be true each time control reaches the "top" of the loop.

def fib(n):
    '''Assume n is a non-negative integer.
    Return the nth Fibonacci number.'''
    if n==0 or n==1: return n
    else: return fib(n-1) + fib(n-2)

def iFib(n):
    '''Imperative implementation of fib.'''
    if n==0 or n==1: return n
    else:
        prev = 0
        cur = 1
        i = 1
        assert cur==fib(i) and prev==fib(i-1) # loop invariant
        assert 1 <= i <= n                    # loop invariant
        while i!=n:
            cur = cur + prev
            prev = cur - prev
            i += 1
            assert cur==fib(i) and prev==fib(i-1)
            assert 1 <= i <= n 

        # The invariant holds following the loop, at which point
        # we also have i==n, which implies cur==fib(n)

    return cur

# Once we're confident our code is correct, we comment-out the assertions.
# Try commenting-out the ones in iFib, and then compare the running
# time of fib(40) and iFib(40).




def iFib_alt(n):
    '''Like iFib but using a for-loop'''
    if n==0 or n==1: return n
    else:
        prev = 0
        cur = 1
        for i in range(1,n):
            assert cur==fib(i) and prev==fib(i-1)
            cur = cur + prev
            prev = cur - prev
        assert cur==fib(n) # why will this be true?
        return cur
