import requests


my_requests = requests.get('https://www.python.org')
# print(my_requests)
print(my_requests.text)
print(my_requests.status_code)


# pip list - установленные пакеты
# сайт pypi.org - все пакеты python


# ###Создание виртульной среды
# В папке проекта создаем папку .venv
# Далее устанавливаем необходимые пакеты с помощью pipenv install (requests) - например
# Чтобы перейти в шел виртуального окружения вводим pipenv shell


# > [! tip]
# > Резюмируя, имея файлы Pipfile и Pipfile.lock можно создать точную копию виртуального окружения командой pipenv install только нужно заранее создать папку в корне проекта .venv
