from argparse import ArgumentParser

def read_data(wordlist):
    datei =  open(wordlist, "r")
    for zeile in datei :
        names = zeile
    name_list = names.replace('"','').split(',')
    name_list.sort()
    return(name_list)

def alphabetical_value(name):
    sum = 0
    for char in name:
        sum += ord(char)-64
    return sum

def total_name_score(wordlist):
    result = 0
    list = read_data(wordlist)
    for name in list:
        result += (list.index(name)+1)*alphabetical_value(name)
    return result

def main():
    parser = ArgumentParser(description= "What is the total of all the name scores in the file?")
    parser.add_argument( "wordlist", help="Wordlist")
    args = parser.parse_args()
    print(total_name_score(args.wordlist))

if __name__ == "__main__":
    main() 