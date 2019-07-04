# One of the best features of Python functions is the extremely flexible parameter handling mechanism, enhanced with keyword-only arguments in Python 3. Closely related are the use of * and ** to “explode” iterables and mappings into separate arguments when we call a function.

def tag(name, *content, cls=None, **attrs):
    """
    Generate one or more HTML tags
    >>> tag('br')
    '<br />'
    >>> tag('p', 'hello')
    '<p>hello</p>'
    >>> print(tag('p', 'hello', 'world'))	# Any number of arguments after the first are captured by *content as a tuple.
    <p>hello</p>
    <p>world</p>
    >>> tag('p', 'hello', id=33)	# Keyword arguments not explicitly named in the tag signature are captured by **attrs as a dict.
    '<p id="33">hello</p>'
    >>> print(tag('p', 'hello', 'world', cls='sidebar'))	# The cls parameter can only be passed as a keyword argument. This is a way as a workaround because class is a keyword in Python
    <p class="sidebar">hello</p>
    <p class="sidebar">world</p>
    >>> tag(content='testing', name="img")	# Even the first positional argument can be passed as a keyword when tag is called.
    '<img content="testing" />'
    >>> my_tag = {'name':'img', 'title':'Sunset Boulevard',
    ...           'src': 'sunset.jpg', 'cls':'framed'}
    >>> tag(**my_tag)	# Prefixing the my_tag dict with ** passes all its items as separate arguments, which are then bound to the named parameters, with the remaining caught by **attrs.
    '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                	    for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                	 (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
Keyword-only arguments are a new feature in Python 3. In above example, the cls parameter can only be given as a keyword argument—it will never capture unnamed positional arguments. To specify keyword-only arguments when defining a function, name them after the argument prefixed with *. If you don't want to support variable positional arguments but still want keyword-only arguments, put a * by itself in the signature, like this:
    >>> def f(a, *, b):
    ... 	return a, b
    >>> f(1, b=2)
    (1, 2)

Note that keyword-only arguments do not need to have a default value: they can be mandatory, like b in the preceding example.
"""
