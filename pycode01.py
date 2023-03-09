#!/usr/bin/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(res))
    return res


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
