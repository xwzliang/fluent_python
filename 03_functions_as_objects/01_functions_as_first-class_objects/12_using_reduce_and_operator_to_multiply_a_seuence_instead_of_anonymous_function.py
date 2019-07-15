from functools import reduce

def fact_anonymous(n):
    """
    Factorial implemented with reduce and an anonymous function
    >>> fact_anonymous(5)
    120
    """
    return reduce(lambda a, b: a*b, range(1, n+1))


# To save you the trouble of writing trivial anonymous functions like lambda a, b: a*b, the operator module provides function equivalents for dozens of arithmetic operators.

from operator import mul
from functools import reduce

def fact_operator(n):
    """
    Factorial implemented with reduce and operator.mul
    >>> fact_operator(5)
    120
    """
    return reduce(mul, range(1, n+1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
