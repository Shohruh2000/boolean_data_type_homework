from math import sqrt
def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return (a) > 0 and (sqrt(a)%2==1 or sqrt(a)%2==0)
number = main(121)
print(bool(number))




