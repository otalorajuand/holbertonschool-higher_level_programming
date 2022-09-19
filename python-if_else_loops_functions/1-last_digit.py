#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is 0"
str4 = "and is less than 6 and not 0"

if number < 0:
    last_digit = -1 * ((-1 * number) % 10)
else:
    last_digit = number % 10

if last_digit > 5:
    print(str1 + f" {number} is {last_digit} " + str2)
elif last_digit == 0:
    print(str1 + f" {number} is {last_digit} " + str3)
elif last_digit < 6 and last_digit != 0:
    print(str1 + f" {number} is {last_digit} " + str4)
