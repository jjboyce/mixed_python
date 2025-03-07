import random
from unittest import removeResult


def flip_coin():
    coin_results = ['Heads', 'Tails']
    confirmed_result = random.choice(coin_results)
    return confirmed_result

def main():

    player = 'Jack'

    flip1 = flip_coin()

    print(player1, 'flipped a ', flip1)

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
        return result

result = []
play_count = int(0)
player1wins = int(0)
player2wins = int(0)
draws = int(0)

while play_count < 1000000:# and draws <1:
    play_count = play_count+1
    result = main()

    if result == 'player1win':
        player1wins = player1wins+1
    elif result == 'player2win':
        player2wins = player2wins+1
    else:
        draws = draws+1

print('***********************************************************************')
print('\nSTATISTICS:\n')
print(f'\nThe total number of plays completed is {play_count}')

player1_pc = (player1wins / play_count)  * 100
player2_pc = (player2wins / play_count)  * 100
draws_pc = (draws / play_count)  * 100

print(f'Player 1 has won {player1wins} times! ({player1_pc}%)')
print(f'Player 2 has won {player2wins} times! ({player2_pc}%)')
print(f'There have been {draws} draws ({draws_pc}%)')
