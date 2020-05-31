# how do you make a decorator accept other arguments? The answer is: make a decorator factory that takes those ar‐ guments and returns a decorator, which is then applied to the function to be decorated.

registry = set()  # registry is now a set, so adding and removing functions is faster


def register(active=True):
    """
    Note how only the f2 function appears in the registry; f1 does not appear because active=False was passed to the register decorator factory, so the decorate that was applied to f1 did not add it to the registry.
    >>> registry  # doctest: +ELLIPSIS
    {<function f2 at 0x...>}
    
    If, instead of using the @ syntax, we used register as a regular function, the syntax needed to decorate a function f would be register()(f) to add f to the registry, or register(active=False)(f) to not add it (or remove it)
    >>> register()(f3)  # doctest: +ELLIPSIS
    running register(active=True)->decorate(<function f3 at 0x...>)
    <function f3 at 0x...>
    >>> registry  # doctest: +ELLIPSIS
    {<function f2 at 0x...>, <function f3 at 0x...>}
    >>> register(active=False)(f2)  # doctest: +ELLIPSIS
    running register(active=False)->decorate(<function f2 at 0x...>)
    <function f2 at 0x...>
    >>> registry  # doctest: +ELLIPSIS
    {<function f3 at 0x...>}
    """

    # The decorate inner function is the actual decorator; note how it takes a function as argument.
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        if active:
            registry.add(func)
        else:
            # If not active and func in registry, remove it.
            registry.discard(func)
        # Because decorate is a decorator, it must return a function.
        return func

    # register is our decorator factory, so it returns decorate.
    return decorate


# The @register factory must be invoked as a function, with the desired parameters.
@register(active=False)
def f1():
    print("running f1()")


# If no parameters are passed, register must still be called as a function—@register()—i.e., to return the actual decorator, decorate.
@register()
def f2():
    print("running f2()")


def f3():
    print("running f3()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
