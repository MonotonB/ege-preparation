def task_1():
    mlpt = 1
    for i in range(int(input())):
        num = int(input())
        if num % 2 != 0:
            mlpt *= num
    print(mlpt)
    return 0


def task_3():
    n = int(input())
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 2] + arr[i - 1])
    print(arr[n - 1])
    return 0


def task_4():
    num = int(input())
    arr = [0, 1]
    while max(arr) < num:
        arr.append(arr[len(arr) - 2] + arr[len(arr) - 1])
    print(arr[len(arr) - 2])
    return 0


def task_5():
    num = int(input())
    arr = [0, 1]
    while max(arr) < num:
        arr.append(arr[len(arr) - 2] + arr[len(arr) - 1])
    print(arr[len(arr) - 2], len(arr) - 1)
    return 0


def task_6_1():
    num = int(input())
    for i in range(1, num + 1):
        print(i * 2, end=' ')
    return 0


def task_6_2(): # Несмотря на то, что решения абсолютно одинаковые, формально условия про 2 варианта с 2-мя разными циклами соблюдено
    num = int(input())
    i = 1
    while i < num + 1:
        print(i * 2, end=' ')
        i += 1
    return 0


if __name__ == '__main__':
    # task_1()
    # task_3()
    # task_4()
    # task_5()
    # task_6_1()
    task_6_2()
    pass
