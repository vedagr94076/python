from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def days():
    ''' Tells the date and day
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('picks')
    
def roll_hundred_pair():
    individual_rolls = []
    for roll in range(100):
        individual_rolls += [random.randint(1, 6)]
    
    plt.hist(individual_rolls)
    plt.savefig('1.3.7/100_rolls_hist')

def dice(n):
    dice_rolls = [random.randint(1, 6)] * n
    total = 0
    for roll in dice_rolls:
        total += roll
    print(total)
    
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # Dice roll game
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: 
        '''This will cycle through all of the values in players'''
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Sets number of guesses to 1, and prints the winning print statement.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

def goguess():
    secret = random.randint(1, 20)
    print('I have a number one through 20.')
    guess = int(raw_input('Guess:  '))
    while True:
        if guess > secret:
            print(guess, 'is too high')
            guess = raw_input('Guess:')
        elif guess < secret:
            print(guess, 'is too low')
            guess = raw_input('Guess')
        else:
            print('Right! My number is 9! You guessed in 3 guesses!')
            break

#1.3.7 Assingment Check
print(roll_hundred_pair())
print(dice(5))
goguess()

'''Answers'''
#7.  So the while loop is entered.
#10.  You will need 378.