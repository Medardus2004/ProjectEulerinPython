from argparse import ArgumentParser
import math

def check_digit_factorial(s) :
    sum_factorials = 0
    for char in s :
        sum_factorials += math.factorial(int(char))
    if sum_factorials == int(s) :
        return True


def main():
    parser = ArgumentParser(description= "Find the sum of all numbers which are equal to the sum of the factorial of their digits.")
    parser.add_argument( "maximum", help="what is does")
    args = parser.parse_args()
    sum_of_digit_factorials = 0 
    for a in range (3, int(args.maximum)) :
        if check_digit_factorial(str(a)) :
            print(a)
            sum_of_digit_factorials += a
    print(sum_of_digit_factorials) 

if __name__ == "__main__":
    main() 