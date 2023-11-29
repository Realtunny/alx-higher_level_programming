#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit =str(number)
last_string = int(last_digit[-1])
if last_string > 5:
    print(f"Last digit of {last_digit} is {last_string} and is greater than 5")
elif last_string < 6 and last_string != 0:
    print(f"Last digit of {last_digit} is {last_string} and is less than 6 and not 0")
elif last_string == 0:
    print(f"Last digit of {last_digit} is {last_string} and is zero")
