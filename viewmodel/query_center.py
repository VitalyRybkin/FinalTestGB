import re
from contextlib import suppress

from viewmodel.CreateAnimal import Counter, CreateAnimal
from model import db_workout as db
from viewmodel.query_lib import Queries


def get_data(table_name: str,
             column: str = '*',
             search_col: str | None = None,
             param: str | None = None) -> tuple[str, str]:
    get_query = Queries(table_name, column, search_col, param, fields=[], values=[])

    db.db_call(get_query.from_output_queries(table_name))

    show_data = get_query.from_select_queries('select')
    show_headers = f'DESC {table_name}'

    headers, data = db.get_data(show_headers, show_data)

    db.db_call(f'DROP TABLE {table_name}')

    return headers, data


def name_not_found(table: str, search_col: str | None, param: str | None) -> bool:
    """
    Function. Checks if searching parameter (param) exists it evaluated table.
    :param table: table name.
    :param search_col: column of a table to be searched in.
    :param param: parameter to be searched.
    :return: if param found or not (true | false)
    """
    result = list()
    get_query = Queries(table=table, column='*', search_col=search_col, param=param, fields=[], values=[])
    if param is not None:
        result = db.db_call(get_query.from_select_queries('select_where'))

    return True if len(result) == 0 else False


class InterruptWithBlock(Exception):
    """
    Class. Interruption of a with-statement.
    """
    pass


def add_animal() -> None:
    """
    Function. Adds new animal to a database.
    :return: None
    """
    new_animal_added = False
    with Counter() as c:
        with suppress(InterruptWithBlock) as _, CreateAnimal() as add:
            # Adding animal name
            animal_name = input('Enter animal\'s name: ')
            add.animal_name = animal_name

            # Handling animal type.
            get_query = Queries(table='animal_type',
                                column='animal_type_name',
                                search_col=None,
                                param=None,
                                fields=[],
                                values=[])
            types = db.db_call(get_query.from_select_queries('select'))
            types = [item[0] for item in types]
            types_list = ', '.join(types)

            while name_not_found('animal_type',
                                 'animal_type_name',
                                 animal_type :=
                                 input(f'Enter animal\'s type from following [{types_list}] or \'exit\': ')):
                if animal_type == 'exit':
                    raise InterruptWithBlock()
                print(f'Animal type \'{animal_type}\' not in list!')
                if add_to_list(animal_type, 'animal_type', 'animal_type_name'):
                    break

            get_query = Queries(table='animal_type',
                                column='id',
                                search_col='animal_type_name',
                                param=animal_type,
                                fields=[],
                                values=[])
            add.animal_type = db.db_call(get_query.from_select_queries('select_where'))[0][0]

            # Handling animal birthdate.
            date = r'(20[0-2][0-9])(-)(0[0-9]|1[0-2])(-)([0-2][0-9]|3[0-1])'
            while re.match(date, birthdate := input('Enter animals\'s birthdate (yyyy-mm-dd) or \'exit\': ')) is None:
                if birthdate == 'exit':
                    raise InterruptWithBlock()
                print(f'{birthdate} is not valid date!')
            add.animal_birthdate = birthdate

            # Handling animal group.
            get_query = Queries(table='animal_group',
                                column='animal_group_name',
                                search_col=None,
                                param=None,
                                fields=[],
                                values=[])
            groups = db.db_call(get_query.from_select_queries('select'))
            groups = [item[0] for item in groups]
            groups_list = ', '.join(groups)

            while name_not_found('animal_group',
                                 'animal_group_name',
                                 group_type := input(
                                     f'Enter animal\'s group from following [{groups_list}] or \'exit\': ')):
                if group_type == 'exit':
                    raise InterruptWithBlock()
                print(f'Animal group \'{group_type}\' not in list!')
                if add_to_list(group_type, 'animal_group', 'animal_group_name'):
                    break

            get_query = Queries(table='animal_group',
                                column='id',
                                search_col='animal_group_name',
                                param=group_type,
                                fields=[],
                                values=[])
            add.animal_group = db.db_call(get_query.from_select_queries('select_where'))[0][0]

            # Adding new animal to db.
            add_new_animal = input(f'Add new animal to a nursery ['
                                   f'type: {animal_type}, '
                                   f'name: {animal_name}, '
                                   f'birthdate: {birthdate}, '
                                   f'group: {group_type}]? '
                                   f'(y/n) ')
            if add_new_animal.strip().lower() == 'y':
                get_query = Queries(table='animal_group',
                                    column='id',
                                    search_col='animal_group_name',
                                    param=group_type,
                                    fields=[],
                                    values=[])
                add.animal_group = db.db_call(get_query.from_select_queries('select_where'))[0][0]

                new_animal_added = True
                get_query = Queries(table='animals',
                                    column=None,
                                    search_col=None,
                                    param=None,
                                    fields=['animal_type_id', 'animal_name', 'birthdate', 'animal_group_id'],
                                    values=[str(add.animal_type),
                                            f'\'{animal_name}\'',
                                            f'\'{add.animal_birthdate}\'',
                                            str(add.animal_group)])
                db.db_call(get_query.from_insert_queries('insert'))
                print(f'\'{animal_type} {animal_name} {birthdate} {group_type}\' added to a nursery!')
                print('List of animal in nursery - \'show -a\'')
            else:
                raise InterruptWithBlock()

        if new_animal_added:
            c.add()


