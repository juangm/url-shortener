import sqlite3


class Sqlite3Helper:

    _DB = "sqlite/url-short.db"

    def __init__(self):
        self.conn = None

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(self._DB)
            return self.conn
        except sqlite3.Error as e:
            print(e)

    def execute_sql(self, sql_statement):
        """ execute sql statement in
        :sql_statement sql statement to be executed
        """
        try:
            return self.conn.cursor().execute(sql_statement)
        except sqlite3.Error as e:
            print(e)

    def setup_db(self):
        """ Create a table in DB for URl shortener """
        sql_create_urls_table = """ CREATE TABLE IF NOT EXISTS urls (
                                        id integer PRIMARY KEY,
                                        short text NOT NULL,
                                        original text NOT NULL,
                                        count integer text,
                                        last_visit text
                                    ); """
        self.create_connection()
        self.execute_sql(sql_create_urls_table)
        print("Setup was successfully")
