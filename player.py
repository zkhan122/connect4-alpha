import math
import numpy as np
from base import *

class Player:
    def __init__(self, turn):
        self.turn = turn
    
    def get_move(self):
        pass

class RandomPlayer(Player): # inherit    
    def __init__(self, turn):
        super().__init__(turn)
    
    def get_move(self, game, col):
        valid_move = False
        val = None
        while not valid_move:
            move = input(self.turn + '\'s turn. Input move from (0-6: ')
            try:
                val = int(move)
                if val is not is_valid_location(self, col):
                    raise ValueError
            except ValueError:
                print("Invalid move. Please try again")
        return val
