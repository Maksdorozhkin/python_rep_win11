# работа с аргументами программы с помощью модуля sys (как внутри программы python получить доступ к аргументам с которыми программа была запущена)

import sys

print(sys.argv)

if len(sys.argv) < 3:
    raise IOError("You must provide username and password")

# username = sys.argv[1]
# password = sys.argv[2]

filename, username, password = sys.argv

# print(username, password)
