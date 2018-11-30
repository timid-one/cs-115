def nCommon(L,M):
    '''return the length of the intersection of two lists.
    input L: a sorted list containing no duplicates
    input M: a sorted list containing no duplicates'''
    com = 0
    j = 0
    i = 0
    while i < len(L) and j < len(M):
        for i in L:
            print(i)
            if i == M[j]:
                com +=1
                j += 1
            else:
                j += 1
    return com
    
