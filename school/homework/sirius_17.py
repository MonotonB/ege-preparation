"""
Задания из 17 урока "Сириуса"
"""

# from math import pow


def task_2():
    a, b = map(int, input().split())
    print(3 * pow((a + b), 3) + 275 * pow(b, 2) - 127 * a - 41)
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


def task_5():
    number = int(input())
    numbers = []
    for i in range(4):
        numbers.append(str(number % 10))
        number //= 10
    print(numbers[2] + numbers[3] + numbers[0] + numbers[1])
    return 0


def task_6():
    # M, N, P = map(int, input().split()) # На платформе не работает ввод в одну строку
    M = int(input())
    N = int(input())
    P = int(input())
    print(f"{(M + (N + P) // 60) % 24} ч {(N + P) % 60} мин")
    return 0


if __name__ == "__main__":
    # print("task num 2")
    # task_2()
    # print("task num 3")
    # task_3()
    # print("task num 4")
    # task_4()
    # print("task num 5")
    # task_5()
    print("task num 6")
    task_6()
    # input("press enter to exit")