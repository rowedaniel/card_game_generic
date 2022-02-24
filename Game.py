from Player import Player
from CardCollection import CardCollection
from Database import decks


class Game:

    __slots__ = (
        'players', # array of type Player
        'commands', # dictionary of valid commands
        'stack',
        
        )
    
    def __init__(self, numPlayers):
        self.players = [
            Player() for i in range(numPlayers)
            ]

        # for card executing purposes
        self.stack = []
        
        self.commands = {
            # stack commands
            'END'  : self.C_end, # end program
            'PNT'  : self.C_print, # debugging purposes only
            'DUP'  : self.C_duplicate, # duplicate top item of stack
            'SWP'  : self.C_swap, # swap last 2 items on stack
            'DRP'  : self.C_drop, # delete last item on stack
            'CYL'  : self.C_cycle, # swap last n items on stack (n=stack.pop())
            'ADD'  : self.C_add, # add last 2 items
            'SUB'  : self.C_subtract, # add last 2 items
            # card commands
            'CMOV' : self.C_move_cards, # moves cards between collections
            
        }

        # add number commands 0-9
        for i in range(10):
            self.commands[str(i)] = self.get_C_num_command(i)

    # private methods
    def check_player(self, p : int):
        """ takes an input player id, and returns an in-range version. """
        return min(max(0, p), len(self.players))



    def move_cards(self,
                   p : int,
                   c1 : int,c2 : int,
                   indicies : list):
        """
        moves cards from p1's c1 collection to c2 collection.
        Then, executes any card actions received along the way
        """
        p = self.check_player(p)
        actions = self.players[p].move_cards(c1, c2, indicies)

        for action in actions:
            self.stack_set((p, c1, c2, action[0]))
            self.C_execute(action[1])
            



    # non-card commands that manipulate stack
    def stack_reset(self):
        self.stack = []

    def stack_extend(self, items : list):
        self.stack.extend(items)

    def stack_set(self, items : list):
        self.stack_reset()
        self.stack_extend(items)

    # card commands
    def C_execute(self, action):
        print(action)
        i = 0
        while i < len(action):
            if action[i] not in self.commands:
                i += 1
                continue
            
            jump, jumpto = self.commands[action[i]]()
            
            if jump:
                if jumpto == 0: break
                i += jumpto
            else:
                i += 1



    def C_end(self):
        return True, 0
    
    def C_duplicate(self):
        self.stack.append(self.stack[-1])
        return False, 0

    def C_swap(self):
        if len(self.stack) < 2: return False, 0
        a = self.stack[-1]
        self.stack[-1] = self.stack[-2]
        self.stack[-2] = a
        return False, 0

    def C_add(self):
        """ pops first 2 stack items then adds their sum to stack """
        if len(self.stack) < 2: return False, 0
        self.stack.append(self.stack.pop() + self.stack.pop())
        return False, 0

    def C_subtract(self):
        """ pops first 2 stack items then adds their difference to stack """
        if len(self.stack) < 2: return False, 0
        self.stack.append(self.stack.pop() - self.stack.pop())
        return False, 0

    def C_drop(self):
        self.stack.pop()
        return False, 0

    def C_cycle(self):
        """
        cycles items in the stack.
        stack expectations (up=top of stack):
          - # of stack items to cycle
          - [list of items to cycle]
        example:
          stack = 1 2 3 4 4
          cycle()
          stack-> 4 1 2 3
        
        """

        if len(self.stack) < 1: return False, 0
        a = self.stack.pop()
        if a >= len(self.stack): a = len(self.stack)
        elif a < 1: a = 1
        self.stack.insert(len(self.stack)-a, self.stack.pop())
        return False, 0

    def C_move_cards(self):
        """
        moves cards from one collection to another within a player.
        stack expectations (up=top of stack):
          - the number of cards to move
          - player's number
          - target collection's number
          - source collection's number
          - [list of card indicies]
        """
        if len(self.stack) < 4: return False, 0
        count       = self.stack.pop()
        player      = self.stack.pop()
        target      = self.stack.pop()
        source      = self.stack.pop()

        indicies = []
        for i in range(count):
            indicies.append(self.stack.pop())

        print('count:',count)
        print('player:',player)
        print('source:',source)
        print('target:',target)
        print('indicies:',indicies)
        self.move_cards(player, source, target, indicies)
                        
        return False, 0
    
    # testing purposes only
    def C_print(self):
        """ prints top item from stack (removing it) """
        if len(self.stack) < 1: return False, 0
        print('stack item:', self.stack.pop())
        return False, 0


    def get_C_num_command(self,i):
        """ returns functions which push numbers 0-9 to the stack """
        def C_num_command():
            f""" pushes {i} to the stack. """
            self.stack.append(i)
            return False, 0
        return C_num_command





        




def main():
    g = Game(2)
    return g

if __name__ == '__main__':
    g = main()
