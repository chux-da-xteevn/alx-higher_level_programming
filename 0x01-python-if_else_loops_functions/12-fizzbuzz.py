#!/usr/bin/python3
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz ", end="")
    elif number % 5 == 0:
        print("Buzz ", end="")
    elif number % 3 == 0:
        print("Buzz ", end="")
    else:
        print(f"{number} ", end="")
