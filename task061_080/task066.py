from argparse import ArgumentParser
from tqdm import tqdm
import gmpy2
import math
import numpy as np
import sys


sys.setrecursionlimit(10000)

memo = {}

def diophantine(D, x, y ) :
    if np.multiply(x, x, dtype=object) - D * np.multiply(y, y, dtype=object)  == 1 :
        return True
    else :
        return False

def kettenbruch(set_of_b) :
    length = len(set_of_b)
    if length in memo:
        return memo[length]
    if len(set_of_b) == 1 :
         result=  np.array([set_of_b[0] , 1], dtype=object)
    else :
        result =  np.array([kettenbruch(set_of_b[1:])[1] + set_of_b[0] * kettenbruch(set_of_b[1:])[0], kettenbruch(set_of_b[1:])[0]], dtype=object)   
    memo[length] = result
    return result

def create_set(D) :
    set_of_b = [] 
    # set_of_x = []

    b_0 = math.floor(math.sqrt(D))
    set_of_b.append(b_0)
    x = math.sqrt(D) - b_0
    # set_of_x.append(str(x)[:6])

    for _ in range (1, 10000) :
        b = math.floor(1 / x)
        x = 1 / x - b

        # if str(x)[:6] in set_of_x :    
        bruch = kettenbruch(set_of_b)
        global memo 
        memo = {}
        if diophantine(D, bruch[0], bruch[1]) :
            return bruch[0]
            
        #set_of_x.append(str(x)[:6])
        set_of_b.append(b)

    print(D, " is out of range for 10000 iterations")
    return 0

def main():
    parser = ArgumentParser(description= "Task 66")
    parser.add_argument( "maximum_D", help="Diophantine equation")
    args = parser.parse_args()
    largest_D = 0
    largest_x = 1
    for d in tqdm(range(1, int(args.maximum_D) + 1)) :
        if gmpy2.is_square(d) :
            continue
        x = create_set(int(d))
        if largest_x < x  :
            largest_D = d
            largest_x = x
        print(d, x)
    print(largest_D, largest_x)

if __name__ == "__main__":
    main() 