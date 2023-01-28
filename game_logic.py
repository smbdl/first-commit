from decouple import config
import random

my_money = config('MY_MONEY', cast=int)

while True:
    stop_or_no = input('Do wou want to continue? yes/no ')
    if stop_or_no == 'no'.lower():
        break
    my_money = config('MY_MONEY', cast=int)
    lucky_number = random.choice(range(1, 31))
    bet = int(input('Money to bet: '))
    win_or_loose = int(input('Choose a number 1-30: '))
    if win_or_loose == lucky_number:
        my_money += bet * 2
        print(f'You gained {bet * 2}$, congratulations!')
    elif win_or_loose != lucky_number:
        my_money -= bet
        print(f'You lost {bet}$, lucky number was {lucky_number}.')