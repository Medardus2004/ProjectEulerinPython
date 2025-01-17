from argparse import ArgumentParser

def create_concatenating_string(n) :
    concatenating_string = ""
    counter = 1
    while len(concatenating_string) < n :
        concatenating_string += str(counter)
        counter += 1
    return concatenating_string

def main():
    parser = ArgumentParser(description= "If d_n represents the n-th digit of the fractional part, find the value of the following expression")
    parser.add_argument( "dindex", help="largest index of d")
    args = parser.parse_args()
    concatenating_string = create_concatenating_string(int(args.dindex))
    print(int(concatenating_string[0]) * int(concatenating_string[9]) * int(concatenating_string[99]) * int(concatenating_string[999]) * int(concatenating_string[9999]) * int(concatenating_string[99999]) * int(concatenating_string[999999]))

if __name__ == "__main__":
    main() 