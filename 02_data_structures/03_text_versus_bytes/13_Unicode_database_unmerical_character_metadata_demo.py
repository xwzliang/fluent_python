import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),	# Code point in U+0000 format
            char.center(6),	# Character centralized in a str of length 6
            're_dig' if re_digit.match(char) else '-',
            'isdig' if char.isdigit() else '-',
            'isnum' if char.isnumeric() else '-',
            format(unicodedata.numeric(char), '5.2f'),	# Numeric value formated with width 5 and 2 decimal places
            unicodedata.name(char),
            sep='\t')

# The result shows that the regular expression r'\d' matches the digit “1” and the De‐ vanagari digit 3, but not some other characters that are considered digits by the isdi git function. The re module is not as savvy about Unicode as it could be.
