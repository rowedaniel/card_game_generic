from Database import decks
from CardCollection import CardCollection

class Player:

    __slots__ = (
        'collections' # array of CardCollections. 0th element must be the deck
        )
    
    def __init__(self, deckName : str):


        # init all collections
        self.collections = [
            CardCollection(decks[deckName]), # deck
            CardCollection(),                # hand
            CardCollection(),                # discard
            ]

        # shuffle deck
        self.collections[0].shuffle()


    def move(self, c1 : int, c2 : int, indicies : list):
        """ moves <count> cards from collection <c1> to collection <c2>. """
        

    def get_collection_size(self, c : int) -> int:
        return len(self.collections[c])
