from Database import decks
from CardCollection import CardCollection

class Player:

    Deck = 0
    Hand = 1
    Discard = 2

    __slots__ = (
        'collections', # array of CardCollections. 0th element must be the deck

        )
    
    def __init__(self):


        # init all collections
        self.collections = []


    # private methods
    def check_collection(self, c : int) -> int:
        """ takes an input collection id, and returns an in-range version. """
        return min(max(0, c), len(self.collections)-1)



    # public methods
    def move_cards(self, c1 : int, c2 : int, indicies : list) -> list:
        """
        moves <count> cards from collection <c1> to collection <c2>.
        returns resultant card action command-strings
        """
        # squeeze c1, c2 to fit into collection
        c1 = self.check_collection(c1)
        c2 = self.check_collection(c2)
        return self.collections[c1].move(indicies, self.collections[c2])

    def notify_cards(self, message : str, c : int, indicies : list):
        c = self.check_collection(c)
        self.collections[c].notify_cards(message, indicies)
        

    def get_collection_size(self, c : int) -> int:
        return len(self.collections[c])
