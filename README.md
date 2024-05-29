# 27.05.py


## Описание
Этот скрипт поможет вам для работы с файлами конфигурации. Дает возможность записывать, изменять настройки в файле конфигурации
## Как запустить
 - python 27.05.py write  config.json --param server.port=2000

## Содержание
- 27.05.py - скрипт с основным функционалом
### Функции 27.05.py
- read_config(путь к файлу): Эта функция принимает путь к файлу в качестве входных данных и считывает данные JSON из файла. Затем она возвращает обработанные данные JSON.

-  write_config(путь к файлу, конфигурация): Эта функция принимает путь к файлу и объект конфигурации в качестве входных данных и записывает данные конфигурации в указанный файл в формате JSON.

-  update_config(конфигурация, параметр, значение): Эта функция принимает в качестве входных данных объект конфигурации, путь к параметру и новое значение. Она обновляет указанный параметр в объекте конфигурации новым значением.
## Используемые модули
- argparse - Модуль предназначен для обработки аргументов командной строки.
Он позволяет создавать интуитивно понятные интерфейсы для работы с командами и опциями, что является важным аспектом при создании полноценных приложений.

- json - JSON (JavaScript Object Notation) — это легковесный формат обмена данными. Он основан на языке программирования JavaScript, но может использоваться в Python и Perl. В основном его применяют для передачи данных между сервером и веб-приложением.


## Автор 
 Бекмамат Жаныбаев
 https://github.com/Bekmama
