def num_to_array(num):
    arr = []
    while num > 0:
        arr.append(num % 10)
        num //= 10
    arr.reverse()
    return arr


def task_1():
    num = int(input())
    arr = num_to_array(num)
    summa = 0
    for i in arr:
        if i < max(arr):
            summa += i
    print(summa)
    return 0


def task_2():
    num = int(input())
    count = 0
    for i in range(1000, num):
        if num_to_array(i)[0] + num_to_array(i)[len(num_to_array(i)) - 1] > max(num_to_array(i)):
            count += 1
    print(count)
    return 0


def task_3_1():
    N = int(input())
    num_b = int(bin(N + 1).replace('0b', ''))
    num_o = int(oct(N + 1).replace('0o', ''))
    while sum(num_to_array(num_b)) < max(num_to_array(num_o)):
        N += 1
        num_b = int(bin(N).replace('0b', ''))
        num_o = int(oct(N).replace('0o', ''))
    print(N)
    return 0


def task_3_2():
    N = int(input()) + 1
    if N == 2: N += 1 # Я не придумал как исправить неработоспособность программы без этого костыля
    num_b = int(bin(N).replace('0b', ''))
    while True:
        if sum(num_to_array(num_b)) > max(num_to_array(N)):
            print(N)
            break
        N += 1
    return 0


def task_4():
    num = int(input())
    t_num = num
    summa = 0
    while t_num > 0:
        if t_num % 10 < max(num_to_array(num)):
            summa += t_num % 10
        t_num //= 10
    print(summa)
    return 0


def task_5():
    num = int(input())
    count = 0
    for i in range(1000, num + 1):
        if num_to_array(i)[0] + num_to_array(i)[len(num_to_array(i)) - 1] > max(num_to_array(i)):
            count += 1
    print(count)
    return 0


def task_6():
    N = int(input()) + 1
    if N == 2: N += 1 # Я не придумал как исправить неработоспособность программы без этого костыля
    num_b = int(bin(N).replace('0b', ''))
    while True:
        if sum(num_to_array(num_b)) > max(num_to_array(N)):
            print(N)
            break
        N += 1
    return 0


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3_1()
    # task_3_2()
    # task_4()
    # task_5()
    task_6()
    pass
