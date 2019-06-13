"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)	# Get the list of occurrences for word, or set it to [] if not found; setdefault returns the value, so it can be updated without requiring a second search. It's the same as follows (but the following code performs at least two searches for key -- three if it's not found -- while setdefault does it all with a single lookup):
            """
            if key not in my_dict:
            	my_dict[key] = []
            my_dict[key].append(new_value)
            """
    # print in alphabetical order
    for word in sorted(index, key=str.upper):	# Pass the str.upper as reference so the sorted function can use it to normalize the words for sorting
        print(word, index[word])
