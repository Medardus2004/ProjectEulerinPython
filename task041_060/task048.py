from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description= "Find the last ten digits of the series")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()

    total_sum = 0
    for counter in range(1, int(args.maximum) + 1) :
        total_sum += counter**counter
        total_sum %= 10000000000
    print(total_sum)

if __name__ == "__main__":
    main() 