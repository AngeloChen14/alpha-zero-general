'''
Board class for the game of PickGame.
Default board size is 3x3.
Board data:
  0=empty(棋子被取走), 1=occupied(棋子未被取走))
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Angelo Chen, github.com/AngeloChen14
Date: May 1, 2020.

Based on the board for the game of Othello by Eric P. Nichols.

'''
import numpy as np
# from bkcharts.attributes import color
class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [1]*self.n

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty squares (color==0)
        for y in range(self.n):
            for x in range(self.n):
                if self[x][y]==1:
                    newmove = (x,y,x,y)
                    moves.add(newmove)
                    if self.n-x>1:
                        for z in range(1,self.n-x):
                            if self[x+z][y]==1:
                                newmove = (x,y,x+z,y)
                                moves.add(newmove)
                            else:
                                break
                    if self.n-y>1:
                        for z in range(1,self.n-y):
                            if self[x][y+z]==1:
                                newmove = (x,y,x,y+z)
                                moves.add(newmove)
                            else:
                                break                       
        return list(moves)

    def has_legal_moves(self): 
        if np.sum(self.pieces) > 1:
            return True
        return False
    
    def execute_move(self, move, color):
        """Perform the given move on the board; 
        """

        (x1,y1,x2,y2) = move

        assert self[x1][y1] == 1 and self[x2][y2] == 1
        assert x1==x2 or y1==y2
        self[x1][y1] = 0
        if x1!=x2:
            for z in range(x2-x1):
                self[x1+z+1][y1]=0
        if y1!=y2:
            for z in range(y2-y1):
                self[x1][y1+z+1]=0

