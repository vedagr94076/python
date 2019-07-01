#4.  (2, 3, 4)
#5.  First and last name is prefered.
#6a.  'b', that is the value assigned to index 1.
#6b.  ('a', 'b')
#7a.  True
#7b.  10
#8.  Print all values of the list values exept for the first one
#9.  The first one reasigns the 4th value of the list, whereas the second one checks a conditional statement
#10a.  [a, b, 3, 4 ,5]
#10b.  [a, b, 3, 4, 5, 6, 7]
#11.  The error reads that int can not be added to a list
#12.  a = 18 since 6 * 3 = 18
from __future__ import print_function
import random

def roll_two_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a + b

#1.3.6 Function Test
print(roll_two_dice())

'''Conclusion'''
#1.  a[3] is a character in a string, b[3] can not be changed, c[3] is a value in a list
#2.  Using multiple string types open up many other oppertunities, and it simpifies code a lot
#3.  We have learned about functions, strings, tuples and lists, branching and output, and nested branching and input, and various other data types.