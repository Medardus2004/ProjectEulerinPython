from argparse import ArgumentParser
from tqdm import tqdm
import gmpy2
import math
import numpy as np


memo = {}

def diophantine(D, x, y) :
    if x**2 - D * y**2 == 1 :
        return True
    else :
        return False

def kettenbruch(set_of_b) :
    length = len(set_of_b)
    if length in memo:
        return memo[length]
    if len(set_of_b) == 1 :
         result=  np.array([set_of_b[0] , 1])
    else :
        result =  np.array([kettenbruch(set_of_b[1:])[1] + set_of_b[0] * kettenbruch(set_of_b[1:])[0], kettenbruch(set_of_b[1:])[0]])   
    memo[length] = result
    return result

def create_set(D) :
    set_of_a = []
    set_of_b = [] 
    set_of_x = []

    a = math.sqrt(D)

    b_0 = math.floor(a)
    set_of_b.append(b_0)
    x = a - b_0
    set_of_x.append(str(x)[:6])
    # set_of_x.append(str(x).split(".")[1][:6])

    #while True :
    for _ in range (1, 200) :
        b = math.floor(1 / x)
        x = 1 / x - b

        if str(x)[:6] in set_of_x :    
            bruch = kettenbruch(set_of_b)
            global memo 
            memo = {}
            # print(set_of_b, bruch)
            if diophantine(D, bruch[0], bruch[1]) :
                return bruch[0]
            
        set_of_x.append(str(x)[:6])
        set_of_b.append(b)
    print(D, " is out of range for 200 iterations")
    return 0


def main():
    parser = ArgumentParser(description= "Task 66")
    parser.add_argument( "maximum_D", help="Diophantine equation")
    args = parser.parse_args()
    largest_D = 0
    largest_x = 1
    #create_set(int(args.maximum_D))
    for d in tqdm(range(2, int(args.maximum_D) + 1)) :
        if gmpy2.is_square(d) :
            continue
        x = create_set(int(d))
        if largest_x < x  :
            largest_D = d
            largest_x = x
    print(largest_D, largest_x)

if __name__ == "__main__":
    main() 