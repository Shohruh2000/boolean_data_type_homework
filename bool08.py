def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return type(a) == type(1) and a >= 0
nuber = main(0)
print(bool(nuber))
