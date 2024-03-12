#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = number % 10
if number >= 0:
    if res >= 6:
        print(f"Last digit of {number} is {res} and is greater than 5")
    elif (0 < res and res < 6):
        print(f"Last digit of {number} is {res} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {res} and is 0")
elif number < 0:
    n = number // 10
    print(f"Last digit of {number} is {number - 10*n} and is less than 6 and not 0")
