'''
Created on 2018-10-08
@author:   Andrew Chinique @achiniqu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle

def sv_tree(trunk_length, levels):
    '''Draws a tree with a given trunk length
    that branches off using recursion.
    input trunk_length: an integer
    input levels: an integer'''
    if (levels <= 0):
        return
    else:
        turtle.pencolor("brown")
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree((trunk_length/2), (levels - 1))
        turtle.right(90)
        turtle.pencolor("green")
        sv_tree((trunk_length/2), (levels - 1))
        turtle.left(45)
        turtle.backward(trunk_length)
        turtle.pencolor("brown")
        return


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]
    input n: a whole number'''
    memo = {}
    def fast_lucas_helper(n):
        if n == 0:
            return 2
        elif n == 1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            number = fast_lucas_helper(n-1) + fast_lucas_helper (n-2)
            memo[n] = number
            return number
    return fast_lucas_helper(n)

        
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.
    input amount: a non-negative integer
    input coins: a list of coin values, where coins[0] == 1'''
    memo = {}
    def fast_change_helper(amount, coins):
        if amount == 0:
            return 0
        elif amount < 0 or coins == ():
            return float("inf")
        elif (amount, coins) in memo:
            return memo[(amount, coins)]
        else:
            useIt = 1 + fast_change_helper(amount-coins[0], coins)
            loseIt = fast_change_helper(amount, coins[1:])
            answer = min(useIt, loseIt)
            memo[(amount, coins)] = answer
            return answer
    return fast_change_helper(amount, tuple(coins))

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
