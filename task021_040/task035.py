from argparse import ArgumentParser
from collections import deque
from tqdm import tqdm
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

def check_circular_prime(n) :
    single_list = list(n)
    rot_list = deque(single_list)
    for _ in single_list :
        if not primzahlcheck(int("".join(rot_list))) :
            return False
        rot_list.rotate(1)
    return True

def main():
    parser = ArgumentParser(description= "How many circular primes are there below maximum = one million?")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()
    counter = 0
    for i in tqdm(range(2, int(args.maximum))) :
        if check_circular_prime(str(i)) :
            counter += 1
    print(counter)
        

if __name__ == "__main__":
    main() 