import math

def primzahlcheck(k):
    for x in range(3, math.isqrt(k) + 1):
        if k % x == 0:
            return False
    return True

    
def solution_task007(N):
    sum = 1
    x = 3
    while sum < int(N):
        if primzahlcheck(x):
            sum += 1
        x += 2
    return x - 2

def solution():
    print("By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13. What is the N = 10001st prime number??\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task007(n))
