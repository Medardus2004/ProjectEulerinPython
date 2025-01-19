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
    counter = 5
    prime_list = [2, 3] 
    set_dictionary = {
        1 : {}, 
        2 : {2},
        3 : {3},
        4 : {2, 2}
    }
    while True :
        if primzahlcheck(counter) :
            prime_list.append(counter)
        set_dictionary.update({counter: prime_factors(counter, prime_list, set_dictionary)})
        
        if len(set(set_dictionary[counter])) == 4 and len(set(set_dictionary[counter - 1])) == 4 and len(set(set_dictionary[counter - 2])) == 4 and len(set(set_dictionary[counter - 3])) == 4 :  
            if len(set(set_dictionary[counter])) + len(set(set_dictionary[counter - 1])) == len(set(set_dictionary[counter] + set_dictionary[counter - 1])) :
                if len(set(set_dictionary[counter - 1])) + len(set(set_dictionary[counter - 2])) == len(set(set_dictionary[counter - 1] + set_dictionary[counter - 2])) :
                    if len(set(set_dictionary[counter - 2])) + len(set(set_dictionary[counter - 3])) == len(set(set_dictionary[counter - 2] + set_dictionary[counter - 3])) :
                        print(counter - 3)
                        break
        counter += 1

if __name__ == "__main__":
    main() 