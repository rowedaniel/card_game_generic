from Card import Card
from random import shuffle

class CardCollection:
    __slots__ = (
        'cards', # type Card
        )

    def __init__(self, cardNames : list=[]):
        # initialize each card
        self.cards = [Card(name) for name in cardNames]

    def __getitem__(self, index : int):
        return self.cards[index]
 

    def count_search(self, func) -> int:
        """
        return the number of cards that satisfy <func>.
        Does NOT remove them from this collection.
        """
        return len(list(filter(func, self.cards)))

    def shuffle(self):
        """ shuffles this card collection in-place """
        shuffle(self.cards)
