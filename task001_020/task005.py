import math

def primzahlcheck(k):
    if k == 2:
        return True
    if k%2 == 0:
        return False
    for x in range(3, k):
        if k % x == 0:
            return False
    return True

def amountinsum(j, N):
    exponent = 1
    while int(j)**exponent < int(N):
        exponent += 1
    return exponent-1
    
def solution_task005(N):
    sum = 1

    for x in range(2, int(N)+1):
        if primzahlcheck(x):
            sum *= x**amountinsum(x,N)
    return sum

def solution():
    print("2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to N =  20?\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task005(n))
