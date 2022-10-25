def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a > 0 and (a % 2 == 1 or a % 2 == 0)
number = main(0)
print(bool(number))
