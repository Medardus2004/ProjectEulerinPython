from argparse import ArgumentParser
import itertools

def permutate(n) :
    permuations = itertools.permutations('0123456789')
    print(list(permuations)[n-1])

def main():
    parser = ArgumentParser(description= "What is the n = millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?")
    parser.add_argument( "number", help="Number")
    args = parser.parse_args()
    permutate(int(args.number))

if __name__ == "__main__":
    main() 