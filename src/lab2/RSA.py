import random
from typing import Tuple

def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    number = int(abs(n)**0.5+1)
    return all([False for i in range(2, number) if n % i == 0])

def gcd(a: int, b: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """

    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    -17
    """
    a, b = e, phi
    x, y = [0], [1]
    AdelB = list()

    while a % b != 0:
        AdelB.append(a // b)
        a, b = b, a % b

    if len(AdelB) == 0:
        return 0

    for i in range(1, len(AdelB)+1):
        x.append(y[i - 1])
        y.append(x[i - 1] - y[i - 1] * AdelB[len(AdelB) - i])
    return x[-1]



def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p-1) * (q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

print(generate_keypair(7,5 ))
