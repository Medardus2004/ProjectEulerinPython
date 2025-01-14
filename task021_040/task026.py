def get_long_division_cycle_length(denominator: int) -> int:
    numerator = 10
    digits = []
    remainders = []
    cur = numerator
    while True:
        digit = cur // denominator
        cur = cur % denominator
        if cur in remainders:
            break
        digits.append(digit)
        remainders.append(cur)
        cur *= 10
        if cur == 0:
            return 0
        while cur < denominator:
            cur *= 10
            digits.append(0)
    while remainders[0] != cur:
        remainders.pop(0)
    return len(remainders)

def solution_long_division() -> int:
    cycle_lengths = {denominator: get_long_division_cycle_length(denominator) for denominator in range(1, 1000)}
    return sorted(cycle_lengths.items(), key=lambda item: item[1])[-1][0]

def task026_output():
    print("A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given: \n 1/2 = 0.5 \n 1/6 = 0.1(6) \n 1/7 = 0.(142857) \n ... \n Where 0.1(6) means , 0.16666 and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle. Find the value of  d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.\n\n Answer:")
    print(solution_long_division())
