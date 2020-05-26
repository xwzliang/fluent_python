import time
import functools


def clock(func):
    """
    A simple decorator to output the running time of functions
    >>> @clock
    ... def snooze(snooze_seconds):
    ...     time.sleep(snooze_seconds)
    >>> @clock
    ... def factorial(num):
    ...     return 1 if num < 2 else num * factorial(num-1)
    >>> snooze(.123)  # doctest: +ELLIPSIS
    [0.123...s] snooze(0.123) -> None
    >>> factorial(5)  # doctest: +ELLIPSIS
    [0.000...s] factorial(1) -> 1
    [0.000...s] factorial(2) -> 2
    [0.000...s] factorial(3) -> 6
    [0.000...s] factorial(4) -> 24
    [0.000...s] factorial(5) -> 120
    120
    
    After using functools.wraps to copy func attributes, now the __name__ of the returned functions are the same as the original name
    >>> factorial.__name__
    'factorial'
    >>> snooze.__name__
    'snooze'
    """

    @functools.wraps(func)
    def clocked_func(
        *args,  **kwargs  # Define inner function clocked to accept any number of positional arguments and keyword arguments
    ):
        time_started = time.perf_counter()
        result = func(*args)
        elapsed_time = time.perf_counter() - time_started
        func_name = func.__name__
        arg_list = []
        if args:
            arg_list.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            arg_key_value_pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(arg_key_value_pairs))
        arg_str_list = ', '.join(arg_list)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed_time, func_name, arg_str_list, result))
        return result

    return clocked_func


if __name__ == "__main__":
    import doctest

    doctest.testmod()
