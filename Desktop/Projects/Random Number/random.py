import random as rd
import numpy as np
from time import sleep


def throw_dice(dice_num,dice):
    num = rd.choice(dice_num)
    dice[0] = num
    return(dice)
    
board = [0]
dice = np.array(board)
dice = dice.reshape(1)

dice_num = [1,2,3,4,5,6]


roll = str(input('Press Y for rolling a dice or press N to exit\n'))
while roll == 'Y' or roll == 'y':
    print(throw_dice(dice_num,dice))
    print('\n\n')
    sleep(0.3)
    roll = str(input('Press Y for rolling a dice or press N to exit\n'))

if roll == 'N' or roll =='n':
          exit(0)
