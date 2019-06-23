"""
test for shave_marks
>>> order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
>>> shave_marks(order)	# Only the letters “è”, “ç”, and “í” were replaced.
'“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'
>>> Greek = 'Ζέφυρος, Zéfiro'
>>> shave_marks(Greek)	# Both “έ” and “é” were replaced.
'Ζεφυρος, Zefiro'

test for dewinize and asciize
>>> order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
>>> dewinize(order)	# dewinize replaces curly quotes, bullets, and ™ (trademark symbol)
'"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."'
>>> asciize(order)	# asciize applies dewinize, drops diacritics, and replaces the 'ß'
'"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'

"""
import unicodedata
import string

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)	# Decompose all characters into base characters and combining marks
    shaved = ''.join(c for c in norm_txt
            	    if not unicodedata.combining(c))	# Filter out all combining marks
    return unicodedata.normalize('NFC', shaved)	# Recompose all characters

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        # Skip over combining marks when base character is Latin
        if unicodedata.combining(c) and latin_base:
            continue	# ignore diacritic on Latin base char
        keepers.append(c)	# Otherwise, keep current character
        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):	# Detect new base character and determine if it's Latin
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


# Transform some Western typographical symbols in Western texts

# Build mapping table for char-to-char replacement
single_map = str.maketrans("""‚ƒ„†ˆ‹‘'“”•–—˜›""",
        		    """'f"*^<''""---~>""")

# Build mapping table for char-to-string replacement
multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)	# Merge mapping tables

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    # dewinize does not affect ASCII or latin1 text, only the Microsoft additions in to latin1 in cp1252.
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    # Replace the Eszett with “ss” (we are not using case fold here because we want to preserve the case)
    no_marks = no_marks.replace('ß', 'ss')
    # Apply NFKC normalization to compose characters with their compatibility code points
    return unicodedata.normalize('NFKC', no_marks)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
