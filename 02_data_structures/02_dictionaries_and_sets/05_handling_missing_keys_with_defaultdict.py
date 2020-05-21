"""Build an index mapping word -> list of occurrences"""

import collections
import re
import sys

WORD_RE = re.compile("\w+")

index = collections.defaultdict(
    list
)  # Create a defaultdict with the list constructor as default_factory
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(
                location
            )  # If word is not initially in the index, the default_factory is called to produce the missing value, which in this case is an empty list that is then assigned to index[word] and returned, so the .append(location) operation always succeeds. If no default_factory is provided, the usual KeyError is raised for missing keys.
            # The default_factory of a defautdict is only invoked to provide default values for __getitem__ calls. For example, if dd is a defaultdict, and k is a missing key, dd[k] will call the default_factory to create a default value, but dd.get(k) still returns None.

    # print in alphabetical order
    for word in sorted(index, key=str.upper):
        print(word, index[word])
