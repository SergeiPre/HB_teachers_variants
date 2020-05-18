"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ('зима',
                'весна',
                'лето',
                'осень',
                )

seasons_dict = {'зима': (12, 1, 2),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11),
                }

user_month_num = 12

season_idx = user_month_num // 3 % 4

for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break

print(season_idx)
print(seasons_list[season_idx])
