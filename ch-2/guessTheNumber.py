# Thsi is a guess the number game.

import random

secretNumber = random.randint(1,6)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess number 6 times.
for guessTaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! you guessed the right number in ' + str(guessTaken) +
' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')