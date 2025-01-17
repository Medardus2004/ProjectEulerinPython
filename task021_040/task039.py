from argparse import ArgumentParser
import math
from tqdm import tqdm

def find_possible_triangles(perimeter) :
    triangle_list = []
    for a in range(1, perimeter):
        for b in range(a, perimeter) :
            c = math.isqrt(a**2 + b**2)
            if a**2 + b**2 == c**2 and a + b + c == perimeter :
                triangle_list.append([a , b ,c])
    return triangle_list 

def main():
    parser = ArgumentParser(description= "For which value of p < 1000, is the number of solutions maximised?")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()
    max_triangles = 0
    for counter in tqdm(range(1, int(args.maximum))) :
        if len(find_possible_triangles(counter)) > max_triangles :
            max_triangles = len(find_possible_triangles(counter))
            print(find_possible_triangles(counter), max_triangles, counter)

if __name__ == "__main__":
    main() 