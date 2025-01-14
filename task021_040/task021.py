from argparse import ArgumentParser

def sum_proper_divisor(n):
    sum = 0
    for divisor in range(1, n):
        if n%divisor == 0:
            sum += divisor
    return sum

def count_amicable_numbers(n):
    sum = 0
    for counter in range(1, n):
        if counter == sum_proper_divisor(sum_proper_divisor(counter)) and counter != sum_proper_divisor(counter) :
            sum += counter
    return sum

def main():
    parser = ArgumentParser(description= "Evaluate the sum of all the amicable numbers under N = 10000.")
    parser.add_argument( "number", help="Number")
    args = parser.parse_args()
    print(count_amicable_numbers(int(args.number)))
    
if __name__ == "__main__":
    main() 