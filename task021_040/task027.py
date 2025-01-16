from argparse import ArgumentParser
import math

def primzahlcheck(k):
    if k == 2:
        return True
    if k%2 == 0 or k  < 0 :
        return False
    for x in range(3, math.isqrt(k) + 1):
        if k % x == 0:
            return False
    return True

def quadratic(n, a, b) :
    return n**2 + a*n + b

def maximum_number_primes(a, b):
    n = 0
    while primzahlcheck(quadratic(n, a, b)):
        n += 1
    return n

def largest_coefficients(max_a, max_b) :
    maximum = 0 
    largest_a = 0
    largest_b = 0
    for a in range(-max_a, max_a) :
        for b in range(-max_b, max_b) :
            if maximum_number_primes(a, b) > maximum :
                maximum = maximum_number_primes(a, b)
                largest_a = a
                largest_b = b
    return largest_a * largest_b

def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "-a", "--linear", help="find for < a ")
    parser.add_argument( "-b", "--coefficient", help="find for < b")
    args = parser.parse_args()
    print(largest_coefficients(int(args.linear), int(args.coefficient)) )


if __name__ == "__main__":
    main() 