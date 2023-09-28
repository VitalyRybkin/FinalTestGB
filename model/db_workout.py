from typing import Sequence

from mysql.connector import connect, Error


def get_data(headers_list, data_query):
    data = db_call(data_query)
    headers = db_call(headers_list)

    return headers, data


def db_call(query: str) -> Sequence:
    """
    Function. Connect to database and handle an sql query.
    :param query: sql query string.
    :return: list of tuples.
    """
    result = None
    try:
        with connect(
                host='localhost',
                user='root',
                password='',
                database='HumanFriends'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                connection.commit()
    except Error as e:
        print(e)

    return result
