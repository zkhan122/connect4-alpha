import numpy as np    
import math
from player import *


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # check horizontal locations for a win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece:
                if board[r][c+2] and board[r][c+3] == piece:
                    return True

    # check for vertical locations for a win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 2):
            if board[r][c] == piece and board[r+1][c] == piece:
                if board[r+2][c] and board[r+3][c] == piece:
                    return True

    # check for positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece:
                if board[r+2][c+2] and board[r+3][c+3] == piece:
                    return True

    # check for negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece:
                if board[r-2][c+2] and board[r-3][c+3] == piece:
                    return True




def play(board, player_one, player_two, print_game=True):

    game_over = False
    turn = 0 # player 1

    if print_game:
        print_board(board)

    while not game_over:

        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("Player 1 Wins! Congrats!")
                    game_over = True
        
        else:
            col = int(input("Player 2 Make your Selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 Wins! Congrats!")
                    game_over = True

                
        print_board(board)
        
        turn += 1
        turn = turn % 2


if __name__ == '__main__':
    board = create_board()
    player_1 = RandomPlayer(1)
    player_2 = RandomPlayer(2)
    play(board, player_1, player_2, print_game=True)
