from numpy import * 

def read_data():
    with open("problem011.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        rows = len(lines)
        matrix = [[0 for _ in range(rows)] for _ in range(rows)]
        for x in range(0, rows):
            for y in range(0, rows):
                matrix[x][y] = lines[x][3*y] + lines[x][3*y + 1]
        return(matrix)

def biggest_vertical(N):
    highest = 1
    matrix = read_data()
    rows = len(matrix)
    for x in range(0, rows - int(N)):
        for y in range(0, rows):
            factor = 1
            for r in range(0, int(N)):
                factor *= int(matrix[x+r][y])
            if factor > highest :
                highest = factor
    return highest
    
def biggest_horizontal(N):
    highest = 1
    matrix = read_data()
    rows = len(matrix)
    for x in range(0, rows):
        for y in range(0, rows-int(N)):
            factor = 1
            for r in range(0, int(N)):
                factor *= int(matrix[x][y+r])
            if factor > highest :
                highest = factor
    return highest

def biggest_diagonal(N):
    highest = 1
    matrix = read_data()
    rows = len(matrix)
    for x in range(0, rows - int(N)):
        for y in range(0, rows-int(N)):
            factor = 1
            for r in range(0, int(N)):
                factor *= int(matrix[x+r][y+r])
            if factor > highest :
                highest = factor
    return highest

def biggest_contradiagonal(N):
    highest = 1
    matrix = read_data()
    rows = len(matrix)
    for x in range(int(N), rows):
        for y in range(int(N), rows):
            factor = 1
            for r in range(0, int(N)):
                factor *= int(matrix[x-r][y-r])
            if factor > highest :
                highest = factor
    return highest



def solution():
    print("In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.  What is the greatest product of N = four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid???\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
 #   print(read_data())
    print(biggest_vertical(n))
    print(biggest_horizontal(n))
    print(biggest_diagonal(n))
    print(biggest_contradiagonal(n))    