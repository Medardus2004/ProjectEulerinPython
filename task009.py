
def pythagoras(k):
    for b in range(2, int(k)):
        for a in range(1, b):
            # c = k - a - b
            if(a**2 + b**2 == (int(k) - (a + b))**2):
                return (a, b, int(k)- (a + b), a * b * (int(k) - (a + b)))
    return 0

def solution():
    print("A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c². For example, 3² + 4² = 5². There exists exactly one Pythagorean triplet for which a + b + c = 1000 = N.Find the product abc\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(pythagoras(n))
