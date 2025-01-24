from argparse import ArgumentParser
import math
from tqdm import tqdm

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
    parser = ArgumentParser(description= "Which prime, below maximum = one-million, can be written as the sum of the most consecutive primes?")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()
    max_counter = 0
    max_elements_in_sum = []
    for i in tqdm(range(2, int(args.maximum))) :
        if primzahlcheck(i) :
            counter = 1
            between_counter = 0
            sum_primes = i
            elements_in_sum = [i]
            j = i + 1
            while True : 
                if primzahlcheck(j) :
                    sum_primes += j
                    if sum_primes > int(args.maximum) :
                        break
                    elements_in_sum.append(j)
                    if primzahlcheck(sum_primes) : 
                        counter += between_counter + 1 
                        between_counter = 0
                    else :
                        between_counter += 1
                j += 1      
            if counter > max_counter :
                max_counter = counter
                max_elements_in_sum = elements_in_sum
    print(max_counter, sum(max_elements_in_sum))

if __name__ == "__main__":
    main() 