from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .PickGameLogic import Board
import numpy as np

"""
Game class implementation for the game of PickGame.
Based on the OthelloGame then getGameEnded() was adapted to new rules.

Author: Angelo Chen, github.com/AngeloChen14
Date: May 1, 2020.

Based on the OthelloGame by Surag Nair.
"""
class PickGame(Game):
    def __init__(self, n):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n)

    def getActionSize(self):
        # return number of actions
        return self.n*self.n*self.n + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n*self.n*self.n + 1:
            return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        #从action到move的反编码，很麻烦
        if action<self.n*self.n:
            move = (int(action/self.n), int(action%self.n),int(action/self.n), int(action%self.n))
        else:
            if(action<self.n*self.n*(self.n+1)/2):
                x1=int((action-self.n*self.n)/((self.n*self.n-self.n)/2))
                x2=x1
                res=(action-self.n*self.n)%((self.n*(self.n-1))/2)
                for i in range(self.n):
                    if res<(2*self.n-i-2)*(i+1)/2:
                        y1=i
                        y2=self.n+res-(2*self.n-i-2)*(i+1)/2
                        move=(int(x1),int(y1),int(x2),int(y2))
                        break
            else:
                y1=int((action-self.n*self.n*(self.n+1)/2)/((self.n*self.n-self.n)/2))
                y2=y1
                res=(action-self.n*self.n*(self.n+1)/2)%((self.n*(self.n-1))/2)
                for i in range(self.n):
                    if res<(2*self.n-i-2)*(i+1)/2:
                        x1=i
                        x2=self.n+res-(2*self.n-i-2)*(i+1)/2
                        move=(int(x1),int(y1),int(x2),int(y2))
                        break
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for x1,y1,x2,y2 in legalMoves:
            if(x1==x2 and y1==y2):
                valids[self.n*x1+y1]=1    
            else:
                if y1!=y2:
                    valids[int(self.n*self.n+self.n*(self.n-1)*x1/2+(2*self.n-y1-1)*y1/2+y2-y1-1)]=1
                if x1!=x2:
                    valids[int(self.n*self.n*(self.n+1)/2+self.n*(self.n-1)*y1/2+(2*self.n-x1-1)*x1/2+x2-x1-1)]=1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)

        if b.has_legal_moves():
            return 0
        else:
            assert(np.sum(b.pieces)==1 or np.sum(b.pieces)==0) 
            if np.sum(b.pieces)==1:
                return -1 #仅剩一子 当前玩家为输家
            return 1   #棋盘无子 当前玩家为赢家

        # draw has a very little value 
        return 1e-4

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return board

    def getSymmetries(self, board, pi):
        # return mirror, rotational board and pi
        assert(len(pi) == self.n**3+1)  # 1 for pass
        n=self.n
        pi_board = np.reshape(pi[:n**2], (n, n)) #前n^2项映射到棋盘跟着转即可
        pi_row=np.reshape(pi[n**2:int(n**2*(n+1)/2)],(n,int(n*(n-1)/2))) #行和列需要根据编码规则特殊处理
        pi_column=np.reshape(pi[int(n**2*(n+1)/2):n**3],(n,int(n*(n-1)/2)))
        pi_row_flip=np.copy(pi_row)
        pi_column_flip=np.copy(pi_column)
        l = []

        for i in range(1, 5):
            newB = np.rot90(board, i)
            newPi_board = np.rot90(pi_board, i)
            pi_row_old=np.copy(pi_row)
            for k in range(n):                   
                pi_row[k,:]=pi_column[n-k-1,:]
            for x in range(n):
                for y in range(n):
                    if x<y:
                        pi_column[:,int(n*x-x*(x+3)/2+y-1)]=pi_row_old[:,int(n*(n-y-1)-(n-y-1)*(n-y+2)/2+n-x-2)]
            for j in [True, False]:               
                if j:
                    newB_flip = np.fliplr(newB)
                    newPi_board_flip = np.fliplr(newPi_board)
                    pi_column_old=np.copy(pi_column)
                    pi_row_old=np.copy(pi_row)
                    for k in range(n):                   
                        pi_column_flip[k,:]=pi_column_old[n-k-1,:]
                    for x in range(n):
                        for y in range(n):
                            if x<y:
                                pi_row_flip[:,int(n*x-x*(x+3)/2+y-1)]=pi_row_old[:,int(n*(n-y-1)-(n-y-1)*(n-y+2)/2+n-x-2)]
                    l += [(newB_flip, list(newPi_board_flip.ravel())+list(pi_row_flip.ravel())+list(pi_column_flip.ravel()) + [pi[-1]])]
                else:
                    l += [(newB, list(newPi_board.ravel())+list(pi_row.ravel())+list(pi_column.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    @staticmethod
    def display(board,action):
        n = board.shape[0]

        print(" y ", end="")
        for y in range(n):
            print (y+1,"", end="")  # print the column #
        print("")
        print("x ", end="")
        for _ in range(n):
            print ("-", end="-")
        print("--")
        for y in range(n):
            print(y+1, "|",end="")    # print the row #
            for x in range(n):
                piece = board[y][x]    # get the piece to print,0表示无棋子，显示0
                if piece == 1: print("1 ",end="")
                elif piece == 0: print("0 ",end="")
                else:
                    if x==n:
                        print("-",end="")
                    else:
                        print("- ",end="")
            print("|")

        print("  ", end="")
        for _ in range(n):
            print ("-", end="-")
        print("--")

        if action<n*n:
            move = (int(action/n+1), int(action%n+1),int(action/n+1), int(action%n+1))
        else:
            if(action<n*n*(n+1)/2):
                x1=int((action-n*n)/((n*n-n)/2))
                x2=x1
                res=(action-n*n)%((n*(n-1))/2)
                for i in range(n):
                    if res<(2*n-i-2)*(i+1)/2:
                        y1=i
                        y2=n+res-(2*n-i-2)*(i+1)/2
                        move=(int(x1+1),int(y1+1),int(x2+1),int(y2+1))
                        break
            else:
                y1=int((action-n*n*(n+1)/2)/((n*n-n)/2))
                y2=y1
                res=(action-n*n*(n+1)/2)%((n*(n-1))/2)
                for i in range(n):
                    if res<(2*n-i-2)*(i+1)/2:
                        x1=i
                        x2=n+res-(2*n-i-2)*(i+1)/2
                        move=(int(x1+1),int(y1+1),int(x2+1),int(y2+1))
                        break
        if action >=0: #取消首局输出
            print("Last move:",move)
