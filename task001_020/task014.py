

def collatz(N):
    biggestchain = 1
    biggestCollatz = 1
    for x in range(2,  N, 1):
        counter = 0
        remember = x
        while(x != 1):
            if x % 2 == 1:
                x = x*3 +1
                counter += 1
            else:
                x /= 2
                counter += 1
        if counter > biggestchain :
            biggestchain = counter
            biggestCollatz = remember
    return biggestCollatz


def solution():
    print("It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number, under N = one million, produces the longest chain??\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(collatz(int(n)))
