from numpy import * 

def read_data():
    with open("problem013.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        return(lines)

def sum_of_lines():
    lines = read_data()
    rest = 0
    ###########################
    #### lines[row][column]
    #### number of columns = len(lines[0]) i.e. x goes from 49 to 0
    #### number of rows = len(lines) i.e. y goes from 0 to 50
    ############################
    for x in range(len(lines[0])-1, -1, -1):
        for y in range(0, len(lines)):             
            rest += int(lines[y][x])
        print(rest%10)
        rest = (rest - ( rest % 10 )) / 10 
    print(rest)
    return 0



def solution():
    print("Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.\n\n")
    print("Answer:\n")
    print(sum_of_lines())