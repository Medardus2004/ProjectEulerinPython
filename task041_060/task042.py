from argparse import ArgumentParser

def create_triangle_list(num) :
    triangle_list = []
    for i in range(1, num) :
        triangle_list.append(i*(i+1)//2)
    return triangle_list

def read_data(wordlist):
    datei =  open(wordlist, "r")
    for zeile in datei :
        names = zeile
    name_list = names.replace('"','').split(',')
    name_list.sort()
    return(name_list)

def alphabetical_value(name):
    total_sum = 0
    for char in name:
        total_sum += ord(char)-64
    return total_sum

def main():
    parser = ArgumentParser(description= "Using words.txt , a 16K text file containing nearly two-thousand common English words, how many are triangle words?")
    parser.add_argument( "-t", "--triangle", help="size of triangle list")
    parser.add_argument( "-w", "--wordlist", help="path to word list")
    args = parser.parse_args()
    counter = 0
    triangle_list = create_triangle_list(int(args.triangle))
    for element in read_data(args.wordlist) :
        if alphabetical_value(element) in triangle_list :
            counter += 1
    print(counter)

if __name__ == "__main__":
    main() 