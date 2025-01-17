from argparse import ArgumentParser
import math

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

def remove_right_to_left(num) :
    for a in range(0, len(num)) :
        if not primzahlcheck(int(num[a:])) :
            return False
    return True

def remove_left_to_right(num) :
    for a in range(len(num), 0, -1) :
        if not primzahlcheck(int(num[:a])) :
            return False
    return True

def main():
    parser = ArgumentParser(description= "Find the sum of the only eleven primes that are both truncatable from left to right and right to left.")
    parser.add_argument( "max_number", help="less than max number")
    args = parser.parse_args()
    total_sum = 0
    for i in range(11, int(args.max_number)):
        if remove_left_to_right(str(i)) and remove_right_to_left(str(i)) :
            total_sum += i
    print(total_sum)

if __name__ == "__main__":
    main() 