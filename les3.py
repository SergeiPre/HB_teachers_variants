def my_pow(a: float) -> float:

    return a ** 2


def my_map(func, temp):
    for itm in temp:
        print("START")
        yield func(itm)
        print('YELD 1 DONE')
        yield func(itm) + 15
        print('CYCLE DONE')
    return None


def my_func(a):
    a += 1

    return lambda x: x + a


def my_except():
    num = 22
    while True:
        try:
            a = int(input('Введите число'))
            result = num / a
            print(type(a), a)
            return result
        except ValueError as error:
            print(error)
            print('ТУТ КОД ОБРАБОТКИ ОШИБКИ')
            continue
        except ZeroDivisionError:
            result = 0
            return result
        finally:
            print('ВЫПОЛНИТСЯ ВСЕГДА')


def my_func2(temp: list) -> float:
    temp.append(2345)
    print(temp)
    return sum(temp)


def func3(a, b, c, d):
    return sum((a, b, c, d))


a = (1, 2, 3, 4, 5)
print(a)

m_d = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 5,
}


def my_max(*args, **kwargs):
    print('KWARGS', type(kwargs))
    print(kwargs)
    print('ARGS', type(args))
    result = float('inf') * -1
    for itm in args:
        if result < itm:
            result = itm
    return result


m_l = [2, 3, 4, 5, 4, 5, 5, 6]
# result = my_max(1, 2, 3, 4, 5, 22, 66, 1, 3, 77, 87, 222, 33, key=my_pow)
#
# print(result)

# def print(*args, **kwarg):
#     pass

# a, b, c, *d = input('HELLO').split(' ')

