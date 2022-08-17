import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_OUTPUT_FORMAT


type_output_dict = {
    'pretty': lambda x: pretty_output(x),
    'file': lambda x, y: file_output(x, y),
    None: lambda x: default_output(x)
}


def control_output(results, cli_args):
    output = cli_args.output
    value = type_output_dict[output]
    argcount = value.__code__.co_argcount
    if argcount == 1:
        value(results)
    else:
        value(results, cli_args)


def default_output(results):
    for row in results:
        print(*row)


def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_OUTPUT_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
