import math
import numpy as np

class Player:
    def __init__(self, turn):
        self.turn = turn
    
    def get_move(self):
        pass

class Player1(Player): #inherit
    def __init__(self, turn):
        super().__init__(turn)
    
    def get_move(self):
        pass
    
    def delete_this_function(self): # delete this file
        pass
