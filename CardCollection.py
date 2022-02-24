from Card import Card
from random import shuffle

class CardCollection:
    """
    General card collection (e.g. hand, deck, discard, etc.) class.
    One founding idea of these card collections is that you should never be
    able to accidentally delete cards.
    For this reason, there is a move() method, but no pop() or similar.
    """
    
    __slots__ = (
        'cards', # type Card
        'name',  # string name
        )

    def __init__(self, cards : list=[], name : str=""):
        
        self.name = name
        
        # initialize each card
        self.cards = [Card(name) for name in cards]


    # testing only
    def __getitem__(self, index : int):
        """
        Question: is this a thing I want people to be able to do?
        Could result in some accidental modifying of cards.
        Maybe for testing only?
        """
        return self.cards[index]

    def __iter__(self):
        for c in self.cards:
            if c is None:
                continue
            yield c
    
    def __str__(self) -> str:
        return ' '.join(str(c) for c in self)

    

    # private--should NOT be called outside of this class
    def check_card(self, c : int) -> int:
        return min(max(0,i),len(self.cards)-1)


    # public--can be called outside of this class
    def __contains__(self, cardName : str):
        return any([str(c)==cardName for c in self.cards])
    
    def additems(self, items : list) -> list:
        """
        takes a list of cards, and adds them to this collection.
        returns the indicies to the cards added.
        """
        self.cards.extend(items)
        return range(len(self.cards)-len(items), len(self.cards))

    def notify(self, message : str, indicies : list):
        for index in indicies:
            i = self.check_card(index)
            if self.cards[i] is None: continue
            self.cards[i].notify(message)
        
    def move(self, indicies : list, target) -> list:
        """
        Move all cards (based off of indicies) to target CardCollection.
        Populate the empty spaces with None, to avoid index confusion.
        Returns a list of commands triggered by various cards
        """
        target_indicies= target.additems(
            [self.cards[self.check_card(i)] for i in indicies]
            )
        commands = []
        for index in indicies:
            i = self.check_card(index)
            if self.cards[i] is None: continue
            
            commands.append(self.cards[i].notify(
                            f'move:{self.name}-{target.name}'))
            self.cards[i] = None
            
        return zip(target_indicies, commands)

    def clear_nones(self):
        """
        Clears all None from card list.
        (The Nones get there when cards are moved out of this array.
        """
        while None in self.cards:
            self.cards.remove(None)
            

    def search(self, func) -> list:
        """
        return the indices of cards that satisfy <func>.
        Does NOT remove them from this collection.
        """
        return 

    def shuffle(self):
        """ shuffles this card collection in-place """
        shuffle(self.cards)
