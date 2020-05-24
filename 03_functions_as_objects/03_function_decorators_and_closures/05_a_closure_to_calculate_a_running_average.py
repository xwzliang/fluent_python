def make_average():
    """
    Compute the mean of an ever-increasing series of values; for example, the average closing price of a commodity over its entire history. Every day a new price is added, and the average is computed taking into account all prices so far.
    >>> avg = make_average()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0

    Inspecting the returned averager object shows how Python keeps the names of local and free variables in the __code__ attribute that represents the compiled body of the function.  Inspecting the returned averager object shows how Python keeps the names of local and free variables in the __code__ attribute that represents the compiled body of the function.
    >>> avg.__code__.co_varnames
    ('new_value', 'total')
    >>> avg.__code__.co_freevars
    ('series',)

    The binding for series is kept in the __closure__ attribute of the returned function avg. Each item in avg.__closure__ corresponds to a name in avg.__code__.co_free vars. These items are cells, and they have an attribute called cell_contents where the actual value can be found.
    >>> avg.__closure__  # doctest: +ELLIPSIS
    (<cell at ...: list object at ...>,)
    >>> avg.__closure__[0].cell_contents
    [10, 11, 12]
    """

    series = []

    def averager(new_value):
        # Within averager, series is a free variable. This is a technical term meaning a variable that is not bound in the local scope.
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


# To summarize: a closure is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is invoked and the defining scope is no longer available.
# Note that the only situation in which a function may need to deal with external variables that are nonglobal is when it is nested in another function.

if __name__ == "__main__":
    import doctest

    doctest.testmod()
