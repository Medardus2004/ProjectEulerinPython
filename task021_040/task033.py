from argparse import ArgumentParser

def check_fraction(enumerator, denumerator):
    enumerator_list = list(str(enumerator))
    denumerator_list = list(str(denumerator))
    for element in enumerator_list :
        if element in denumerator_list and element != "0":
            enumerator_list.remove(element)
            denumerator_list.remove(element)
    if enumerator * int("".join(denumerator_list)) == denumerator * int("".join(enumerator_list)) and len(enumerator_list) != len(str(enumerator)):
        return (int("".join(enumerator_list)), int("".join(denumerator_list))) 

def main():
    parser = ArgumentParser(description= "Task x")
    # parser.add_argument( "xyz", help="what is does")
    parser.add_argument( "-e", "--enumerator", help="Numerator")
    parser.add_argument( "-d", "--denumerator", help="Enumerator")
    args = parser.parse_args()
    for enu in range(10, int(args.enumerator)) :
        for denu in range(enu+1, int(args.denumerator)) :         
            if check_fraction(enu, denu) :
                print(enu, denu, check_fraction(enu, denu))

if __name__ == "__main__":
    main() 