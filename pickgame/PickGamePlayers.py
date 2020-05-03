import numpy as np

"""
Random and Human-ineracting players for the game of PickGame.

Author: Angelo CHen, github.com/AngeloChen14
Date: May 1, 2020.

Based on the OthelloPlayers by Surag Nair.

"""
class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a


class HumanPickGamePlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        # display(board)
        valid = self.game.getValidMoves(board, 1)
        # for i in range(len(valid)):
        #     if valid[i]:
        #         print(int(i/self.game.n), int(i%self.game.n))
        while True: 
            input_move = input()
            a = input_move.split(" ")
            if len(a) == 4:
                try:
                    x1,y1,x2,y2 = [int(x) for x in a]
                    x1-=1;y1-=1;x2-=1;y2-=1
                    if (0 <= x1) and (x1 < self.game.n) and (0 <= y1) and (y1 < self.game.n) and \
                         (0 <= x2) and (x2 < self.game.n) and (0 <= y2) and (y2 < self.game.n) and (x1==x2 or y1==y2):
                        if(x1==x2 and y1==y2):
                            a=(self.game.n*x1+y1)   
                        else:
                            if y1!=y2:
                                a=int(self.game.n*self.game.n+self.game.n*(self.game.n-1)*x1/2+(2*self.game.n-y1-1)*y1/2+y2-y1-1)
                            if x1!=x2:
                                a=int(self.game.n*self.game.n*(self.game.n+1)/2+self.game.n*(self.game.n-1)*y1/2+(2*self.game.n-x1-1)*x1/2+x2-x1-1)
                        if valid[a]:
                            break
                except ValueError:
                    # Input needs to be an integer
                    'Invalid integer'
            print('Invalid move')
        return a
