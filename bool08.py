def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return (a % 2 == 1 or a % 2 == 0) 
nuber = main(7)
print(bool(nuber))
