import math

def primzahlcheck(k):
    if k == 2:
        return True
    if k%2 == 0:
        return False
    for x in range(3, math.isqrt(k) + 1):
        if k % x == 0:
            return False
    return True


def solution_task003(N):
    prime_factors = []
    for x in range(2, int(math.sqrt(int(N)))):
        if int(N)%x == 0 and primzahlcheck(x):
            prime_factors.append(x)
    return prime_factors

def solution():
    print("The prime factors of 13195 are 5, 7, 13, 29. What is the largest prime factor of the number N = 600851475143?\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task003(n))
