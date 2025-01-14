import math

def cross_sum_of_square(N):
    square = str(2**N)
    crosssum = 0
    for number in square:
        crosssum += int(number)
    return crosssum



def solution():
    print("2 hoch 15 = 32786 and the sum of its digits is 26. What is the sum of the digits of the number 2 hoch N = 1000?\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(cross_sum_of_square(int(n)))
