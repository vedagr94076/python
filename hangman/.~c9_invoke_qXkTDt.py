from __future__ import print_function
import random

def hangman_display(guessed, secret_word):
    ''' 
    This function returns a string that the player will see. 
    The arguments are guessed, which shows the letter guessed so far, 
    and secret, which is the secret hangman phrase. If the guessed letter is in 
    secret, the function adds the letter to display. If the guessed letter is 
    not in secret, it adds an underscore to the display. Since a space was 
    added to guessed, even if the player guesses a space, it will show up as
    a space.
    '''
    display = ""
    guessed += " "
    for letter in secret_word:
        if letter in guessed:
            display += letter
        elif letter not in guessed:
            display += "_"
    return display

words = ['BATMAN', 'THE FLASH', 'WOLVERINE', 'SPIDERMAN', 'THANOS','SUPERMAN',
        'LOKI','THE HULK','THE JOKER']

def hangman():
    '''
    This function says what the secret word is, then prints the secret word. 
    Then it asks for a guess, and it lets the user input upper or lowercase
    letters. It makes guessed and guess the same, then defines replay, which 
    lets you replay the game after you finished. The secret_word is the secret
    word which the player tries to guess. The guess_num the number of guesses.
    If you do not enter the secret word correctly in 10 guesses or under, 
    it prints you lost and breaks the loop. If you guess the secret word 
    correctly, it prints congratulations, you won! and breaks the loop. It also
    prints how many guesses you have left after each guess, and is already 
    guessed and lets you guess again.
    '''
    print('Theme: Marvel + DC Characters')
    global cheat
    global replay
    global secret_word
    secret_word = words[random.randint(0, 8)]
    print (secret_word)
    guess = ''
    guess_num = 0
    guessed = guess + '   '
    replay = ''
    cheat = ''
    while guess_num <= 10:
        if guess_num == 10:
            if hangman_display(guessed, secret_word) != secret_word:
                print('You lost!')
                print('The secret word was', secret_word)
                replay = raw_input('Would you like to play again?  ').lower()
                break
        elif hangman_display(guessed, secret_word) == secret_word:
            print(hangman_display(guessed, secret_word))
            print('Congratulations, you won!!!')
            replay = raw_input('Would you like to play again?  ').lower()
            break
        else:
            print('You have', 10 - guess_num, 'guesses left.')
            guess_num += 1
            print('Already guessed: ', guessed)
            print(hangman_display(guessed, secret_word))
            guess = raw_input('Guess:  ').upper()
            if len(guess) > 1:
                cheat = 'yes'
                break
            guessed += guess + '   '
            
h

if cheat == 'yes':
    print('Cheater!  You lose!  You don\'t even get to try again (or know the secret word).')
elif replay == 'yes':
    while replay == 'yes':
        hangman()
else:
    print('OK')