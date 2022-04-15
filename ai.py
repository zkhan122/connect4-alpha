
from mainGame import *
import random

class RandomAI():

    def __init__(self, board):
        self.board = board

    def evaluate_connection(self, connect, piece):

        score = 0
        
        opponent = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opponent = AI_PIECE
        
        if connect.count(piece) == 4:
            score += 100 
        elif connect.count(piece) == 3 and connect.count(EMPTY) == 1:
            score += 10
        elif connect.count(piece) == 2 and connect.count(EMPTY) == 2:
            score += 5
        
        if connect.count(opponent) == 4 and connect.count(EMPTY) == 1:
            score -= 80 

        return score
    
    def score_position(self, piece):

        score = 0

        # score center
        center_array = [int(i) for i in list(self.board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)

        score += center_count * 6

        # score horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r, :])]
            for c in range(COLUMN_COUNT-3):
                connect = row_array[c : c + CONNECT_LENGTH]

                self.evaluate_connection(connect, piece)
        
        # score vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board[:, c])]
            for r in range(ROW_COUNT-3):
                connect = col_array[r: r + CONNECT_LENGTH]

                self.evaluate_connection(connect, piece)


        # score positively sloped diagonals
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                connect = [self.board[r+i][c+i] for i in range(CONNECT_LENGTH)]

                self.evaluate_connection(connect, piece)
        # score negatively sloped diagonals
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                connect = [self.board[r+i][c+i] for i in range(CONNECT_LENGTH)]

                self.evaluate_connection(connect, piece)

        return score

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if is_valid_location(board, col):
                valid_locations.append(col)
        
        return valid_locations

    def pick_best_move(self, piece):

        valid_locations = self.get_valid_locations(self.board)
        best_score = 0
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(self.board, col)
            temp_board = self.board.copy()
            drop_piece(temp_board, row, col, piece)
            score = self.score_position(piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

