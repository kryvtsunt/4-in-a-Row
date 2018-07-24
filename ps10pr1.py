# Board Class

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions"""

#Function 1

    def __init__(self, height, width):
        """constructor for Board objects"""
        self.height = height
        self.width = width
        self.slots = [[' ']*width for r in range(height)]


#Function 2

    def __repr__(self):
        """returns a string representing a Board object"""
        s = ''

        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        s += '-'*(self.width+ self.width+1)
        s += '\n'

        for i in range(self.width):
            if i < 10:
                s += ' ' + str(i)
            else:
                s += ' ' + str(i-10)
        return s


#Function 3

    def add_checker(self, checker, col):
        """adds a specified checker to the board"""

        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = -1
        while self.slots[row][col] != ' ':
            row -= 1

        self.slots[row][col] = checker


#Function 4

    def reset(self):
        """reset the Board object on which it ismcalled by
           setting all slots to contain a space character"""

        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '


#Function 5

    def add_checkers(self, colnums):
        """takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object,
        starting with 'X'."""

        checker = 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


#Function 6

    def can_add_to(self, col):
        """returns True if it is valid to place a checker
           in the column on the calling Board object
           ans returns False otherwise."""
        if col < 0 or col >= self.width:
            return False
        else:
            for row in range(self.height):
                if self.slots[row][col] == ' ':
                    return True
                else:
                    return False
#Function 7

    def is_full(self):
        """returns True if the called Board object is completely full
           of checkers, and returns False otherwise"""
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        else:
            return True


#Function 8

    def remove_checker(self, col):
        """removes the top checker from column col of the called Board object"""
        row = 0
        while self.slots[row][col] == ' ' and row <= self.height - 2:
                row += 1

        self.slots[row][col] = ' '


#Function 9

#Helper functions

    def is_horizontal_win(self, checker):
        """ checks for a horizontal win for the specified checker"""
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
        return False


    def is_vertical_win(self, checker):
        """checks for a vertical win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
        return False


    def is_up_diagonal_win(self, checker):
        """checks for a up diagonal win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(3, self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                       return True
        return False


    def is_down_diagonal_win(self, checker):
        """checks for a down diagonal win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
        return False

#is_win cumulative function

    def is_win_for(self, checker):
        """checks for a win for the specified checker"""
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
