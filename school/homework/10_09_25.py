"""
Задания из 17 урока "Сириуса"
"""

# from math import pow


def task_2():
    a, b = map(int, input().split())
    print(3 * pow((a + b), 3) + 275 * pow(b, 3) - 127 * a - 41)
    return 0


def task_3():
    F = float(input())
    print(5 / 9 * (F - 32))
    return 0


def task_4():
    sit_number = int(input())
    if sit_number % 4 != 0:
        print(sit_number // 4 + 1)
    else:
        print(sit_number // 4)
    return 0


if __name__ == "__main__":
    print("task num 2")
    task_2()
    print("task num 3")
    task_3()
    print("task num 4")
    task_4()
    input("press enter to exit")