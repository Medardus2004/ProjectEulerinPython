from argparse import ArgumentParser

def check_pandigital(a,b):
    all_numbers = list(str(a) + str(b) + str(a * b))
    if len(all_numbers) == len(set(all_numbers)) == 9 and "0" not in all_numbers:
        return True

def sum_of_pandigital_list(max_a, max_b) : 
    pandigital_list = []
    for a in range(1, max_a):
        for b in range(1, max_b):
            if check_pandigital(a, b) :
                pandigital_list.append(a*b)
    return sum(set(pandigital_list))

def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "-a", "--factor1", help="find for < a ")
    parser.add_argument( "-b", "--factor2", help="find for < b")
    args = parser.parse_args()
    print(sum_of_pandigital_list(int(args.factor1), int(args.factor2)))

if __name__ == "__main__":
    main() 