from databaseConnection import DatabaseConnection


class Database:
    def __init__(self):
        db_connection = DatabaseConnection()
        self.engine = db_connection.get_engine()

    def import_to_database(self, df, name):
        try:
            df.to_sql(name=name, con=self.engine, if_exists="append", index=False)
        except ValueError:
            print("Already Exists")
