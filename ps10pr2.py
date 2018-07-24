# A Connect-Four Player class 
#

from ps10pr1 import Board

# write your class below

class Player:
    """a player of the Connect Four game"""

    def __init__(self, checker):
        """constructs a new Player object"""

        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0


    def __repr__(self):
        """returns a string representing a Player object"""
        s = 'Player ' + str(self.checker)
        return s

    def opponent_checker(self):
        """returns a one-character string
           representing the checker of the Player object’s opponent"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """returns the column where the player wants to make the next move"""
        while True:
            input1 = int(input('Enter a column: __'))

            if input1 < 0 or input1 > board.width - 1 or board.can_add_to(input1)==False:
                print('Try Again!')
            else:
                self.num_moves += 1
                return input1
