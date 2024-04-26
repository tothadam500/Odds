from sqlalchemy import create_engine
import psycopg2 as pg2
from data import database


class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.engine = None
        self.database_name = database['database_name']
        self.username = database['username']
        self.password = database['password']

        self.connect()

    def connect(self):
        try:
            self.conn = pg2.connect(database=self.database_name, user=self.username, password=self.password)
            self.engine = create_engine(
                f'postgresql://{self.username}:{self.password}@localhost:5432/{self.database_name}')
            print("Connection established successfully!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def get_engine(self):
        return self.engine
