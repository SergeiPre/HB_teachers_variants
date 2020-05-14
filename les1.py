# PEP8
# name = input('Ваше имя?\n')


while True:
    age = input('Возраст число\n')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Неверный ввод повторите')

print(age)
#
# this_year = 2020
#
# while age:
#     if age == 10:
#         age -= 1
#         continue
#     print(age)
#     age -= 1
# else:
#     print('сработал ELSE')
#
# print('завершили')
#


# if age.isdigit():
#     age = int(age)
#     b_year = this_year - age
#     print(b_year)
#
#     while True:
#         if not age:
#             break
#         elif age == 10:
#             age -= 1
#             continue
#         print(age)
#         age -= 1
#
#         # age = age - 1
#
#     # if age >= 18:
#     #     print("Вам можно во все разделы")
#     # elif age == 16:
#     #     print('Можно посмотреть ограниченый контент')
#     # elif (age <= 12) and age > 8:
#     #     print('Вот тебе ссылка на мультики')
#     # elif 12 >= age > 8:
#     #     print('Вот тебе ссылка на мультики')
#     # else:
#     #     print("Нет смылса что-то печатать, ты не умеешь читать")
#
# else:
#     print('Неверный возраст')
