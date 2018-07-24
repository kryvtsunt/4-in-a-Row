# Playing the game 
#

from ps10pr1 import Board
from ps10pr2 import Player
import random

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board


def process_move(player, board):
    """performs all of the steps involved in processing a single move
       by the specified player on the specified board"""
    print()
    s = player.__repr__() + "'s turn"
    print(s)

    chosen_col = player.next_move(board)

    Board.add_checker(board, player.checker, chosen_col)
    print()
    print(board)
    print()

    if Board.is_win_for(board, player.checker) == True:
        print(player.__repr__(), 'wins in', player.num_moves, 'moves.')
        print('Congratulations!')
        return True
    elif Board.is_full(board) == True and Board.is_win_for(board, player.checker) == False:
        print("It's a tie!")
        return True
    else:
        return False



class RandomPlayer(Player):
    """inherited class from Player that creates an unintelligent computer player"""

    def next_move(self, board):
        list_available_col = []
        for i in range(board.width):
            if Board.can_add_to(board, i) == True:
                list_available_col += [i]

        chosen_col = random.choice(list_available_col)
        self.num_moves += 1
        return chosen_col
