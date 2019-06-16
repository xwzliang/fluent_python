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
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])	# Get the list of occurrences for word, or [] if not found
            occurrences.append(location)	# Append new location to occurrences
            index[word] = occurrences	# Put changed occurrences into index dict; this entails a second search through the index
    # print in alphabetical order
    for word in sorted(index, key=str.upper):	# Pass the str.upper as reference so the sorted function can use it to normalize the words for sorting
        print(word, index[word])
