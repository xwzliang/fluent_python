import collections

# Construct a simple class to represent individual cards. "namedtuple" can be used to build classes of objects that are just bundles of attributes with no custom methods, like a database record
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    # Responds to the len() function by returning the number of cards in it, like a standard Python collection
    def __len__(self):
        return len(self._cards)
        
    # Allow to read specific cards from the deck, like deck[0] of deck[-1], 
    # And it supports slicing, like deck[:3], deck[12::13](starts on index 12 and skips 13 cards at a time). 
    # And deck now is also iterable by implementing __getitem__ special method: for card in deck: ...
    def __getitem__(self, position):
        return self._cards[position]
