from argparse import ArgumentParser
from tqdm import tqdm
import gmpy2
import math
from fractions import Fraction

def bruch(b_0, step , b, D) : 
    length = step
    while True : 
        zaehler = b
        nenner = 1
        switcher = 1

        for i in range(1, length ) :
            switcher = nenner
            nenner = zaehler
            zaehler = switcher + nenner
            print("Step: " , i , " zaehler: " , 2* nenner + zaehler , " nenner: ", nenner)

        x = (b_0 - 1) * nenner + zaehler
        y = nenner
        print("------ x: " , x , " y: ", y , "D", D ,"--------")
        if x**2 == 1 + D * y**2  :
            return x
        else :
            length += step
        if length > 12 :
            break

def kettenbruchentwicklung(D):
    set_of_a = []
    set_of_b = [] 
    set_of_x = []

    a = math.sqrt(D)

    b_0 = math.floor(a)
    x = a - b_0

    set_of_x.append(str(x).split(".")[1][:6])

    for step in range(1 , 14) :
        a = 1 / x
        set_of_a.append(a)

        b = math.floor(a)
        set_of_b.append(b)

        x = a - b
        if str(x).split(".")[1][:6] in set_of_x :
            print(bruch(b_0, step, set_of_b[-2], D) )
            break
        
        #print("step: ", step ," a = ", a ," b = ", b ," x = ", x)


def main():
    parser = ArgumentParser(description= "Task 66")
    parser.add_argument( "maximum_D", help="what is does")
    args = parser.parse_args()
    largest_D = 0
    largest_x = 1
    kettenbruchentwicklung(float(args.maximum_D))

    #for d in tqdm(range(2, int(args.maximum_D) + 1)) :
    #    if gmpy2.is_square(d) :
    #        continue
    #    diophan = diophantine(d)
    #    if largest_x < diophan :
    #        largest_D = d
    #        largest_x = diophan
    #        print(largest_D, largest_x)

if __name__ == "__main__":
    main() 