import sys, locale

expressions = """
	locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
"""
# locale.getpreferredencoding is the most important setting
# The output is going to the console, so sys.stdout.isatty() is True, if it's redirected to a file, sys.stdout.isatty() will become False
# The best practice about encoding defaults is: do not rely on them. Always be explicit about the encodings in your programs when read/write files.

my_file = open('dummy.swp', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

my_file.close()
