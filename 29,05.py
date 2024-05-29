
import argparse # парсер аргументов командной строки 
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
    parser.add_argument("action", type=str, choices=['read', 'write', 'play'])
    # Создание аргумента для имени файла
    parser.add_argument('filepath', type=str)
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