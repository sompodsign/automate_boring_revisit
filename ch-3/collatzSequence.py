
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)

userInput = 0

try:
    userInput = int(input('Enter a number: '))
    collatz(userInput)
except ValueError:
    print('please enter an integer')















