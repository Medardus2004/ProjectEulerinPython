from tqdm import tqdm
import math
from argparse import ArgumentParser


def primzahlcheck(k):
    for x in range(2, math.isqrt(k) + 1):
        if k % x == 0:
            return False
    return True

def main():
    parser = ArgumentParser(description= "Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an number = eight prime value family.")
    parser.add_argument( "numbers", help="Amount of numbers")
    args = parser.parse_args()

    # check for two digit
    max_counter = 0
    already_checked_list = []
    number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for element in tqdm(range(10**(int(args.numbers) -1), 10**int(args.numbers))) :
        if primzahlcheck(element) and element not in already_checked_list:
            word_number = list(str(element)) 
            for a in range(0, int(args.numbers)) :
                for b in range(a+1, int(args.numbers)) :
                    counter = 0
                    for number in number_list :
                        word_number[a] = number
                        word_number[b] = number
                        tocheck_number = int(''.join(word_number))
                        already_checked_list.append(tocheck_number)
                        if primzahlcheck(tocheck_number):
                            counter += 1
                            if max_counter < counter :
                                max_counter = counter
                                print(f" max_counter for 2: {counter}, min. Primzahl: {element}" )

if __name__ == "__main__":
    main() 