"""
Задания из 18 урока "Сириуса"
"""

from random import randint
from math import sqrt, pi, cos, sin, e


def task_1():
    count = int(input("enter coin flip count: "))
    heads = 0
    tails = 0
    for i in range(count):
        if bool(randint(0,1)):
            heads += 1
        else:
            tails += 1
    print(f"heads count: {heads} ({round(heads / count, 4)}); tails count: {tails} ({round(tails / count, 4)}); ")
    return 0


def task_2():
    num1, num2, num3, num4, num5, num6 = 0, 0, 0, 0, 0, 0
    count = int(input("enter dice rolls count: "))
    for i in range(count):
        dice = randint(1,6)
        match dice:
            case 1: num1 += 1
            case 2: num2 += 1
            case 3: num3 += 1
            case 4: num4 += 1
            case 5: num5 += 1
            case 6: num6 += 1
    print(f"1: {num1} ({round(num1 / count, 4)})")
    print(f"2: {num2} ({round(num2 / count, 4)})")
    print(f"3: {num3} ({round(num3 / count, 4)})")
    print(f"4: {num4} ({round(num4 / count, 4)})")
    print(f"5: {num5} ({round(num5 / count, 4)})")
    print(f"6: {num6} ({round(num6 / count, 4)})")
    return 0


def task_3():
    password = ""
    char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    password_len = int(input("enter password len: "))
    for i in range(password_len):
        password += char_list[randint(0, len(char_list) - 1)]
    print(f"password: {password}")
    return 0


def task_4():
    print("enter x1, y1, x2 and y2: ")
    x1, y1, x2, y2 = map(float, input().split())
    p = round(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), 4)
    print(f"distance: {p}")
    return 0

def task_5():
    R = float(input("enter radius: "))
    print(f"area: {round(pi * pow(R, 2), 4)}; perimeter: {round(2 * pi * R, 4)}")
    return 0


def task_6():
    print("enter x and t")
    x, t = map(int, input().split())
    z = ((9 * pi * t + 10 * cos(x)) / (sqrt(t) - abs(sin(t)))) * pow(e, x)
    print(f"result: {round(z, 2)}")
    return 0


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    task_6()