from menu import Menu
from player import *
from ai import *
from menu import *
from cProfile import label
import numpy as np    
import pygame
import sys
import tkinter as ttk
import math
from PIL import Image
import random



ROW_COUNT = 6
COLUMN_COUNT = 7
square_size = 100 # in px - GUI
width = COLUMN_COUNT * square_size 
height = (ROW_COUNT+1) * square_size 
radius = int(square_size / 2 - 5) 

color_blue = (23,64,154) # rgb
color_black = (0, 0, 0)
color_white = (255,255,255)
color_red = (195, 48, 48)
color_yellow = (209, 183, 15)

size = (width, height)

pygame.font.init()
font = pygame.font.SysFont("Lexend Deca", 30) # font
winning_font = pygame.font.SysFont("Lexend Deca", 70) # winning move font

# image processing
# C:\\Users\\ayesh\\OneDrive\\Documents\\Zayaan\\code base\\nea
img1 = pygame.image.load("C:\\Users\\ayesh\\OneDrive\\Documents\\Zayaan\\code base\\nea\\p1.jpg")
img1 = pygame.transform.scale(img1, (30, 30))

img2 = pygame.image.load("C:\\Users\\ayesh\\OneDrive\\Documents\\Zayaan\\code base\\nea\\p2.jpg")
img2 = pygame.transform.scale(img2, (30, 30))

end_gameImg = pygame.image.load("C:\\Users\\ayesh\\OneDrive\\Documents\\Zayaan\\code base\\nea\\gameOverimg.png")
end_gameImg = pygame.transform.scale(end_gameImg, (500, 100))

text_1 = font.render("Player 1", True, color_white)
text_2 = font.render("Player 2", True, color_white)

# game variables
PLAYER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2

CONNECT_LENGTH = 4
EMPTY = 0


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 # check if space is empty


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
                if board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

    # check for vertical locations for a win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece:
                if board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

    # check for positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece:
                if board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

    # check for negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece:
                if board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True


def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+CONNECT_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+CONNECT_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(CONNECT_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(CONNECT_LENGTH)]
			score += evaluate_window(window, piece)

	return score

def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, maximizingPlayer):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return (None, 100000000000000)
			elif winning_move(board, PLAYER_PIECE):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, False)[1]
			if new_score > value:
				value = new_score
				column = col

		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, True)[1]
			if new_score < value:
				value = new_score
				column = col

		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

def pick_best_move(board, piece):

	valid_locations = get_valid_locations(board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(board, col)
		temp_board = board.copy()
		drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col




def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, color_blue, (c * square_size, r * square_size+square_size, square_size*4, square_size) )

           # if board[r][c] == 0: # if empty space
            pygame.draw.circle(screen, color_black, (int(c * square_size + square_size / 2), 
            int(r * square_size + square_size + square_size / 2)), radius)
   
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE: # player 1 - red
                pygame.draw.circle(screen, color_red, ( int(c * square_size + square_size / 2), 
                height - int(r * square_size + square_size / 2) ), radius) 

            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, color_yellow, ( int(c * square_size + square_size / 2), 
                height - int(r * square_size + square_size / 2) ), radius)

    pygame.display.update()

