#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print('last digit of', number, 'is', lastdigit, 'and is greater than 5')
elif lastdigit == 0:
    print('last digit of', number, 'is', lastdigit)
else:
    print('last digit of', number, 'is', lastdigit, 'and \
     is less than 6 and not 0')
