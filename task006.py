import math

def sum_of_squares(k):
    sum = 0
    for x in range(1, int(k)+1):
        sum += x**2
    return sum

def square_of_sum(k):
    sum = 0
    for x in range(1, int(k)+1):
        sum += x
    return sum**2

def solution():
    print("The sum of the squares of the first ten natural numbers is 385. The square of the sum of the first ten natural numbers is 3025, Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.Find the difference between the sum of the squares of the first N = one hundred natural numbers and the square of the sum.\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(square_of_sum(n) - sum_of_squares(n))
