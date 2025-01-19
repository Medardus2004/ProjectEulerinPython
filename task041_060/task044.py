def penatgon_number(num) :
    return num * (3 * num - 1) // 2

def main():
    pentagonal_list = []
    element1 = 0
    while True : 
        pentagonal_list.append(penatgon_number(element1))
        for element2 in range(1, element1) :
            if pentagonal_list[element1] - pentagonal_list[element2] in pentagonal_list :
                if 2 *pentagonal_list[element2] - pentagonal_list[element1] in pentagonal_list :
                    print( 2* pentagonal_list[element2] - (pentagonal_list[element1]))
        element1 += 1

if __name__ == "__main__":
    main() 