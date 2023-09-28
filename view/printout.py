import datetime

from view.headers_lib import Headers


def print_db_query(headers: str, query: str) -> None:
    """
    Function. Data output from queries to console.
    :param headers: get column headers from query.
    :param query: data from database query.
    :return: None
    """
    if len(query) == 0:
        print('Nothing\'s here, yet!')
        return
    col_widths = count_max_column_width(query)
    header_name = Headers()
    table_width = sum(col_widths) + len(col_widths) * 7 + 1

    print('-' * table_width)
    for index, header in enumerate(headers):
        if header[0] in header_name.all_headers():
            print(f'| {header_name.get_header(header[0]):<{col_widths[index] + 5}}', end='')
    print('|')
    print('-' * table_width)

    for data in query:
        for index, item in enumerate(data):
            if isinstance(item, datetime.date):
                item = item.strftime('%m-%d-%Y')
            print(f'| {item:<{col_widths[index] + 5}}', end='')
        print('|')
    print('-' * table_width)


def count_max_column_width(query: str) -> list:
    """
    Function. Counts max length of a single string from a database query to count max width of each column to be printed
    out to console.
    :param query: database data from query.
    :return: list of max lengths of strings to be printed to console
    """
    max_width = [0 for _ in query[0]]
    for data in query:
        for index, item in enumerate(data):
            if isinstance(item, datetime.date):
                item = item.strftime('%m-%d-%Y')
            if len(item) > max_width[index]:
                max_width[index] = len(item)
    return max_width


def print_help(commands: dict, options: dict) -> None:
    """
    Function. Prints out user help instructions.
    :param commands: commands dict.
    :param options: options dict.
    :return: None
    """
    print('Usage: command -option ... -option [name]')
    print('Commands:')
    for k, v in commands.items():
        print(f'\t{k:<8} {v}')

    print('Options:')
    for k, v in options.items():
        print(f'\t{k:<8} {v}')
    print()

    print('Examples:')
    print('\t\'show -a\' - list of animals;')
    print('\t\'show -c\' - list of animals commands;')
    print('\t\'show -a -n [name]\' - list of chosen animal commands;')
    print('\t\'add -a -c\' - teach animal to a command from list;')
    print('\t\'add -c\' - add command to commands list;')
