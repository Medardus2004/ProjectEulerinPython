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

def create_prime_list(max):
    sum = 0
    for i in range(2, max):
        if primzahlcheck(i):
            sum += i
    return sum


def solution():
    print("The sum of the primes below 10 is 2 + 3 +5 + 7 = 17.Find the sum of all the primes below N = two million??\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(create_prime_list(int(n)))
