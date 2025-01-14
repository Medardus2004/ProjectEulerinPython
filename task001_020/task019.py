import datetime

def count_mondays():
    counter = 0
    for year in range(1901, 2001):
        for month in range(1,13):
            if datetime.datetime(year, month, 1).weekday() == 6 :
                counter += 1
    return counter

def solution():
    print("How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000.\n\n")
    print("Answer:\n")
    print(count_mondays())