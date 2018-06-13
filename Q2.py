from math import gcd


def count_number_not_multiple_of_3_5_but_15(num: int):
    """if num == 0: #count from 1 to 0
    1 counts,
    0 counts (0 is a multiple of 15)
    if num < 0: #count from -(-1) to -(num) and plus 2 for 0 and 1"""
    count = 0
    if num <= 0:
        count += 2
    num = abs(num)
    count += num

    count3 = num//3
    count5 = num//5
    count15 = num//lcm(3, 5)
    count = count-count3-count5+2*count15
    return count


def lcm(x, y):
    return x//gcd(x, y)*y


if __name__ == '__main__':
    numberInput = int(input('input: '))
    print(count_number_not_multiple_of_3_5_but_15(numberInput))
    # for i in range(-5, 16):
    #     print(i, count_number_not_multiple_of_3_5_but_15(i))
