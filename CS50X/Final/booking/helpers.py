import sqlite3
from sqlite3 import Error


class SQL:
    def __init__(self, path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

    def do(command):
        cursor.execute(command)