def add_command() -> None:
    """
    Function. Adds a new command to a commands list.
    :return: None
    """

    # Handling new command.
    while True:
        while not name_not_found('animal_commands_list',
                                 'command_name',
                                 command_name := input('Enter new animal command: ')):
            print(f'\'{command_name}\' command available in a list!')

        headers, query = get_data('commands_list')
        commands_list = [item[0] for item in query]
        if similar := check_similarity(command_name, commands_list):
            print(f'Looks like \'{command_name}\' similar to \'{similar}\'')
            prompt = input('Add anyway? (y/n): ')
            if prompt.lower().strip() == 'y':
                break
        else:
            break

    # Adding new command description.
    description = input('Enter command description: ')
    prompt = input(f'Add \'{command_name}\' to a commands list? (y/n) ')
    if prompt.lower().strip() == 'y':
        get_query = Queries('animal_commands_list',
                            None,
                            None,
                            None,
                            fields=['command_name', 'command_description'],
                            values=[str(f'\'{command_name}\''), str(f'\'{description}\'')])
        db.db_call(get_query.from_insert_queries('insert'))
        print(f'{command_name} successfully added!')
        print('List of commands in nursery - \'show -c\'')
    else:
        print('Interrupted by user!')
        return


def teach_animal() -> None:
    """
    Function. Adds a new command to a commands list.
    :return: None
    """

    # Handling animal to teach new command&
    while name_not_found('animals',
                         'animal_name',
                         animal_name := input('Enter animal\'s name to teach command or \'exit\': ')):
        if animal_name.lower().strip() == 'exit':
            print('Interrupted by user!')
            return
        print(f'\'{animal_name}\' name not found in nursery! (Exit and add animal first - \'add -a\')')
        headers, query = get_data('animals_list')
        animals_list = [item[1] for item in query]
        print(f'... or choose from available animals: \n\t{animals_list}')

    # Getting available commands for chosen animal.
    headers, query = get_data('chosen_animal_commands', param=animal_name)
    animal_commands = [item[0] for item in query]
    if len(animal_commands) == 0:
        print(f'Commands known by \'{animal_name}\' - No commands yet!')
    else:
        print(f'Commands known by \'{animal_name}\' - {animal_commands}')

    headers, query = get_data('commands_list')
    commands_list = [item[0] for item in query]

    available_commands = list(set(commands_list) - set(animal_commands))
    print(f'Available commands for \'{animal_name}\' - {available_commands}')

    # Adding a new command for chosen animal&
    while True:
        while name_not_found('animal_commands_list',
                             'command_name',
                             command_name := input(f'Enter new command for {animal_name} or \'exit\': ')):
            if command_name.lower().strip() == 'exit':
                print('Interrupted by user!')
                return
            print(f'\n\'{command_name}\' not found in commands list!')
            if similar := check_similarity(command_name, animal_commands):
                print(f'... looks similar to \'{similar}\'')
            print(f'... choose from available commands: \n\t{available_commands}')
            print(f'... or exit and add command first - \'add -c\'!\n')

        if command_name in animal_commands:
            print(f'\'{command_name}\' already known by \'{animal_name}\'')
        else:
            break

    # Adding new command for animal to db.
    prompt = input(f'Add \'{command_name}\' for \'{animal_name}\'? (y/n) ')
    if prompt.lower().strip() == 'y':
        get_query = Queries(table='animals',
                            column='id',
                            search_col='animal_name',
                            param=animal_name,
                            fields=[],
                            values=[])
        animal_id = db.db_call(get_query.from_select_queries('select_where'))[0][0]
        get_query = Queries(table='animal_commands_list',
                            column='id',
                            search_col='command_name',
                            param=command_name,
                            fields=[],
                            values=[])
        animal_command_id = db.db_call(get_query.from_select_queries('select_where'))[0][0]
        get_query = Queries('animal_commands',
                            None,
                            None,
                            None,
                            fields=['animal_id', 'animal_command_id'],
                            values=[str(animal_id), str(animal_command_id)])
        db.db_call(get_query.from_insert_queries('insert'))
        print(f'\'Command {command_name}\' now known by \'{animal_name}\'!')
        print('List of commands known by animal - \'show -a -n [name]\'')
    else:
        print('Interrupted by user!')


def check_similarity(command, commands) -> str:
    """
    Function. Checks if there is a similar command in a commands list.
    :param command: command to be checked.
    :param commands: list of commands to be evaluated.
    :return: similar command from a list of commands.
    """
    for item in commands:
        if command in item:
            return item


def add_to_list(value: str, *args) -> bool:
    """
    Function. Adds new row to a db table.
    :param value: value to be added to db.
    :param args: parameters of sql query (table, field, etc.)
    :return: True if added
    """
    added = False
    add_type = input(f'Add \'{value}\' to list? (y/n) ')
    if add_type.lower().strip() == 'y':
        added = True
        get_query = Queries(args[0],
                            None,
                            None,
                            None,
                            fields=[args[1]],
                            values=[f'\'{value}\''])
        db.db_call(get_query.from_insert_queries('insert'))
        print(f'\'{value}\' successfully added!')

    return added
