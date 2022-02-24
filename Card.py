from Database import cards


class Card:

    __slots__ = (
        'name', # string name of card
        'action',
        )
    
    def __init__(self, name : str):
        self.name = name
        self.action = cards[name]['action']

    # testing only
    def __str__(self):
        return self.name

    # public--can be called anywhere
    def notify(self, message : str):
        print(f'{self.name} recieved message: {message}')
        if message in self.action:
            return self.action[message]
        return []

        
    
