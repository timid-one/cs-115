FullAdder = { ('0','0','0') : ('0','0'), ('0','0','1') : ('1','0'), ('0','1','0') : ('1','0'),('0','1','1') : ('0','1'), ('1','0','0') : ('1','0'), ('1','0','1') : ('0','1'), ('1','1','0') : ('0','1'), ('1','1','1') : ('1','1') }

def addB(S, T):
    """add two binary, S and T and return the result. This function uses full adder, and operate fully by binary."""
    diff = len(S) - len(T)
    if diff > 0:
        T = "0" * diff + T
    if diff < 0:
        S = "0" * diff + S

    def addBHelper(C, S, T):
        if S == "":
            return "" if C == "0" else "1"
        return addBHelper(FullAdder[(C, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(C, S[-1], T[-1])][0]
    return addBHelper("0", S, T)
