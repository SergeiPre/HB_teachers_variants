# import sys
# from my_lib.my_module import r_sum
#
# print(sys.argv)
#
# _, *vars = sys.argv
#
# tmp = [int(itm) for itm in vars if itm.isdigit()]
# print(r_sum([int(itm) for itm in vars if itm.isdigit()]))


# temp = []
# for itm in vars:
#     if itm.isdigit():
#         temp.append(int(itm))


# print(tmp)
# print(r_sum([]))

# def my_f(n):
#     tmp = 0
#     while tmp != n:
#         yield tmp ** 2
#         tmp += 1
#
#
# for itm in my_f(2):
#     print(itm)

#
# def deco(func, x=1):
#     def wrap(*args, **kwargs):
#         print(args, kwargs)
#         result = func(*args, *kwargs)
#         print('end')
#         return result
#
#     return wrap
#
#
# @deco
# def my_sum(a, b):
#     return a + b
#
#
# # deco_func = deco(my_sum)
#
# print(my_sum(a=1, b=3))
# tmp = 2
#
#
# def my_gen(n):
#     while n:
#         yield n
#         n -= tmp
#     return None
#
#
# print(tmp)
# for itm in my_gen(3):
#     print(itm)
# print('#' * 30)
# print(tmp)


# class Myob:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         return Myob(self.x + other.x)
#
#     def __str__(self):
#         return str(self.x)

# result = []
# for itm in range(10):
#     if itm & 1:
#         result.append(itm)
from typing import List
from statistics import mean
from functools import reduce

data: int = 111


def my_f() -> List[int, float]:
    prev = [None]

    def hello(trade):
        if prev[0]:
            result = trade + prev[0]
            prev[0] = trade
            return result

    return hello


def f(a: list):
    a.append(2222)


a = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

tmp = list(map(lambda x: x ** 2, a))
print(tmp)
