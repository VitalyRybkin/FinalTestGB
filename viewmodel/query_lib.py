class Queries:
    """
    Class. Collection of database queries.
    """

    def __init__(self, table: str, column: str | None, search_col: str | None, param: str | None, *args, **kwargs):
        self.__output_queries = {
            'animals_list': f'''
                        CREATE TABLE {table} AS
                        SELECT tp.animal_type_name, animal.animal_name, animal.birthdate, grp.animal_group_name 
                        FROM animals animal
                        JOIN animal_type tp ON animal.animal_type_id = tp.id
                        JOIN animal_group grp ON animal.animal_group_id = grp.id''',
            'commands_list': f'''
                        CREATE TABLE {table} AS
                        SELECT command_name, command_description
                        FROM animal_commands_list''',
            'animals_and_commands': f"""
                        CREATE TABLE {table} AS
                        SELECT a.animal_type_name, a.animal_name, acl.command_name 
                        FROM animal_commands ac
                        JOIN 
                            (SELECT animal_type.animal_type_name, a.id, a.animal_name 
                            FROM animals a 
                            JOIN animal_type ON animal_type.id = a.animal_type_id) a ON ac.animal_id = a.id
                        JOIN animal_commands_list acl ON ac.animal_command_id = acl.id
                        ORDER BY a.animal_type_name""",
            'chosen_animal_commands': f"""
                        CREATE TABLE {table} AS
                        SELECT acl.command_name 
                        FROM animal_commands ac 
                        JOIN animal_commands_list acl ON ac.animal_command_id = acl.id
                        JOIN animals a ON a.id = ac.animal_id
                        WHERE a.animal_name = \'{param}\'""",
            'chosen_command_animals': f"""
                        CREATE TABLE {table} AS
                        SELECT a.animal_name 
                        FROM animal_commands ac 
                        JOIN animal_commands_list acl ON ac.animal_command_id = acl.id
                        JOIN animals a ON a.id = ac.animal_id
                        WHERE acl.command_name = \'{param}\'"""
        }
        self.__select_queries = {
            'select': f'SELECT {column} FROM {table}',
            'select_where': f'SELECT {column} FROM {table} WHERE {search_col} = \'{param}\''
        }
        self.__values = ', '.join(kwargs.get('values'))
        self.__columns = ', '.join(kwargs.get('fields'))
        self.__insert_queries = {
            # 'one_filed_insert': f'INSERT INTO {table} '
            #                     f'({self.__columns}) '
            #                     f'VALUES (\'{kwargs.get("field_1")}\')',
            'insert': f'INSERT INTO {table} '
                      f'({self.__columns}) '
                      f'VALUES ({self.__values})'
        }

    @property
    def get_output_queries(self) -> dict:
        return self.__output_queries

    def from_output_queries(self, key) -> str:
        return self.get_output_queries.get(key)

    @property
    def get_select_queries(self) -> dict:
        return self.__select_queries

    def from_select_queries(self, key) -> str:
        return self.__select_queries.get(key)

    @property
    def get_insert_queries(self):
        return self.__insert_queries

    def from_insert_queries(self, key):
        return self.__insert_queries.get(key)
