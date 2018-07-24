# AI Player for use in Connect Four   
#

import random
from ps10pr3 import *

class AIPlayer(Player):
    """inherited class from Player that creates an AI computer player"""

    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""

        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

        super().__init__(checker)

    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        s = 'Player ' + str(self.checker) + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """returns the index of the column with the maximum score"""
        max_score = 0
        index_list = []

        for i in range(len(scores)):
            if scores[i] == max(scores):
                index_list += [i]

        if self.tiebreak == 'RIGHT':
            return index_list[-1]

        elif self.tiebreak == 'LEFT':
            return index_list[0]

        elif self.tiebreak == 'RANDOM':
            return random.choice(index_list)


    def scores_for(self, board):
        """determines the called AIPlayer‘s scores for all columns in board"""
        scores = [0]*board.width
        for i in range(len(scores)):
            if board.can_add_to(i) == False:
                scores[i] = -1
            elif board.is_win_for(self.checker):
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                if max(opp_scores) == 50:
                    scores[i] = 50
                elif max(opp_scores) == 100:
                    scores[i] = 0
                elif max(opp_scores) == 0:
                    scores[i] = 100
                board.remove_checker(i)

        return scores


    def next_move(self, board):
        """overrides the next_move method that is inherited from Player and
           returns the column where the player wants to make the next move"""
        self.num_moves += 1
        list_scores = self.scores_for(board)
        return self.max_score_column(list_scores)
