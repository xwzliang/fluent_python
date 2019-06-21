# This example demonstrates the effect of loading three dicts with the same data, just in different order. The resulting dictionaries all compare equal, even if their order is not the same.

DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3	# The dictionaries compare equal, because they hold the same key:value pairs

"""
Adding items to a dict may change the order of existing keys, because the Python interpreter may decide that the hash table of that dictionary needs to grow. And this is implementation-dependent, so we cannot reliably predict when it will happen.

This is why modifying the contents of a dict while iterating through it is a bad idea. If you need to scan and add items to a dictionary, do it in two steps: read the dict from start to finish and collect the needed additions in a second dict. Then update the first one with it.
"""
