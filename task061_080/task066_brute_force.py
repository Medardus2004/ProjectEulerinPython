from argparse import ArgumentParser
from tqdm import tqdm
import gmpy2
import math
import numpy as np

def find_x(D) :
    x = D
    while True :
        for y in range(1, x) :
            if x **2 - D * y**2 == 1 :
                return x
        x += 1


def main():
    parser = ArgumentParser(description= "Task 66")
    parser.add_argument( "maximum_D", help="Diophantine equation")
    args = parser.parse_args()
    largest_D = 0
    largest_x = 1
    print(find_x(int(args.maximum_D)))


if __name__ == "__main__":
    main() 