
from view.printout import print_help, print_db_query
from viewmodel import query_center as queries


def run_nursery() -> None:
    """
    Function. Handles commands from user input.
    :return: None
    """
    n_parameter = ''

    commands = {'show': '- list of nursery animals;',
                'add': '- add animal to nursery;',
                'change': '- change animal info;',
                'help': '- list of commands;',
                'exit': '- exit nursery;'}

    options = {'-a': '- animals;',
               '-c': '- commands;',
               '-n': '- animal|command name;'}

    print_help(commands, options)
    print()

    while True:
        comm_list = list()
        opt_list = list()

        for k, v in commands.items():
            comm_list.append(k)

        for k, v in options.items():
            opt_list.append(k)

        user_input = input(f'Enter command {comm_list} and option {opt_list}: ')
        if not user_input.find(' -n') == -1:
            res = user_input.strip().split()
            n_parameter = res.pop()
            res = [i.lower() for i in res]
            user_input = " ".join(res)
        else:
            user_input = " ".join(user_input.lower().strip().split())

        match user_input:
            case 'show -c':
                headers, query = queries.get_data('commands_list')
                print_db_query(headers, query)
            case 'show -a':
                headers, query = queries.get_data('animals_list')
                print_db_query(headers, query)
            case 'show -a -c':
                headers, query = queries.get_data('animals_and_commands')
                print_db_query(headers, query)
            case 'show -a -n':
                if queries.name_not_found('animals', 'animal_name', n_parameter):
                    print(f'No such animal - \'{n_parameter}\'')
                else:
                    print(f'Commands known by {n_parameter}:')
                    headers, query = queries.get_data('chosen_animal_commands', param=n_parameter)
                    print_db_query(headers, query)
            case 'show -c -n':
                if queries.name_not_found('animal_commands_list', 'command_name', n_parameter):
                    print(f'No such command - \'{n_parameter}\'')
                else:
                    print(f'\'{n_parameter}\' known by following animals:')
                    headers, query = queries.get_data('chosen_command_animals', param=n_parameter)
                    print_db_query(headers, query)
            case 'add -a':
                queries.add_animal()
            case 'add -c':
                queries.add_command()
            case 'add -a -c':
                queries.teach_animal()
            case 'change -c':
                pass
            case 'change -a':
                pass
            case 'help':
                print_help(commands, options)
            case 'exit':
                exit()
            case _:
                print(f'Achtung! Wrong command \'{user_input}\'! Try again!')
