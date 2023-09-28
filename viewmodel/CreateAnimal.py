from model import db_workout as db


class CreateAnimal:
    def __init__(self):
        self.__name = None
        self.__type = None
        self.__birthdate = None
        self.__group = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not all([bool(self.animal_name),
                    bool(self.animal_group),
                    bool(self.animal_birthdate),
                    bool(self.animal_type)]):
            print('Interrupted by user!')

    @property
    def animal_name(self):
        return self.__name

    @animal_name.setter
    def animal_name(self, name):
        self.__name = name

    @property
    def animal_type(self):
        return self.__type

    @animal_type.setter
    def animal_type(self, type_id):
        self.__type = type_id

    @property
    def animal_group(self):
        return self.__group

    @animal_group.setter
    def animal_group(self, group):
        self.__group = group

    @property
    def animal_birthdate(self):
        return self.__birthdate

    @animal_birthdate.setter
    def animal_birthdate(self, date):
        self.__birthdate = date


class Counter:
    animal_counter = len(db.db_call('SELECT * FROM animals'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def add(self):
        self.animal_counter += 1
