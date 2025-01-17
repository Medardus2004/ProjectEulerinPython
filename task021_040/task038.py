from argparse import ArgumentParser

def check_pandigital(pan_list):
    if len(pan_list) == len(set(pan_list)) == 9 and "0" not in pan_list:
        return True

def main():
    parser = ArgumentParser(description= "What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()
    largest_pandigital = 0
    for a in range(1, int(args.maximum)) :
        pandigital_list = []
        for b in range(1, 10) :
            pandigital_list.append(str(a*b))
            str_list = "".join(pandigital_list)
            if check_pandigital(str_list) and largest_pandigital < int(str_list):
                largest_pandigital = int(str_list)
            if len(str_list) > 9 :
                break
    print(largest_pandigital)

if __name__ == "__main__":
    main() 