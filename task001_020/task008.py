
    
def solution_task008(N):
    max_sum = 0
    with open("problem008.txt", "r") as f:
        data = f.read()
        for x in range(len(data)-int(N)):
            count = 1
            for y in range(int(N)):
                count *= int(data[x+y])
            if count > max_sum:
                max_sum = count
    return max_sum

def solution():
    print("The four adjacent digits in the 1000-digit number that have the greatest product are 5832. Find the N = thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product???\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(solution_task008(n))
