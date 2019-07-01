from __future__ import print_function
import random

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

def f(x):
    '''Classifies numbers'''
    if int(x)==x:
        if x%2==0:
            if x%3==0:
                return "%s is a multiple of 6" %(str(x))
            else:
                return "%s is even" %(str(x))
        else:
            return "%s is odd" %(str(x))
    else:
        return "%s is not an integer" %(str(x))

def f_test():
    ''' Unit test for f(x)
    returns True if good, returns False and prints error if not 
    good
    '''
    works = ""
    if f(.1) != "0.1 is not an integer":
        works = ".1 doesn't work"
    elif f(1) != "1 is odd":
        works = "1 doesn't work"
    elif f(2) != "2 is even":
        works = "2 doesn't work"
    elif f(3) != "3 is odd":
        works = "3 doesn't work"
    elif f(6) != "6 is a multiple of 6":
        works = "6 doesn't work"
    else:
        works = "All good"
    print (works)

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess < secret:
            print("Too low - my number was", secret, end="\n")
        elif guess > secret:
            print("Too high, my number was", secret, end="\n")
    else:
        print('Right on, I had the number', guess, end='!\n')

def quiz_decimal(low, high):
    answer = float(raw_input("Type a number between %s and %s:  " %(low, high)))
    if answer < low:
        print("No, ", answer, " is less than ", low)
    elif answer > high:
        print("No, ", answer, " is greater than ", high)
    else:
        print("Good!", low, " < ", answer, " < ", high)

def g(x):
    '''Classifies numbers'''
    if int(x)==x:
        return "%s is an integer" %(str(x))
    else:
        return "%s is not an integer" %(str(x))

def h(x):
    '''Classifies numbers'''
    if x%2==0:
        return "%s is even" %(str(x))
    else:
        return "%s is odd" %(str(x))


def i(x):
    '''Classifies numbers'''
    if x%6==0:
        return "%s is a multiple of 6" %(str(x))
    else:
        return "%s is not a multiple of six" %(str(x))

def f_challenge(n):
    print (g(n))
    print (h(n))
    print (i(n))

#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

'''Part 1'''
#1.
#   a.  Line 17
#   b.  
#       i.  orange
#       ii.  apple, banana
#       iii.  potato
#       iv.  none
#   c.  The bananas will be computed as if-else statements first
#4. Teat one of each type of number.
#7. As a concatenation, + conects two string, simply "gluing" them together.  As numeric addition, + adds the two values.
#9a.  The end argument of the print function sets the end of the print funtion.  In the examle above, the end is set to an exclamaion mark and the a new
#     line.
"""Conclusion"""
#1. Both test a bit of software.
#2. None might be executed, or all might be executed, it depends on the input.
#3. A test suite tests a program to see if it works.  Test suites might be coded first to remind the programmer of the end goals or to be easy to access while writing the code.
