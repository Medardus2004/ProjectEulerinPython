from argparse import ArgumentParser
import itertools as it

def create_permutations() :
    permuations = it.permutations('0123456789')
    return list(permuations)

def main():
    #parser = ArgumentParser(description= "Task x")
    #parser.add_argument( "xyz", help="what is does")
    #parser.add_argument( "-a", "--abc", help="Alphabet")
    #args = parser.parse_args()
    total_sum = 0
    permutation_list = create_permutations()
    for element in permutation_list :
        if int(element[1]+element[2]+element[3]) % 2 == 0 :
            if int(element[2]+element[3]+element[4]) % 3 == 0 :
                if int(element[3]+element[4]+element[5]) % 5 == 0 :
                    if int(element[4]+element[5]+element[6]) % 7 == 0 :
                        if int(element[5]+element[6]+element[7]) % 11 == 0 :
                            if int(element[6]+element[7]+element[8]) % 13 == 0 :
                                if int(element[7]+element[8]+element[9]) % 17 == 0 :
                                    total_sum += int("".join(element))
    print(total_sum)
if __name__ == "__main__":
    main() 