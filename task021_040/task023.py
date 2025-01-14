from argparse import ArgumentParser

def sum_proper_divisor(n):
    sum = 0
    for divisor in range(1, n):
        if n%divisor == 0:
            sum += divisor
    return sum

def is_abundant(n):
    if sum_proper_divisor(n) > n :
        return True
    else:
        return False

def list_all_abundant(n):
    abundant_list = []
    for i in range(1, n):
        if is_abundant(i):
            abundant_list.append(i)
    return abundant_list

def list_sum_two_abundant(n):
    sum = []
    list = list_all_abundant(n)
    for i in range(1, n):
        new_list = [x for x in list if x < i ]
        for element in new_list :
            if i-element in new_list :
                sum.append(i)
                break
    final_list = set(sum)
    return final_list

def sum_of_not_in_list(n):
    sum = 0
    list = list_sum_two_abundant(n)
    for i in range(1, n):
        if i not in list:
            sum += i
    return sum

def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "highest", help="highest number")
   # parser.add_argument( "-a", "--abc", help="Alphabet")
    args = parser.parse_args()
    print(sum_of_not_in_list(int(args.highest)))

if __name__ == "__main__":
    main() 