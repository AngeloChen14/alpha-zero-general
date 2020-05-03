# PickGame implementation for Alpha Zero General

An implementation of a simple game provided to check extendability of the framework. Neural network architecture was copy-pasted from the game of Othello, so possibly it can be simplified. 

```Coach.py``` contains the core training loop and ```MCTS.py``` performs the Monte Carlo Tree Search. The parameters for the self-play can be specified in ```main.py```. Additional neural network parameters are in ```pickgame/keras/NNet.py``` (cuda flag, batch size, epochs, learning rate etc.). 


To train a model for PickGame, change the imports in ```main.py``` to (already changed):
```python
from Coach import Coach
from pickgame.PickGame import PickGame
from pickgame.keras.NNet import NNetWrapper as nn
from utils import *
 ```

and the first line of ```__main__``` to
```python
g = PickeGame(n)
```
 Make similar changes to ```pit.py```.

To start training a model for PickGame:
```bash
python main.py
```

To play againt the model-based player:
```bash
python pit.py
```

You can choose players of the game (human / random / model) by switching flags in ```pit.py```
### Environment Requirement
Python3, NumPy, Keras Library, CUDA Toolkit (optional)
### Experiments
I trained a Keras model for 4x4 PickGame (50 iterations, 100 episodes, 10 epochs per iteration and 50 MCTS simulations per turn). This took about 30 minutes on an i5-8250U with MX150 CUDA. The pretrained model (Keras) can be found in ```pretrained_models/pickgame/keras/```. You can play a game against it using ```pit.py```. 

### Contributors and Credits
* [Angelo Chen](https://github.com/AngeloChen14)

The implementation is based on this [project](https://github.com/suragnair/alpha-zero-general/).

A concise description of this algorithm can be found [here](https://github.com/suragnair/alpha-zero-general/raw/master/pretrained_models/writeup.pdf).
