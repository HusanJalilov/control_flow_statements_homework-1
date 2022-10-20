def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    s=0
    if a<0:
        s+=1
    elif b<0:
        s+=1
    elif c<0:
        s+=1
    return s
print(main(3,-3,6))