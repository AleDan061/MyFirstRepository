import random

print('hello there, a computer will choose a number from 1-9, try to guess the number!')
computer = random.randint(1,9)
player = input('enter a number between 1 and 9: ')
player = int(player)
if player > 9 or player < 1:
    print('invalid guess, try again')
if player == computer:
    print(f'You guessed right! the number was {computer}')
else:
    print(f'You're wrong, the number was {computer}')
attempt = input('Want to play again? (y/n)')
while attempt == 'y' or attempt == 'Y':
    print('hello there, a computer will choose a number from 1-9, try to guess the number!')
    computer = random.randint(1,9)
    player = input('enter a number between 1 and 9: ')
    player = int(player)
    if player > 9 or player < 1:
        print('invalid guess, try again')
    if player == computer:
        print(f'You guessed right! the number was {computer}')
    else:
        print(f'You're wrong, the number was {computer}')
