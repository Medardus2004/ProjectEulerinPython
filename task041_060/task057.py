from argparse import ArgumentParser
import numpy as np
import sys

memo = {}
sys.setrecursionlimit(2000)

def check_nom_denom(nom, denom) :
    if len(str(nom) == len(str(denom))) :
        return True
    else :
        return False

def kettenbruch(iter) : 
    if iter in memo:
        return memo[iter]
    if iter == 0 :
         result=  np.array([1 , 2], dtype=object)
    else :
        result =  np.array([ kettenbruch(iter -1)[1],2 * kettenbruch(iter -1)[1] + kettenbruch(iter -1)[0] ], dtype=object)   
    memo[iter] = result
    return result

def main():
    parser = ArgumentParser(description= "Task 57")
    parser.add_argument( "iterations", help="what is does")
    args = parser.parse_args()
    
    kettenbruch(int(args.iterations))

    fractions_with_more_digits = 0
    for counter in range(0, len(memo)) :
        memo[counter][0] += memo[counter][1]
        if (len(str(memo[counter][0]))) != (len(str(memo[counter][1]))) :
            fractions_with_more_digits += 1
    print(fractions_with_more_digits)



if __name__ == "__main__":
    main() 