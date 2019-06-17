import collections

class StrKeyDict(collections.UserDict):	
    """
    StrKeyDict always converts non-string keys to str - on inserting, update and lookup
    >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
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

  """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):	# this is simpler: we can assume all stored keys are str and we can check on self.data instead of invoking self.keys() as we did in StrKeyDict0
        return str(key) in self.data

    def __setitem__(self, key, item):	# __setitem__ converts any key to a str. This method is easier to overwrite when we can delegate to the self.data attribute
        self.data[str(key)] = item

if __name__ == "__main__":
    import doctest
    doctest.testmod()
