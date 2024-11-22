def solution_task001(N):
    sum = 0
    for x in range(int(N)):
        if(x%3 == 0 or x%5 == 0):
            sum += x
    return sum


def solution():
    print("If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3, 5, 6 and  9. The sum of these multiples is 23.\n Find the sum of all the multiples 3 of 5 below N = 1000.\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task001(n))
