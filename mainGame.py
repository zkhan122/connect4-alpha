
import math
import numpy as np #type: ignore


class Connect4():

    def __init__(self, ROW_COUNT, COL_COUNT): # accessed in line 38
        self.winning_move = None
        self.game_over = False

        self.board = self.create_board()
    
    
    def create_board(self):
        return np.zeros((self.ROW_COUNT, self.COL_COUNT)) # numpy matrix

    def print_board(self):
        print(np.flip(self.board, 0))

    def drop_piece(self, row, col, piece): # board parameter not needed (using self)
        self.board[row][col] = piece

    def is_valid_location(self, col, ):
        return self.board[self.ROW_COUNT-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def winning_move(self, piece):
           # check horizontal locations for a win
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece:
                    if self.board[r][c+2] and self.board[r][c+3] == piece:
                        return True

        # check for vertical locations for a win
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 2):
                if self.board[r][c] == piece and self.board[r+1][c] == piece:
                    if self.board[r+2][c] and self.board[r+3][c] == piece:
                        return True

        # check for positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece:
                    if self.board[r+2][c+2] and self.board[r+3][c+3] == piece:
                        return True

        # check for negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece:
                    if self.board[r-2][c+2] and self.board[r-3][c+3] == piece:
                        return True


# game loop
def play(game, print_game =  True):
    if print_game:
        game.create_board()
        game.print_board()




if __name__ == '__main__':
    game = Connect4(6, 7)
    play(game, print_game = True)
    print("Case: ")

