from database.connection import get_connection


class DatabaseTransaction:

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = get_connection()
        self.connection.start_transaction()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()