
def check_palindrome(num):
    res = [int(x) for x in str(num)]
    while res:
        if len(res) == 1:
            return True
        if res[0] != res[-1]:
            return False
        else:
            res.remove(res[0])
            res.remove(res[-1])
    return True

def solution_task004(N):
    highest_number = 0
    for x in range(10**(int(N)-1), 10**int(N)):
        for y in range(x, 10**int(N)):
            number = x*y
            if number > highest_number and check_palindrome(number):
                highest_number = number
    return highest_number
        
    


def solution():
    print("A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two N = 3-digit numbers.\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task004(n))
