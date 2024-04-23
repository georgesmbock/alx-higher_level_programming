#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "and is less than 6 and not 0"
res = number % 10
if number >= 0:
    if res >= 6:
        print(f"{str1} {number} is {res} and is greater than 5")
    elif (0 < res and res < 6):
        print(f"{str1} {number} is {res} {str2}")
    else:
        print(f"{str1} {number} is {res} and is 0")
elif number < 0:
    n = int(number / 10) # partie entière d'un entien négatif
    print(f"{str1} {number} is {number - 10*n} {str2}")
