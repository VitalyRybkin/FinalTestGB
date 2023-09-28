
class Headers:
    """
    Class. Collection of database columns and their names to be printed out to console.
    """

    def __init__(self):
        self.__col_headers = {
            'animal_type_name': 'Type',
            'animal_name': 'Name',
            'birthdate': 'Birthdate',
            'animal_group_name': 'Group',
            'command_name': 'Command',
            'command_description': 'Description'
        }

    @property
    def get_headers(self) -> dict:
        return self.__col_headers

    def get_header(self, key) -> str:
        return self.get_headers.get(key)

    def all_headers(self) -> dict:
        return self.get_headers
