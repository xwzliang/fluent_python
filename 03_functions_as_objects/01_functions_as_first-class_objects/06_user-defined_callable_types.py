# Not only are Python functions real objects, but arbitrary Python objects may also be made to behave like functions. Implementing a __call__ instance method is all it takes.

import random

class BingoCage:
    '''
    A BingoCage does ont thing: picks items from a shuffled list, one item at a time
    >>> bingo = BingoCage(range(3))
    >>> bingo.pick()	# Test will be likely to fail because bingo shuffles the list
    1
    >>> bingo()	# Note how a bingo instance can be invoked as a function
    0
    >>> callable(bingo)
    True
    '''
    def __init__(self, items):
        # __init__ accepts any iterable; building a local copy prevents unexpected side effects on any list passed as an argument
        self._items = list(items)
        random.shuffle(self._items)	# shuffle is guaranteed to work because self._items is a list

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):	# Shortcut to bingo.pick() is bingo()
        return self.pick()

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# A class implementing __call__ is an easy way to create function-like objects that have some internal state that must be kept across invocations, like the remaining items in the BingoCage. An example is a decorator. Decorators must be functions, but it is sometimes convenient to be able to “remember” something between calls of the decorator (e.g., for memoization—caching the results of expensive computations for later use). A totally different approach to creating functions with internal state is to use closures.
