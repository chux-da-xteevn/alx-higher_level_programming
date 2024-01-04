#!/usr/bin/python3
num = 0
while num <= 90:
    if num % 10 == 0:
        num += 1 + num // 10
        print("{:02d}".format(num), end='\n' if num == 90 else ", ")
        num += 1
