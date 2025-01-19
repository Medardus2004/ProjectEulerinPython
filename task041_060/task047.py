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

def create_prime_list(maximum) :
    prime_list = []
    for i in range(2, maximum) : 
        if primzahlcheck(i) :
            prime_list.append(i)
    return prime_list

def prime_factors(num, prime_list, dictionary) :
    prime_factor_list = []
    acutal_primelist = filter(lambda x: x <= num, prime_list)
    for element in acutal_primelist :
        if num % element == 0 :
            prime_factor_list.append(element)
            num  //= element
            prime_factor_list += dictionary[num]
            break
    return prime_factor_list


def main():
    parser = ArgumentParser(description= "Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?")
    parser.add_argument( "-m", "--maximum", help="Maximum")
    args = parser.parse_args()

    prime_list = create_prime_list(int(args.maximum))
    set_dictionary = {}
    set_dictionary.update({1 : []})
    for counter in range(2, 5) :
        set_dictionary.update({counter: prime_factors(counter, prime_list, set_dictionary)})

    for counter in tqdm(range(5, int(args.maximum))) :
        set_dictionary.update({counter: prime_factors(counter, prime_list, set_dictionary)})
        if len(set(set_dictionary[counter])) == 4 and len(set(set_dictionary[counter - 1])) == 4 and len(set(set_dictionary[counter - 2])) == 4 and len(set(set_dictionary[counter - 3])) == 4 :  
            if len(set(set_dictionary[counter])) + len(set(set_dictionary[counter - 1])) == len(set(set_dictionary[counter] + set_dictionary[counter - 1])) :
                if len(set(set_dictionary[counter - 1])) + len(set(set_dictionary[counter - 2])) == len(set(set_dictionary[counter - 1] + set_dictionary[counter - 2])) :
                    if len(set(set_dictionary[counter - 2])) + len(set(set_dictionary[counter - 3])) == len(set(set_dictionary[counter - 2] + set_dictionary[counter - 3])) :
                        print(counter - 3)



if __name__ == "__main__":
    main() 