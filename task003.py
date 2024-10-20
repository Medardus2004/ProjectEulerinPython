import math

#def fermat_test(n, k):
#    if n == 2:
#        return True
#    if n%2 == 0:
#        return False
#    if n == 0 or n == 1:
#        return False
#    for _ in range(k):
#        a = random.randint(1, n-1)
#        if pow(a, n-1) % n != 1:
#            return False
#        return True

def primzahlcheck(k):
    if k == 2:
        return True
    if k%2 == 0:
        return False
    for x in range(3, k):
        if k % x == 0:
            return False
    return True

#def primfaktoren(N):
#    sum = 0
#    list = []
#    for x in range(2, int(math.sqrt(int(N)))):
#        if primzahlcheck(x):
#            list.append(x)
#    print(list)
#    return list

def solution_task003(N):
    prime_factors = []
    for x in range(2, int(math.sqrt(int(N)))):
        if int(N)%x == 0 and primzahlcheck(x):
            prime_factors.append(x)
    return prime_factors

def task003_output():
    print("The prime factors of 13195 are 5, 7, 13, 29. What is the largest prime factor of the number N = 600851475143?\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task003(n))
