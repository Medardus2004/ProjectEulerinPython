import math

def cross_sum_factorial(N):
    cross_sum = 0
    factorial = str(math.factorial(100))
    for number in factorial:
        cross_sum += int(number)
    return cross_sum


def solution():
    print("Find the sum of the digits in the number n = 100!.\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(cross_sum_factorial(n))