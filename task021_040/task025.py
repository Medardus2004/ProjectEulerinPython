from argparse import ArgumentParser

def fibonacci():
    list = [1, 1]
    next_fibonacci = 0
    counter = 2
    while next_fibonacci < 10**999 :
        next_fibonacci = list[0]+ list[1]
        list.append(next_fibonacci)
        list.remove(min(list))
        counter += 1
    return list[1], counter

def main():
    parser = ArgumentParser(description= "Task x")
    args = parser.parse_args()
    print(fibonacci())

if __name__ == "__main__":
    main() 