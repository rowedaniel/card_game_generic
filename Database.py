decks = {
    'deck1': ['card1','card3', 'card2'],
    }

cards = {
    'card1' : {
        'action': {
            'move:deck-hand': 'PNT PNT PNT PNT PNT'.split(' '),
            },
        },
    'card2' : {
        'action': {
            'move:deck-hand': '1 2 3 4 4 CYL PNT PNT PNT PNT'.split(' '),
            },
        },
    
    'card3' : {
        'action': {
            'move:deck-hand': '4 CYL SWP DRP 2 3 CYL 3 CYL 1 CMOV'.split(' '),
            },
        },
    }

history = []
