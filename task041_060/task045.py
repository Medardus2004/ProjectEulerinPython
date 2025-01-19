from argparse import ArgumentParser

def create_triangle_numbers(num) :
    triangle_list = []
    for i in range(1, num) :
         triangle_list.append(i * (i + 1) // 2)
    return triangle_list

def create_penatgon_numbers(num) :
    pentagonal_list = []
    for i in range(1, num) :
         pentagonal_list.append(i * (3 * i - 1) // 2)
    return pentagonal_list

def create_hexagon_numbers(num) :
    hexagonal_list = []
    for i in range(1, num) :
         hexagonal_list.append(i * (2 * i - 1))
    return hexagonal_list

def main():
    parser = ArgumentParser(description= "Find the pair of pentagonal numbers")
    parser.add_argument( "maximum", help="Maximum")
    args = parser.parse_args()

    triangle_list = create_triangle_numbers(int(args.maximum))
    pentagon_list = create_penatgon_numbers(int(args.maximum))
    hexagon_list = create_hexagon_numbers(int(args.maximum))

    for element in triangle_list :
        if  element in hexagon_list :
            if element in pentagon_list :
                print(element)

if __name__ == "__main__":
    main() 