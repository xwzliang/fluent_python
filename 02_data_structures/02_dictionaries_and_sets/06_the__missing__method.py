"""StrKeyDict0 converts nonstring keys to str on lookup"""

class StrKeyDict0(dict):	# inherits from dict
    """
    Test for item retrieval using 'd[key]' notation::
    >>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    >>> d['2']
    'two'
    >>> d[4]
    'four'
    >>> d[1]
    Traceback (most recent call last):
        ...
    KeyError: '1'

    Test for item retrieval using 'd.get(key)' notation::
    >>> d.get('2')
    'two'
    >>> d.get(4)
    'four'
    >>> d.get(1, 'N/A')
    'N/A'

    Test for the 'in' operator::
    >>> 2 in d
    True
    >>> 1 in d
    False

    A better way to create a user-defined mapping type is to subclass collections.UserDict instead of dict. Here we subclass dict just to show that __missing__ is supported by the built-in dict.__getitem__ method.
    """

    def __missing__(self, key):
        if isinstance(key, str):	# Check whether key is already a str. If it is, and it's missing, raise KeyError
            raise KeyError(key)
        return self[str(key)]	# Build str from key and look it up

    def get(self, key, default=None):
        try:
            return self[key]	# The get method delegates to __getitem__ by using the self[key] notation; that gives the opportunity for our __missing__ to act
        except KeyError:
            return default	# If a KeyError was raised, __missing__ already failed, so we return the default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
