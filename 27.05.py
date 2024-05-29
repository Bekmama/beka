
import argparse
import json
# DONE: Читать файл конфига и выводить
# DONE: Открывать файл и менять настройку(ки)
# DONE: Написать документацию
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
    keys = param.split(':')#путь к параметру
    data = config
    for key in keys[:-1]:# Проходим по всем ключам кроме последнего
    # Переход на следующий уровень сложности, если ключа нет то создаем пустой словарь
        data = data.setdefault(key, {})
    data[keys[-1]] = value# Устанавливаем новое значение для последнего ключа
# server.host=4.567.8

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Работа с файлом конфигурации")
    # Создание аргумента для выбора действия
    parser.add_argument('action', type=str, choices=['read', 'write'], help='Действие: read или write')
    # Создание аргумента для имени файла
    parser.add_argument('filepath', type=str, help='Путь к файлу конфигурации')
    parser.add_argument('--param', type=str, help='Параметр и значение для этого параметра в формате: key.subkey=value (Только для действия Write)')
    # Парсинг аргументов и сохранение в args
    args = parser.parse_args()

    if args.action == 'read':
        config_data = read_config(args.filepath)
        print(json.dumps(config_data, indent=3))
    elif args.action == 'write':
        config_data = read_config(args.filepath)
        path, value = args.param.split('=')
        update_config(config_data, path, value)
        write_config(args.filepath, config_data)
        
        
if __name__ == "__main__":
    main()