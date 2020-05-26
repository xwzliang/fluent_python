import time


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
    
    clock gets the factorial function as its func argument. It then creates and returns the clocked function, which the Python interpreter assigns to factorial behind the scenes
    factorial = clock(factorial)
    So factorial now actually holds a reference to the clocked function. From now on, each time factorial(n) is called, clocked_func(n) gets executed.
    >>> factorial.__name__
    'clocked_func'
    >>> snooze.__name__
    'clocked_func'
    """

    def clocked_func(
        *args,  # Define inner function clocked to accept any number of positional arguments
    ):
        time_started = time.perf_counter()
        result = func(
            *args
        )  # This line only works because the closure for clocked encompasses the func free variable.
        elapsed_time = time.perf_counter() - time_started
        func_name = func.__name__
        arg_str_list = ", ".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed_time, func_name, arg_str_list, result))
        # This is the typical behavior of a decorator: it replaces the decorated function with a new function that accepts the same arguments and (usually) returns whatever the decorated function was supposed to return, while also doing some extra processing.
        return result

    return clocked_func


if __name__ == "__main__":
    import doctest

    doctest.testmod()
