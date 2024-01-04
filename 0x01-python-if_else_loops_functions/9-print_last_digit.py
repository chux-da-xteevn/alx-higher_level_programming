#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        lastDigit = num % 10
    else:
        lastDigit = num % -10
        lastDigit *= -1

    print("{:d}".format(lastDigit), end='')
    return (lastDigit)
