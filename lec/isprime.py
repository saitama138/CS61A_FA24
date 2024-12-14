from math import sqrt

def isPrime(n) :
    """ isPrime is a function that takes as input an integer and
    returns True if is prime 
    and False otherwise
    >>> isPrime(9)
    False
    >>> isPrime(7)
    True
    >>> isPrime(797)
    True
    """
    
    i = 2
    while i <= int(sqrt(n)) :
        if n % i == 0 :
            return False
        i = i + 1
    return True
