import inflect

def numbertowords(letter):
    p = inflect.engine()
    new_string = p.number_to_words(letter).replace("-", "").replace(",", "").replace(" ", "")
    return len(new_string)

def countletters(N):
    counter = 0
    for x in range(1, N +1):
        counter += numbertowords(x)
    return counter

def solution():
    print("If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 19 letters used in total. If all the numbers from 1 to N = 1000  (one thousand) inclusive were written out in words, how many letters would be used?\n\n")
    print("Enter N:\n")
    n = input()
    print("Answer:\n")
    print(countletters(int(n)))
