import sqlite3
import datetime as dt
from pathlib import Path
from typing import Union


class Db:
    """Stores the categories and timer records in an SQLite database"""

    DATE_FORMAT = '%Y-%m-%d'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    conn = None

    def __init__(self, db_path: Union[str, Path] = '') -> None:
        self._db_path = str(db_path)
        if db_path:
            self.__connection()

    def __del__(self):
        """Clean up after ourselves on exit"""
        if self.conn:
            self.conn.close()

    @property
    def db_path(self) -> str:
        return self._db_path

    @db_path.setter
    def db_path(self, path: str) -> None:
        self._db_path = path
        self.__connection()

    ## SQL basics
    def __connection(self):
        """Connect to the database"""
        if not self.db_path:
            raise Exception("Database path not set")

        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        # Return rows as dictionaries
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    def execute(self, sql: str) -> None:
        '''Execute a SQL statement'''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def query(self, sql: str) -> list:
        '''Execute a query and return the results as a list of dictionaries'''
        cur = self.conn.cursor()
        cur.execute(sql)
        data = [dict(x) for x in cur.fetchall()]
        cur.close()
        return data

    def queryOne(self, sql: str) -> list:
        '''Execute a query and return the results as a list of dictionaries'''
        cur = self.conn.cursor()
        cur.execute(sql)
        data = [dict(x) for x in cur.fetchall()]
        cur.close()
        if len(data) == 1:
            return {**data[0]}
        if len(data) == 0:
            return None
        if len(data) > 1:
            raise Exception("More than one record returned")

    
    # Helper functions, 

    def insert(self, table: str, data: dict) -> None:
        '''Insert a record into a table from a dictionary
            - The dictionary keys must match the table field names
            - The dictionary values must be the correct type for the field
        '''
        fields = ''
        values = '' 
        for field, value in data.items():
            fields += f"{field}, "
            if isinstance(value, str):
                values += f"'{value.replace("'","''")}', "
            elif isinstance(value, dt.date):
                values += f"'{value.strftime(self.DATE_FORMAT)}', "
            elif isinstance(value, dt.datetime):
                values += f"'{value.strftime(self.DATETIME_FORMAT)}', "
            elif isinstance(value, bool):
                values += f"{int(value)}, "
            elif value == None:
                values += "NULL, "
            else:
                values += f"{value}, "
        fields = fields[:-2] # Remove trailing comma and space
        values = values[:-2] # Remove trailing comma and space

        sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"
        self.execute(sql)

    def create_table(self, table_name:str, fields:str) -> None:
        """Creates a table if it doesn't exist"""
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def drop_table(self, table_name:str) -> None:
        """Drops a table if it exists"""
        sql = f"DROP TABLE IF EXISTS {table_name}"
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def get_table_fields(self, table_name:str) -> list:
        """Returns a list of the fields in a table"""
        sql = f"PRAGMA table_info({table_name})"
        cur = self.conn.cursor()
        cur.execute(sql)
        data = [dict(x) for x in cur.fetchall()]
        cur.close()
        return data
    
    def get_table_names(self) -> list:
        """Returns a list of the tables in the database"""
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        cur = self.conn.cursor()
        cur.execute(sql)
        data = [x[0] for x in cur.fetchall()]
        data.remove('sqlite_sequence')
        cur.close()
        return data
    

db = Db('gastroTrack.db')