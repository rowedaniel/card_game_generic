from Player import Player


class Game:

    __slots__ = (
        'players', # array of type Player
        )
    
    def __init__(self, numPlayers, deckNames):
        self.players = [
            Player(deckNames[i]) for i in range(numPlayers)
            ]

    def test(self):
        print(len(self.players[0].collections[0]))
        




def main():
    g = Game(2, ['deck1','deck1'])
    g.test()
    
if __name__ == '__main__':
    main()
