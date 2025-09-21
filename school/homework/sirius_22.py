"""
Задания из 21 урока "Сириуса"
"""


def task_1():
    num = int(input())
    min_num = 10
    while num > 0:
        if num % 10 < min_num and (num % 10) % 3 == 0 and not num % 10 == 0:
            min_num = num % 10
        num //= 10
    print('NO' if min_num == 10 else min_num)
    return 0


def task_2():
    num = int(input())
    min_num = 10
    while num > 0:
        if num % 10 < min_num and (num % 10) > 3 and not num % 10 == 3:
            min_num = num % 10
        num //= 10
    print('NO' if min_num == 10 else min_num)
    return 0


def task_3():
    num = int(input())
    count = 0
    while num > 0:
        if (num % 10) % 3 == 0 and num % 10 != 0:
            count += 1
        num //= 10
    print(count if count > 0 else 'NO')
    return 0


def task_4():
    num = int(input())
    k = 0
    is_ok = True
    while num > 0:
        if float(num // 4) == num / 4:
            k += 1
            num //= 4
        else:
            is_ok = False
            break
        if num == 1:
            break
    print(k if is_ok else 'NO')
    return 0


def task_5():
    num = int(input())
    summa = 0
    while num > 0:
        if not (num % 10) % 3 == 0:
            summa += num % 10
        num //= 10
    print(summa if summa != 0 else 'NO')
    return 0


def task_6():
    num = int(input())
    arr = []
    while num > 0:
        if num % 10 < 5: arr.append(num % 10)
        num //= 10
    print(min(arr) if len(arr) > 0 else 'NO')
    return 0


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    task_6()
    pass
