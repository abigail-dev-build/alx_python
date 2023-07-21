#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

LAST_DIGIT = abs(number) % 10

if LAST_DIGIT > 5:
    print(f"Last digit of {number}, is {LAST_DIGIT} and is greater than 5")
elif 0 < LAST_DIGIT < 6  :
    print(f"Last digit of {number}, is {LAST_DIGIT} and is less than 6 and not 0")
else:
    print(f"Last digit of {number}, is {LAST_DIGIT} and is 0")