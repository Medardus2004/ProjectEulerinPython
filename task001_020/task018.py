from numpy import * 

def read_data():
    with open("problem018.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        rows = len(lines)
        matrix = [[0 for _ in range(rows)] for _ in range(rows)]
        ###########################
        #### matrix[row][column]
        #### number of rows = len(lines) i.e. x goes from 0 to 50
        #### number of columns = len(lines[0]) i.e. y goes from 0 to 
        ############################
        for x in range(0, rows):
            for y in range(0, x + 1):
                matrix[x][y] = int(lines[x][3*y] + lines[x][3*y+1])
        return(matrix)

def sum_of_lines():
    matrix = read_data()
    for row in range(len(matrix) - 2, -1 , -1):
        for column in range(0, len(matrix)-1):
            if matrix[row+1][column] > matrix[row+1][column+1] :
                matrix[row][column] += matrix[row+1][column]
            else:
                matrix[row][column] += matrix[row+1][column+1]
    return matrix[0][0]


def solution():
    print("Find the maximum total from top to bottom of the triangle below.\n\n")
    print("Answer:\n")
    print(sum_of_lines())