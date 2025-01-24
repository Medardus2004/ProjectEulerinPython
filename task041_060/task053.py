
import math

def main():
    counter = 0
    for n in range(1, 101) :
        for r in range(1, n + 1) :
            if math.comb(n, r) > 1000000 :
                counter += 1
    print(counter)

if __name__ == "__main__":
    main() 