import mysql.connector
from mysql.connector import Error

from config import DATABASE_CONFIG


def get_connection():
    try:
        connection = mysql.connector.connect(
            **DATABASE_CONFIG
        )

        if connection.is_connected():
            return connection

        raise ConnectionError("Gagal terhubung ke database.")

    except Error as error:
        raise ConnectionError(
            f"Gagal terhubung ke MySQL: {error}"
        ) from error