from argparse import ArgumentParser
from tqdm import tqdm

def create_penatgon_numbers(num) :
    pentagonal_list = []
    for i in range(1, num) :
         pentagonal_list.append(i * (3 * i - 1) // 2)
    return pentagonal_list

def main():
    parser = ArgumentParser(description= "Find the pair of pentagonal numbers")
    parser.add_argument( "pentagonal", help="pentagonal")
    args = parser.parse_args()

    pentagonal_list = create_penatgon_numbers(int(args.pentagonal))
    for element1 in tqdm(range(1, int(args.pentagonal) - 1)) :
        for element2 in range(element1, int(args.pentagonal) - 1) :
            if pentagonal_list[element1] - pentagonal_list[element2] in pentagonal_list and pentagonal_list[element1] + pentagonal_list[element2] in pentagonal_list :
                print (pentagonal_list(element1), pentagonal_list(element2))

if __name__ == "__main__":
    main() 