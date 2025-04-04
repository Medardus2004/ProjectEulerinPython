from argparse import ArgumentParser

def check_palindrome_base10(num):
    for a in range(0, len(num)//2):
        if num[a] != num[-a - 1] :
            return False
    return True

def check_lychrel(num) :
    for _ in range(50) :
        num += int(str(num)[::-1])
        if check_palindrome_base10(str(num)) :
            return True
    return False

def main():
    parser = ArgumentParser(description= "Task 55")
    parser.add_argument( "maximum", help="what is does")
    args = parser.parse_args()

    counter = 0
    for i in range(1, int(args.maximum)) :
        if check_lychrel(i) :
            counter += i
    print(counter)


if __name__ == "__main__":
    main() 