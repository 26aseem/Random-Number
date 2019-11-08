import random as rd
import numpy as np
from time import sleep


def toss_coin(coin_num,coin):
    num = rd.choice(coin_num)
    coin[0] = num
    return(coin)
    
board = [0]
coin = np.array(board)
coin = coin.reshape(1)

coin_num = [1,2]


toss = str(input('Press Y for tossing a coin or press N to exit\n'))
while toss == 'Y' or toss == 'y':
    print(toss_coin(coin_num,coin))
    print('\n\n')
    sleep(0.3)
    toss = str(input('Press Y for tossing a coin or press N to exit\n'))

if toss == 'N' or toss =='n':
          exit(0)
