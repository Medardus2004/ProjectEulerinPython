from argparse import ArgumentParser
import numpy as np

def get_cross_sum(Num):
    summe = 0
    for number in Num:
        summe += int(number)
    return summe

def main():
    parser = ArgumentParser(description= "Task 56")
    parser.add_argument( "maximum", help="what is the maximum digital sum")
    args = parser.parse_args()
    largest_cross_sum = 0
    for a in range(1,  int(args.maximum) ) :
        for b in range(1,  int(args.maximum) ) :
            cross_sum = get_cross_sum(str(np.power(a,b, dtype=object)))  
            if largest_cross_sum < cross_sum  :
                largest_cross_sum = cross_sum
    print(largest_cross_sum)

if __name__ == "__main__":
    main() 