import random
from unittest import removeResult

draw_count = int(0)
win_count = int(0)



def draw_number():
    ball_number = int(0)
    balls_drawn = int(0)
    successful_draw = []
    ball_number = random.randint(1, 59)
    while ball_number not in drawn_numbers and balls_drawn > 0:
        balls_drawn = balls_drawn+1
        successful_draw = True
        return ball_number



def regular_numbers():
    pick1 = int(22)
    pick2 = int(23)
    pick3 = int(7)
    pick4 = int(13)
    pick5 = int(1)
    pick6 = int(59)

    my_regular_numbers = [pick1, pick2, pick3, pick4, pick5, pick6]

    return my_regular_numbers


def draw():
    draw1 = []
    draw2 = []
    draw3 = []
    draw4 = []
    draw5 = []
    draw6 = []

    draw1 = draw_number()
    draw2 = draw_number()
    draw3 = draw_number()
    draw4 = draw_number()
    draw5 = draw_number()
    draw6 = draw_number()

    drawn_numbers = [draw1, draw2, draw3, draw4, draw5, draw6]

    return drawn_numbers

while draw_count <1000 and win_count <1:
    draw_count = draw_count+1
    my_regular_numbers = regular_numbers()
    drawn_numbers = draw()
    print(f'Number of Draws: {draw_count}')

    numbers_match = all(num in my_regular_numbers for num in drawn_numbers)

    if numbers_match:
        win_count = win_count+1
        print("numbers matched!\n")
        print(f'Your Numbers: {my_regular_numbers}')
        print(f'This weeks Numbers: {drawn_numbers}')


print(f' Number of Wins: {win_count}')




