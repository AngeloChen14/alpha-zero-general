import Arena
from MCTS import MCTS
from pickgame.PickGame import PickGame
from pickgame.keras.NNet import NNetWrapper as NNet
from pickgame.PickGamePlayers import *
import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""
#choose player, both set to Flase -> cpu vs cpu 
human_vs_cpu = True
random_vs_cpu = False

#choose number of games to play
num_to_play = 2     

#choose size of board, must be same as model loaded below
g = PickGame(4)

# all players
rp = RandomPlayer(g).play
hp = HumanPickGamePlayer(g).play

# nnet players
n1 = NNet(g)
n1.load_checkpoint('./pretrained_models/pickgame/keras','4x4-best.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

if human_vs_cpu:
    player2 = hp
else:
    if random_vs_cpu:
        player2 = rp
    else:
        n2 = NNet(g)
        n2.load_checkpoint('./temp', 'best.pth.tar')
        args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
        mcts2 = MCTS(g, n2, args2)
        n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))
        player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=PickGame.display)

print(arena.playGames(num_to_play, verbose=True))
