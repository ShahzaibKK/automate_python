import sys


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(number * 3 + 1)
        return 3 * number + 1


try:
    num = input("type your number: ")
    while num != 1:
        num = collatz(int(num))
except ValueError:
    print("please enter only integer! ")
