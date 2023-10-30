def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    number = int(abs(n)**0.5)
    return all([False for i in range(2, number) if n % i == 0])


