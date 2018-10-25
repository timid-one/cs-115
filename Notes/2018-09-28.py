# 2018-09-28 NOTES

# turtle graphics
    # is pen
    # when tail down, is drawing

# svTree(3,100)
    #100 long
    #tree recursion


def LCS (S1, S2):
    def traceLCS(S1, S2, depth):
        print(depth * '   ' + "traceLCS(" + S1 +', ' + S2 + ")")
        depth = depth + 1
        if S1 == '' or S2 == '':
            return 0
        elif S1[0] == S2[0]:
            return 1 + LCS(S1[1:], S2[1:])
        else:
            yeet = max(LCS(S1, S2[1:]), LCS(S1[1:], S2))
            return yeet
    return traceLCS(S1, S2, 0)

    
def LCSX(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    elif S1[0] == S2[0]:
        return 1 + LCSX(S1[1:], S2[1:])
    else:
        chopS1 = LCSX(S1[1:], S2)
        chopS2 = LCSX(S1, S2[1:])
        answer = max(chop1, chop2)
        return answer


# lists are muteable
# changing a variable that was already declared is an effect
    # no output to the prompt
    # like print()

#DICTIONARY
    # represented with {}
        # curly braces
    # associate keys with values
    # should use unique identifiers for keys
    #D = {}
        #D[k] = v
    
# tuples
    # immutable lists
    # use parentheses

D = {}
D['joe'] = 23
D['sue'] = 19

# memoization
    # maintain table with keys = argument for LCS and values = LCS output for
    # given argument
    
memo = {}
def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    if S1 == '' or S2 == '':
        memo[(S1,S2)] = 0
        return 0
    elif S1[0] == S2[0]:
        answer = 1 + fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer
    else:
        chopS1 = fastLCS(S1[1:], S2)
        chopS2 = fastLCS(S1, S2[1:])
        answer = max(chop1, chop2)
        memo[(S1, S2)] = answer
        return answer

def fastLCSalt(S1, S2):
    memo = {}
    def fastLCS2(S1, S2):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == '' or S2 == '':
            memo[(S1,S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + fastLCS2(S1[1:], S2[1:])
            memo[(S1, S2)] = answer
        else:
            chopS1 = fastLCS2(S1[1:], S2)
            chopS2 = fastLCS2(S1, S2[1:])
            answer = max(chop1, chop2)
            memo[(S1, S2)] = answer
            return answer
    return fastLCS2(S1, S2)

# invariant
    # for any s,t:
        # if (s,t) in memo:
            # then memo(t,s) = LCS(s,t)




