def safe_print_division(a, b):
    try:
        divide = a / b
    except ZeroDivisionError:
        divide = None
    finally:
        print("Inside result: {}".format(divide))
        return divide

# Test cases
if __name__ == "__main__":
    a = 12
    b = 2
    divide = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, divide))

    a = 12
    b = 0
    divide = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, divide))
