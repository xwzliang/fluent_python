# Each argument in the function declaration may have an annotation expression preceded by :. If there is a default value, the annotation goes between the argument name and the = sign. To annotate the return value, add -> and another expression between the ) and the : at the tail of the function declaration. The expressions may be of any type. 


def clip(text:str, max_len:'int > 0'=80) -> str:	# The annotated function declaration
    """
    Return text clipped at the last space before or after max_len

    The only thing Python does with annotations is to store them in the __annotations__ attribute of the function. Nothing else: no checks, enforcement, validation, or any other action is performed. In other words, annotations have no meaning to the Python interpreter. They are just metadata that may be used by tools, such as IDEs, frameworks, and decorators.
    >>> clip.__annotations__
    {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}

    inspect.signature() knows how to extract the annotations
    >>> from inspect import signature
    >>> sig = signature(clip)
    >>> sig.return_annotation
    <class 'str'>
    >>> for param in sig.parameters.values():
    ... 	note = repr(param.annotation).ljust(13)
    ... 	print(note, ':', param.name, '=', param.default)
    <class 'str'> : text = <class 'inspect._empty'>
    'int > 0'     : max_len = 80
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:	# no spaces were found
            end = len(text)
        return text[:end].rstrip()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
