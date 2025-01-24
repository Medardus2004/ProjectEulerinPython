
import itertools as it

def create_permutations(s) :
    permuations = it.permutations(s)
    return list(permuations)

def main():
    counter = 10
    while True :
        permutations = create_permutations(str(counter))
        perm_list = []
        for element in permutations :
            perm_list.append("".join(element))
        if str(2 * counter) in perm_list :
            if str(3 * counter) in perm_list :
                if str(4 * counter) in perm_list :
                    if str(5 * counter) in perm_list :
                        if str(6 * counter) in perm_list :
                            print(counter)
                            break
        counter += 1

if __name__ == "__main__":
    main() 