
'''import argparse # парсер аргументов командной строки 
import json
from textwrap import indent

# DONE: Читать файл конфига и выводить
# TODO: Открывать файл и менять настройку(ки)
# TODO: Написать документацию
# TODO: Написать README

def read_config(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Работа с фйлом конфигурации")
    # Создание аргумента для выбора действия
    parser.add_argument('action', type=str, choices=['read', 'write', 'play'])
    # Создание аргумента для имени файла
    parser.add_argument('filepath', type=str)
    #создание аргумента для параметра   
    

    # Парсинг аргументов и сохранение в args
    args = parser.parse_args()

    

    if args.action == 'read':
        config_data=read_config(args.filepath)
        print(json.dumps(config_data, indent=3))
    elif args.action == 'write':
        print('write')
    elif args.action == 'play':
        print('play')

if __name__=="__main__":
    main()



def update_config(config, param,value):
    keys = param.split(":")    #путь к параметру 
    r = config
    for key in keys: #проходим по всем ключам кроме последнего 
        #перход на след уровень вложености , если ее нет то создает пустой словарь
        data = config.setdefault(key,{})
    data [keys[-1]] = value #устанавливает новое значение для последнего ключа

def write_config(filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump('config' , f, indent= 2)
'''




import argparse # парсер аргументов командной строки 
import json
from textwrap import indent

# DONE: Читать файл конфига и выводить
# DONE: Открывать файл и менять настройку(ки)
# TODO: Написать документацию
# TODO: Написать README

def read_config(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Запись конфига в файл
def write_config(filepath, config):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

# Изменение параметра в конфиге
def update_config(config, param, value):
    keys = param.split(':') #путь к параметру 
    for key in keys: # Проходим по всем ключам кроме последнего
        # Переход на следующий уровень сложности, если ключа нет то создаем пустой словарь
        data =config.setdefault(key, {})
    data[keys[-1]]= value # Устанавливаем новое значение для последнего ключа
# server.host=4.567.8

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Работа с фйлом конфигурации")
    # Создание аргумента для выбора действия
    parser.add_argument('action', type=str, choices=['read', 'write'])
    # Создание аргумента для имени файла
    parser.add_argument('filepath', type=str)
    #
    parser.add_argument('--param', type=str)
    # Парсинг аргументов и сохранение в args
    args = parser.parse_args()

    if args.action == 'read':
        config_data=read_config(args.filepath)
        print(json.dumps(config_data, indent=3))
    elif args.action == 'write':
        path, value = args.param.split('=')
        update_config(config_data, path, value)
        write_config(args.filepath, config_data)
        # server.host=5.4.3.5

if __name__=="__main__":
    main()