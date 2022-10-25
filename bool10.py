from math import pow
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return int(pow(a,(1/2))) > 0 

number = main(121)
print(bool(number))
