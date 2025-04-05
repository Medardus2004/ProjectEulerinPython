from argparse import ArgumentParser


def create_palindrome(num) :
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def check_palindrome_base10(num):
    for a in range(0, len(num)//2):
        if num[a] != num[-a - 1] :
            return False
    return True

def check_lychrel(num) :
    for _ in range(50) :
        num += create_palindrome(num)
        if check_palindrome_base10(str(num)) :
            return False
    return True

def main():
    parser = ArgumentParser(description= "Task 55")
    parser.add_argument( "maximum", help="what is does")
    args = parser.parse_args()

    lychrel_counter = 0
    for i in range (1, int(args.maximum)) :
        if check_lychrel(i) :
            lychrel_counter += 1

    print(lychrel_counter)

if __name__ == "__main__":
    main() 