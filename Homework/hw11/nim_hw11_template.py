# nim template DNaumann (2018), for assignment nim_hw11.txt

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)

from cs115 import *

def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print("N-Nani?! Bested? by a human??")
            print("Surely you won through sheer luck. Challenge me again!")
            print("I shall prove thou art inferior to I, NimMaster5000!")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print("As expected. No mortal can surpass the great NimMaster5000!")
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    print("We're going to play Nim. You'd better play optimally or I'll win.")
    num_piles = int(input("How many piles shall we play with? (Max 3) "))
    while num_piles < 1 or num_piles > 3:
        num_piles=int(input("Invalid input! " +
                            "Try again, and get it right this time. "))
    piles = [0] * num_piles
    for var in (range(num_piles)):
        piles[var] = int(input("How many coins will be in pile " + str(var) +
                               "? (Max 3) "))
        while piles[var] < 1 or piles[var] > 3:
            piles[var] = int(input("Invalid imput! " +
                                   "Try again, and get it right this time. "))
    

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    for var in (range(num_piles)):
        print("Pile " + str(var) + " has " + str(piles[var]) + " coins.")

        

def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt



def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    chosen = int(input("Which pile? "))
    while chosen not in range(num_piles):
        chosen = int(input("Invalid selection! Try again. "))
    while piles[chosen] == 0:
        print("That pile is empty! Try again." )
    return chosen
    


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    amount = int(input("How many coins will you take? "))
    while amount not in (map(lambda x: x +1, range(piles[pnum]))):
        amount = int(input("Invalid amount! Try again. "))
    return amount



def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    return reduce(lambda a, b: a ^ b, piles)



def isNotZero(num):
    if num == 0:
        return False
    return True



def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    pile_sums = []
    for var in range(num_piles):
        pile_sums = pile_sums + [(piles[var]) ^ game_nim_sum()]
    for var in range(num_piles):
        if pile_sums[var] < piles[var]:
            return (piles.index(piles[var]), piles[var] - pile_sums[var])
    return (piles.index(next(x for x in piles if isNotZero(x))), 1)

    

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    print("It is my turn. Your demise approaches.")
    choice = opt_play()
    piles[choice[0]] = piles[choice[0]] - choice[1]
    print("I have removed " + str(choice[1]) + " coin from Pile " +
          str(choice[0]) + ".")
    


#   start playing automatically
if __name__ == "__main__" : play_nim()
