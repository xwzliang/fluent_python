from functools import singledispatch
from collections import abc
import numbers
import html


# Because we don't have method or function overloading in Python, we can't create variations of htmlize with different signatures for each data type we want to handle differently. A common solution in Python would be to turn htmlize into a dispatch function, with a chain of if/elif/elif calling specialized functions like htmlize_str, htmlize_int, etc. This is not extensible by users of our module, and is unwieldy: over time, the htmlize dispatcher would become too big, and the coupling between it and the specialized functions would be very tight.
# The new functools.singledispatch decorator in Python 3.4 allows each module to contribute to the overall solution, and lets you easily provide a specialized function even for classes that you can't edit. If you decorate a plain function with @singledispatch, it becomes a generic function: a group of functions to perform the same operation in different ways, depending on the type of the first argument. (This is what is meant by the term single-dispatch. If more arguments were used to select the specific functions, we'd have multiple-dispatch.)
# A notable quality of the singledispatch mechanism is that you can register specialized functions anywhere in the system, in any module. If you later add a module with a new user-defined type, you can easily provide a new custom function to handle that type. And you can write custom functions for classes that you did not write and can't change.

# @singledispatch marks the base function that handles the object type.
@singledispatch
def htmlize(obj):
    """
    By default, the HTML-escaped repr of an object is shown enclosed in <pre></ pre>.
    >>> htmlize({1, 2, 3})
    '<pre>{1, 2, 3}</pre>'
    >>> htmlize(abs)
    '<pre>&lt;built-in function abs&gt;</pre>'
    >>> htmlize('Heimlich & Co.\\n- a game')  # backslash needs to be escaped in docstring
    '<p>Heimlich &amp; Co.<br>\\n- a game</p>'
    
    An int is shown in decimal and hexadecimal, inside <pre></pre>.
    >>> htmlize(42)
    '<pre>42 (0x2a)</pre>'
    
    Each list item is formatted according to its type, and the whole sequence rendered as an HTML list.
    >>> print(htmlize(['alpha', 66, {3, 2, 1}]))
    <ul>
    <li><p>alpha</p></li>
    <li><pre>66 (0x42)</pre></li>
    <li><pre>{1, 2, 3}</pre></li>
    </ul>
    """
    content = html.escape(repr(obj))
    return "<pre>{}</pre>".format(content)


# Each specialized function is decorated with @«base_function».regis ter(«type»).
@htmlize.register(str)
# The name of the specialized functions is irrelevant; _ is a good choice to make this clear.
def _(text):
    content = html.escape(text).replace("\n", "<br>\n")
    return "<p>{0}</p>".format(content)


# For each additional type to receive special treatment, register a new function. numbers.Integral is a virtual superclass of int.
@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)


# When possible, register the specialized functions to handle ABCs (abstract classes) such as numbers.Integral and abc.MutableSequence instead of concrete implementations like int and list. This allows your code to support a greater variety of compatible types. For example, a Python extension can provide alternatives to the int type with fixed bit lengths as subclasses of numbers.Integral.
# Using ABCs for type checking allows your code to support existing or future classes that are either actual or virtual subclasses of those ABCs.
# You can stack several register decorators to support different types with the same function.
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"


# @singledispatch is not designed to bring Java-style method overloading to Python. A single class with many overloaded variations of a method is better than a single function with a lengthy stretch of if/elif/elif/elif blocks. But both solutions are flawed because they concentrate too much responsibility in a single code unit—the class or the function. The advantage of @sin gledispath is supporting modular extension: each module can register a specialized function for each type it supports.


if __name__ == "__main__":
    import doctest

    doctest.testmod()
