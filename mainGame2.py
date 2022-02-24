import numpy as np    
import pygame
import sys
import tkinter as ttk
import math
from player import *


ROW_COUNT = 6
COLUMN_COUNT = 7
square_size = 100 # in px - GUI
width = COLUMN_COUNT * square_size 
height = (ROW_COUNT+1) * square_size + 20
radius = int(square_size / 2 - 5) 

color_blue = (23,64,154) # rgb
color_black = (0, 0, 0)
color_white = (255,255,255)

size = (width, height)

pygame.font.init()
font = pygame.font.SysFont("Lexend Deca", 30) # font


# image processing
img1 = pygame.image.load("C:\\Users\\ayesh\\OneDrive\\Pictures\\nea\\p1.jpg")
img1 = pygame.transform.scale(img1, (30, 30))

img2 = pygame.image.load("C:\\Users\\ayesh\\OneDrive\\Pictures\\nea\\p2.jpg")
img2 = pygame.transform.scale(img2, (30, 30))


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

def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, color_blue, (c * square_size, r * square_size+square_size, square_size*4, square_size) )
            pygame.draw.circle(screen, color_black, (int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)), radius)




def play(board, player_one, player_two, print_game=True):

    game_over = False
    turn = 0 # player 1

    pygame.init() # initialize pygame

  
    # set title
    pygame.display.set_caption("Connect 4!")

    screen = pygame.display.set_mode(size)

    draw_board(board, screen)

    text_1 = font.render("Player 1", True, color_white)
    screen.blit(text_1, (10, 10))
    screen.blit(img1, (100, 5))

    text_2 = font.render("Player 2", True, color_white)
    screen.blit(text_2, (610, 10))
    screen.blit(img2, (570, 5))

    pygame.display.update() # update window


    if print_game:
        print_board(board)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

                # if turn == 0: # player 1 
                #     col = int(input("Player 1 Make your Selection (0-6): "))

                #     if is_valid_location(board, col):
                #         row = get_next_open_row(board, col)
                #         drop_piece(board, row, col, 1)

                #         if winning_move(board, 1):
                #             print("Player 1 Wins! Congrats!")
                #             game_over = True

                #     else:
                #         print("Space Taken! .. Enter again.")
                #         turn -= 1
                
                # else:
                #     col = int(input("Player 2 Make your Selection (0-6): "))

                #     if is_valid_location(board, col):
                #         row = get_next_open_row(board, col)
                #         drop_piece(board, row, col, 2)

                #         if winning_move(board, 2):
                #             print("Player 2 Wins! Congrats!")
                #             game_over = True
                    
                #     else:
                #         print("Space Taken! .. Enter again.")
                #         turn -= 1
                    

                        
                # print_board(board)
                
                # turn += 1
                # turn = turn % 2


if __name__ == '__main__':
    board = create_board()
    player_1 = RandomPlayer(1)
    player_2 = RandomPlayer(2)
    play(board, player_1, player_2, print_game=True)
