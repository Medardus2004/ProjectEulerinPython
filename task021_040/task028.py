from argparse import ArgumentParser


def spiral_diagonal(n) :
    sum = 1
    for i in range(3, n+1) :
        if i % 2 == 1 :
            sum += i**2
            sum += i**2 - (i - 1)
            sum += i**2 - 2 * (i - 1)
            sum += i**2 - 3 * (i - 1)
    return sum


def main():
    parser = ArgumentParser(description= "What is the sum of the numbers on the diagonals in a n = 1001 by 1001 spiral formed in the same way?")
    parser.add_argument( "number", help="what is does")
    args = parser.parse_args()
    print(spiral_diagonal(int(args.number)))

if __name__ == "__main__":
    main() 