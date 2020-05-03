# PickGame implementation for Alpha Zero General

An implementation of a simple game provided to check extendability of the framework. Neural network architecture was copy-pasted from the game of Othello, so possibly it can be simplified. 

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
To start a tournament of 100 episodes with the model-based player against a random player:
```bash
python pit.py
```
You can play againt the model by switching to HumanPlayer in ```pit.py```

### Experiments
I trained a Keras model for 4x4 PickGame (50 iterations, 100 episodes, 10 epochs per iteration and 50 MCTS simulations per turn). This took about 30 minutes on an i5-8250U with MX150 CUDA. The pretrained model (Keras) can be found in ```pretrained_models/pickgame/keras/```. You can play a game against it using ```pit.py```. 

### Contributors and Credits
* [Angelo Chen](https://github.com/AngeloChen14)

The implementation is based on the game of Othello (https://github.com/suragnair/alpha-zero-general/tree/master/othello).

### AlphaGo / AlphaZero Talks
* February 8, 2018 - [Advanced Spark/Tensorflow Meetup at Thumbtack](https://www.meetup.com/Advanced-Spark-and-TensorFlow-Meetup/events/245308722/): [Youtube](https://youtu.be/dhmBrTouCKk?t=1017) / [Slides](http://static.brettkoonce.com/presentations/go_v1.pdf)
* March 6, 2018 - [Advanced Spark/Tensorflow Meetup at Strata San Jose](https://www.meetup.com/Advanced-Spark-and-TensorFlow-Meetup/events/246530339/): [Youtube](https://www.youtube.com/watch?time_continue=1257&v=hw9VccUyXdY) / [Slides](http://static.brettkoonce.com/presentations/go.pdf)
