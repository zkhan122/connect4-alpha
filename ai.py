from mainGame import *

class RandomAI():

    def __init__(self, board):
        self.board = board
    
    def score_position(self, piece):
        # score horizontal
        score = 0
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r, :])]
            for c in range(COLUMN_COUNT-3):
                connect = row_array[c : c + CONNECT_LENGTH]
                if connect.count(piece) == CONNECT_LENGTH:
                    score += 100 
                elif connect.count(piece) == 3 and score.count(EMPTY) == 1:
                    score += 10

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
