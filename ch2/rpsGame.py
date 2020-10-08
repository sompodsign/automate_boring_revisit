import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True: #the player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what player chose:

    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    #Display what computer choose;
    randonNumber = random.randint(1,3)
    if randonNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randonNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randonNumber == 3:
        computerMove = 's'
        print('Scissors')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you loose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        losses += 1


    

