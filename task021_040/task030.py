from argparse import ArgumentParser

def check_digit_fifth_power(n) :
    sum  = 0
    for a in n :
        sum += int(a)**5
    if sum == int(n) :
        return True
    else :
        return False

def main():
    parser = ArgumentParser(description= "Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()
    sum = 0
    for i in range (2, int(args.maximum)) :
        if check_digit_fifth_power(str(i)):
            sum += i
    print(sum)

if __name__ == "__main__":
    main() 