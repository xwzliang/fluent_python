# Our previous implementation of make_averager was not efficient. We stored all the values in the historical series and computed their sum every time averager was called. A better implementation would just store the total and the number of items so far, and compute the mean from these two numbers.


def make_average_broken():
    """
    >>> avg = make_average_broken()
    >>> avg(10)  # doctest +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: local variable 'count' referenced before assignment
    """

    count = 0
    total = 0

    def averager(new_value):
        # The problem is that the statement count += 1 actually means the same as count = count + 1, when count is a number or any immutable type. So we are actually assigning to count in the body of averager, and that makes it a local variable. The same problem affects the total variable.
        # We did not have this problem in previous example because we never assigned to the series name; we only called series.append and invoked sum and len on it. So we took advantage of the fact that lists are mutable.
        # But with immutable types like numbers, strings, tuples, etc., all you can do is read, but never update. If you try to rebind them, as in count = count + 1, then you are implicitly creating a local variable count. It is no longer a free variable, and therefore it is not saved in the closure.
        count += 1
        total += new_value
        return total / count

    return averager


def make_average():
    """
    >>> avg = make_average()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0
    """

    count = 0
    total = 0

    def averager(new_value):
        # The nonlocal declaration was introduced in Python 3. It lets you flag a variable as a free variable even when it is assigned a new value within the function. If a new value is assigned to a nonlocal variable, the binding stored in the closure is changed.
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == "__main__":
    import doctest

    doctest.testmod()
