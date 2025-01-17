from argparse import ArgumentParser
import math
from tqdm import tqdm

def check_pandigital(pan_list):
    if len(pan_list) == len(set(pan_list)) and "0" not in pan_list and "9" not in pan_list and "8" not in pan_list:
        return True

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

def main():
    parser = ArgumentParser(description= "What is the largest n-digit pandigital prime that exists?")
    parser.add_argument( "maximum", help="Maximum, try 1000000000")
    args = parser.parse_args()
    for counter in tqdm(range(1000000, 7654321)):
        if  check_pandigital(list(str(counter))) and primzahlcheck(counter) :
            print(counter)

if __name__ == "__main__":
    main() 