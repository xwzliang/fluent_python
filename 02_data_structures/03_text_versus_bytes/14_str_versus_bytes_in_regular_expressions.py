# If you build a regular expression with bytes, patterns such as \d and \w only match ASCII characters; in contrast, if these patterns are given as str, they match Unicode digits or letters beyond ASCII.

import re

# Regular expressions for str type
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
# Regular expressions for bytes type
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

# Unicode text to search, containing the Tamil digits for 1729 (the logical line continues until the right parenthesis token).
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"	# This string is joined to the previous one at compile time
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

# A bytes string is needed to search with the bytes regular expressions
text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))	# The str pattern r'\d+' matches the Tamil and ASCII digits
print('  bytes:', re_numbers_bytes.findall(text_bytes))	# The bytes pattern rb'\d+' matches only the ASCII bytes for digits
print('Words')
print('  str  :', re_words_str.findall(text_str))	# The str pattern r'\w+' matches the letters, superscripts, Tamil, and ASCII digits
print('  bytes:', re_words_bytes.findall(text_bytes))	# The bytes pattern rb'\w+' matches only the ASCII bytes for letters and digits
