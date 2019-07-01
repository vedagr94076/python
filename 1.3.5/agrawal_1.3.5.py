from __future__ import print_function

def how_eligible(essay):
    score = 0
    if "?" in essay:
        score += 1
    if "\"" in essay:
        score += 1
    if "," in essay:
        score += 1
    if "!" in essay:
        score += 1
    return score

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

"""Answers"""
#5.  int or float.
#6.  The second one will produce an error scine a str and an int are being concatinated.
#7.  The seventh to last letter.
#8.  All the characters form indices 5-20, including 20.
#10a.  6, 7 characters minus 1.
#10b.  all the letters other than the last one will be printed.
#11.  "test goo" is part of the string it is being checked in, so the statement returns true.
#12.  I got the expected result from my function test, so i believe that I have successfully completed the assignment.