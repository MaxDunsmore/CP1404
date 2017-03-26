"""
CP1404/CP5632 Practical
Lottery number generator
"""


import random


def main():
    count = 0
    quick_picks = int(input("How many quick picks? "))

    while not count == quick_picks:
        print(lottery_generator())
        count += 1


def lottery_generator():
    lottery_numbers = []
    while len(lottery_numbers) < 6:
        number = (random.randrange(1, 46))
        if number in lottery_numbers:
            pass
        else:
            lottery_numbers.append(number)
    lottery_numbers.sort()
    return"{:2} {:2} {:2} {:2} {:2} {:2}".format(lottery_numbers[0], lottery_numbers[1], lottery_numbers[2],
                                                 lottery_numbers[3], lottery_numbers[4], lottery_numbers[5])



main()




