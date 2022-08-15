# Проект парсинга pep
### Описание
Были написаны три парсера, путь до основого файла - src/main.py. Настроено логирование и обработка исключений. Функции программы и режимы парсера запускаются через аргументы командной строки.
### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/FedyaevaAS/bs4_parser_pep
cd bs4_parser_pep/
```
Cоздать и активировать виртуальное окружение:
```
py -m venv env
```
Установить зависимости из файла requirements.txt:
```
py -m venv env
```
Перейти в директорию с основным файлом
```
cd src/
```
### Примеры запуска парсера из командной строки
Запуск парсера pep без очистки кеша и выводом данных в файл
```
py main.py pep --output file
```
Запуск парсера whats-new с очисткой кеша и выводом данных в терминал в табличном виде
```
py main.py whats-new --clear-cache --output pretty
```
### Автор
Федяева Анастасия