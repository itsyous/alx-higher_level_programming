#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number % 10)
if number < 0:
    n = -(n)
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
elif n < 6:
    print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
