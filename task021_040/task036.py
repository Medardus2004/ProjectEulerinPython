from argparse import ArgumentParser

def check_palindrome_base2(num):
    res = [int(x) for x in num[2:]]
    for a in range(0, len(res)//2):
        if res[a] != res[-a - 1] :
            return False
    return True

def check_palindrome_base10(num):
    for a in range(0, len(num)//2):
        if num[a] != num[-a - 1] :
            return False
    return True

def check_palindrome_both(num) :
    if check_palindrome_base10(str(num)) and check_palindrome_base2(str(bin(num))) :
        return True
    
def main():
    parser = ArgumentParser(description= "Find the sum of all numbers, less than n = one million, which are palindromic in base 10 and base 2.")
    parser.add_argument( "max_number", help="less than max number")
    args = parser.parse_args()
    total_sum = 0
    for counter in range(1, int(args.max_number)) :
        if check_palindrome_both(counter) :
            total_sum += counter
    print(total_sum)

if __name__ == "__main__":
    main() 