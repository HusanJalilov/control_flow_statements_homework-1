from operator import truediv


def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    s=a%10
    n=a//10
    new=s*10+n
    if new>=a:
        return "True"
    else:
        return "False"