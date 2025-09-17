def task_1():
    psw1 = input()
    psw2 = input()
    print('Пароль принят' if psw1 == psw2 else 'Ошибка ввода')
    return 0


def task_2():
    num = int(input())
    array = []
    while num > 0:
        array.append(num % 10)
        num //= 10
    array.reverse()
    print(True if (array[0] + array[3]) == (array[1] - array[2]) else False)
    return 0


def task_3():
    year = int(input())
    print(True if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0 else False)
    return 0


def task_4():
    string = input()
    print(True if ('н' in string and 'г' in string and 'д' in string) else False)
    return 0


def task_5():
    print(True if int(input()) % 100 == 0 else False)
    return 0


def task_6():
    x1, y1, x2, y2 = map(int, input().split())
    print(True if (x1 % 2 == x2 % 2) and (y1 % 2 == y2 % 2) else False)
    return 0


def task_7():
    age = int(input())
    gender = input()
    print(True if (gender == 'f') and (10 <= age <= 15) else False)
    return 0


def task_8():
    num = int(input())
    if not num % 2 == 0:
        print('YES')
    elif 2 <= num <= 5:
        print('NO')
    elif 6 <= num <= 20:
        print('YES')
    else:
        print('NO')
    return 0


def task_9():
    weight = int(input())
    if weight <= 69:
        if weight <= 64:
            if weight <= 60:
                print(1)
                return 0
            print(2)
            return 0
        print(3)
        return 0
    else:
        print(4)
        return 0


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    task_9()
