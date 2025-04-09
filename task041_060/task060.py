from argparse import ArgumentParser
import math
from itertools import permutations

def primzahlcheck(k):
    if k < 2 : 
        return False
    if k == 2:
        return True
    if k%2 == 0 or k  < 0 :
        return False
    for x in range(3, math.isqrt(k) + 1):
        if k % x == 0:
            return False
    return True

def check_concenating_prime(pps) :
    for i in range(len(pps)):
        for j in range(len(pps)):
            if i == j :
                continue
            if not primzahlcheck(int(str(pps[i]) + str(pps[j]))) :
                return False
    return True


def main():
    parser = ArgumentParser(description= "Task 60")
    parser.add_argument( "number_of_primes", help="Find the lowest sum for a set of N = five primes for which any two primes concatenate to produce another prime.")
    args = parser.parse_args()

    set_of_primes = [2]
    counter = 3

    while True :
        if primzahlcheck(counter) :
            for prime_pair_set in permutations(set_of_primes, int(args.number_of_primes) - 1) :
                prime_pair_set = prime_pair_set + (counter, )
                if check_concenating_prime(prime_pair_set) :
                    print(prime_pair_set)
            set_of_primes.append(counter)
        counter += 2
        print(counter)

if __name__ == "__main__":
    main() 