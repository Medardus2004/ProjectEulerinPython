from argparse import ArgumentParser
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

def spiral_diagonal(n) :
    counter = 0
    if primzahlcheck(n**2) :
        counter += 1
    if primzahlcheck(n**2 - (n - 1)) :
        counter += 1
    if primzahlcheck( n**2 - 2 * (n - 1)) :
        counter += 1
    if primzahlcheck( n**2 - 3 * (n - 1)) :
        counter += 1
    return counter


def main():
    parser = ArgumentParser(description= "What is the sum of the numbers on the diagonals in a n = 1001 by 1001 spiral formed in the same way?")
    parser.add_argument( "ratio", help="what is does")
    args = parser.parse_args()
    #print(spiral_diagonal(int(args.ratio)))
    side_length = 1
    prime_counter = 0
    number_of_odds = 1
    while True :
        side_length += 2
        number_of_odds += 4
        prime_counter += spiral_diagonal(side_length)
        if  prime_counter / number_of_odds <  float(args.ratio):
            print(side_length)
            break
    
if __name__ == "__main__":
    main() 