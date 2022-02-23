from Database import cards

class Card:

    __slots__ = (
        'name', # string name of card
        )
    
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return self.name
