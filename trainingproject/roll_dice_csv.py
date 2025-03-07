import os
import webbrowser
import random
from unittest import removeResult
import csv
import pandas
import sys


def roll_dice():
    dice_total = random.randint(1,6)
    return dice_total

def main():

    player1 = 'Jack'
    player2 = 'James'

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        result = 'player1win'
        print(player1, 'wins!')
        return result
    elif roll2 > roll1:
        result = 'player2win'
        print(player2, 'wins!')
        return result
    else:
        result = 'tied'
        print('Draw!')
        return result

result = []
play_count = int(0)
player1wins = int(0)
player2wins = int(0)
draws = int(0)


play_count_input = int(input("How many games would you like to simulate?   \n"))

while play_count < play_count_input: #and draws <1:
    play_count = play_count+1
    result = main()

    if result == 'player1win':
        player1wins = player1wins+1
    elif result == 'player2win':
        player2wins = player2wins+1
    else:
        draws = draws+1

print('***********************************************************************')
print('\nRESULTS:\n')
print(f'\nThe total number of plays completed is {play_count}')

player1_pc = (player1wins / play_count)  * 100
player2_pc = (player2wins / play_count)  * 100
draws_pc = (draws / play_count)  * 100

print(f'Jack has won {player1wins} times! ({player1_pc}%)')
print(f'James has won {player2wins} times! ({player2_pc}%)')
print(f'There have been {draws} draws ({draws_pc}%)')
