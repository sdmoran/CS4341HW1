def isreverse(s1, s2):
    # Your code here
    # base cases:
    if len(s1) == 0 and len(s2) == 0:
        return True

    # reduction step: take character off front of s1 and off back of s2, call function recursively
    elif s1[0:1] == s2[len(s2) - 1 : len(s2)]:
        return isreverse(s1[1:len(s1)], s2[0:len(s2) - 1])

    # If current character or string lengths mismatch, they cannot be reverses of each other
    else:
        return False
