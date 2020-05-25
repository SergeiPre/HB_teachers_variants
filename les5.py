# import json

# file = open('input.txt', 'r', encoding='UTF-8')
# try:
#     print(file.read())
# except IOError:
#     print('ОШТБКА')
# finally:
#     file.close()
#
# with open('output1.txt', 'wb') as out_file:
#     content = bytes('HELOO MY DEAR FRENDS, ЭТО БАЙТОВАЯ СТРОКА', encoding='UTF-8')
#     print(content)
#     out_file.write(content)

#
# data = {
#     'key1': [1, 2, 3],
#     'key2': True,
#     'key3': None,
#     'key4': 'HELLO МИР"',
#     "key5": (1, 2, 3, 4),
#     'key6': {'key1': [1, 2, 3],
#              'key2': True,
#              'key3': None, },
#
# }
#
# a = data['key6']['key1'][0]
# print(a)
# new_data = [data, data]
#
# j_data = json.dumps(new_data, ensure_ascii=False)
#
# print(j_data)
#
# with open('j_data.json', 'r') as j_file:
#     print(json.load(j_file))

import os

# print(os.listdir('.'))
# print(os.path.isdir('env22'))
dir_path_root = os.path.dirname(__file__)

file_name = 'output1.txt'

full_path = os.path.join(dir_path_root, file_name)

# os.rename(full_path, 'new_name.txt')

# with open(full_path, 'r') as in_file, open('new_copy.txt', 'w') as cop_file:
#     cop_file.write(in_file.read())
#
# print(os.path.exists(full_path))
#
# import shutil
#
# shutil.copy(full_path, 'new_cop.txt')

# import sys
#
#
# print(sys.path)

import requests

response = requests.get('https://api.github.com/users/gefmar')
data = response.json()
print(data['login'])
