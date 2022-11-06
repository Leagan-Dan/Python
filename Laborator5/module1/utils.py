from math import sqrt


def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1, 1):
        if x % i == 0:
            return False
    return True


def process_item(x):
    number = x + 1
    found = False
    while not found:
        if is_prime(number):
            return number
        number += 1
    return False


def exercitiul1a():
    print("input exercitiul1a:")
    number = input()
    number = int(number)
    print(process_item(number))
