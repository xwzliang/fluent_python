import time

DEFAULT_FMT = "[{elapsed_time:0.8f}s] {func_name}({arg_str_list}) -> {func_result}"


def clock(fmt=DEFAULT_FMT):
    """
    clock is our parameterized decorator factory.
    >>> @clock()
    ... def snooze(seconds):
    ...     time.sleep(seconds)
    >>> for i in range(3):  # doctest: +ELLIPSIS
    ...     snooze(.123)
    [0.123...s] snooze(0.123) -> None
    [0.123...s] snooze(0.123) -> None
    [0.123...s] snooze(0.123) -> None

    >>> @clock('{func_name}: {elapsed_time}s')
    ... def snooze(seconds):
    ...     time.sleep(seconds)
    >>> for i in range(3):  # doctest: +ELLIPSIS
    ...     snooze(.123)
    snooze: 0.123...s
    snooze: 0.123...s
    snooze: 0.123...s
    """

    # decorate is the actual decorator.
    def decorate(func):
        # clocked wraps the decorated function.
        def clocked(*_args):
            time_started = time.time()
            _result = func(*_args)  # the actual result of the decorated function.
            elapsed_time = time.time() - time_started
            func_name = func.__name__
            arg_str_list = ", ".join(repr(arg) for arg in _args)
            # func_result is the str representation of _result, for display.
            func_result = repr(_result)
            # Using **locals() here allows any local variable of clocked to be referenced in the fmt.
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


if __name__ == "__main__":
    import doctest

    doctest.testmod()
