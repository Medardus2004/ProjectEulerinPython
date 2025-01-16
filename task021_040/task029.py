from argparse import ArgumentParser

def create_power_list(max_a, max_b) :
    list = []
    for a in range(2, max_a+1) :
       for b in range(2, max_b+1) :
           list.append(a**b)
    return list


def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "-a", "--coefficient", help="find for < a ")
    parser.add_argument( "-b", "--exponent", help="find for < b")
    args = parser.parse_args()
    print(len(set(create_power_list(int(args.coefficient), int(args.exponent)))))

if __name__ == "__main__":
    main() 