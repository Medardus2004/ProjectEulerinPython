from argparse import ArgumentParser
import itertools as it
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

def create_permutations(s) :
    permuations = it.permutations(s, 4)
    return list(permuations)

def main():
    for i in range(1234, 3340) :
        term = [i, i + 3330, i + 6660]
        perm_list = []
        perm = create_permutations(str(i))
        for element in perm :
            perm_list.append("".join(element))
        if str(term[0]) in perm_list and  primzahlcheck(term[0]):
            if str(term[1]) in perm_list and  primzahlcheck(term[1]):
                if str(term[2]) in perm_list and  primzahlcheck(term[2]):
                    print(term[0], term[1], term[2])

if __name__ == "__main__":
    main() 