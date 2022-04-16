from mainGame import *
import random
import math

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
            score += 5
        elif connect.count(piece) == 2 and connect.count(EMPTY) == 2:
            score += 2
        
        if connect.count(opponent) == 4 and connect.count(EMPTY) == 1:
            score -= 4

        return score
    
    def score_position(self, piece):

        score = 0

        ## Score center column
        center_array = [int(i) for i in list(self.board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r,:])]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+CONNECT_LENGTH]
                score += self.evaluate_connection(window, piece)

        ## Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board[: , c])]
            for r in range(ROW_COUNT-3):
                window = col_array[r: r + CONNECT_LENGTH]
                score += self.evaluate_connection(window, piece)

        ## Score posiive sloped diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [self.board[r+i][c+i] for i in range(CONNECT_LENGTH)]
                score += self.evaluate_connection(window, piece)

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [self.board[r+3-i][c+i] for i in range(CONNECT_LENGTH)]
                score += self.evaluate_connection(window, piece)

        return score


    def is_terminal_node(self): #is the final node to be traversed (end of game)
        return winning_move(self.board, PLAYER_PIECE) or winning_move(self.board, AI_PIECE) or len(self.get_valid_locations()) == 0

# minimax

    def minimax(self, board, depth, maximizingPlayer):

        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:

            if is_terminal:
                
                if winning_move(self.board, AI_PIECE):
                    return (None, math.inf)
                elif winning_move(self.board, PLAYER_PIECE):
                    return (None, -math.inf)
                else:
                    # not winning condition
                    return (None, 0) # game_over - no more valid moves
            
            else: # depth is 0    
                return (None, self.score_position(AI_PIECE))
        
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = get_next_open_row(self.board, col)
                dup_board = self.board.copy()
                drop_piece(dup_board, row, col, AI_PIECE)
                new_score = self.minimax(dup_board, depth - 1, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
            return new_score, value

        else: # minimizing player
            value = math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = get_next_open_row(self.board, col)
                dup_board = self.board.copy()
                drop_piece(dup_board, row, col, PLAYER_PIECE)
                new_score = self.minimax(dup_board, depth - 1, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return new_score, value
        

    def get_valid_locations(self):
        valid_locations = []    
        for col in range(COLUMN_COUNT):
            if is_valid_location(self.board, col):
                valid_locations.append(col)
        
        return valid_locations

    def pick_best_move(self, piece):

        valid_locations = self.get_valid_locations()
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
