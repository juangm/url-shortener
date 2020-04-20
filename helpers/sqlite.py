import datetime
import sqlite3
import termtables


class Sqlite3Helper:

    _DB = "sqlite/url-short.db"

    def __init__(self):
        self.conn = None

    def _create_connection(self):
        """ Create DB connection to SQLite DB """
        try:
            self.conn = sqlite3.connect(self._DB)
            return self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def _execute_sql(self, sql_statement):
        """ execute sql statement in
        :sql_statement sql statement to be executed
        """
        try:
            c = self.conn.cursor()
            c.execute(sql_statement)
            return c
        except sqlite3.Error as e:
            print(e)

    def setup_db(self):
        """ Create a table and delete previous data if table was created """
        sql_create_urls_table = """ CREATE TABLE IF NOT EXISTS urls (
                                        id integer PRIMARY KEY,
                                        short text NOT NULL,
                                        original text NOT NULL,
                                        count integer NOT NULL,
                                        last_visit text NOT NULL
                                    ); """
        self._create_connection()
        self._execute_sql(sql_create_urls_table)
        self.conn.commit()
        # Delete all the values in case table contains already some values
        self._execute_sql("DELETE FROM urls")
        self.conn.commit()
        print("Setup was successfully")

    def search_url(self, url_to_search):
        """ Search for an original url in the DB """
        sql_search_url = "SELECT * FROM urls WHERE original = '{}';"
        self._create_connection()
        cursor = self._execute_sql(sql_search_url.format(url_to_search))
        url_row = cursor.fetchall()
        if len(url_row) > 1:
            raise AssertionError("Not possible to have same url in DB")
        return list(url_row[0]) if len(url_row) == 1 else []

    def search_short_path(self, short_path):
        """ Search for an original url in the DB """
        sql_search_url = "SELECT * FROM urls WHERE short = '{}';"
        self._create_connection()
        cursor = self._execute_sql(sql_search_url.format(short_path))
        url_row = cursor.fetchall()
        if len(url_row) > 1:
            raise AssertionError("Not possible to have same url in DB")
        return list(url_row[0]) if len(url_row) == 1 else []

    def count_urls_stored(self):
        sql_count_total = "SELECT COUNT(*) FROM urls;"
        self._create_connection()
        cursor = self._execute_sql(sql_count_total)
        return list(cursor.fetchone())[0]

    def update_short_url(self, short_url):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_update_count = """UPDATE urls
                              SET count = count + 1 ,
                                last_visit = '{}'
                              WHERE short = '{}'"""
        self._create_connection()
        self._execute_sql(sql_update_count.format(now, short_url))
        self.conn.commit()

    def input_new_url(self, original_url, short_path):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_input_new = """INSERT INTO urls(short,original,count,last_visit)
                           VALUES('{}','{}',0, '{}');"""
        self._create_connection()
        cursor = self._execute_sql(
            sql_input_new.format(short_path, original_url, now))
        self.conn.commit()
        print("Added url {} to DB".format(original_url))

    def admin_get_all_urls(self):
        sql_display_urls = "SELECT * FROM urls ORDER BY count DESC;"
        self._create_connection()
        cursor = self._execute_sql(sql_display_urls)
        headers = ["id", "short", "original", "count", "last_visit"]
        # Convert the row values into list
        all_values = cursor.fetchall()
        data = [list(x) for x in all_values] if all_values != [] else [
            ["", "", "", "", ""]]
        termtables.print(data, header=headers, alignment='c')

    def update_latest_visit(self, original_url):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_replace_url = """UPDATE urls
                             SET count = 0 ,
                               original = '{}',
                               last_visit = '{}'
                             ORDER BY last_visit ASC LIMIT 1;"""
        self._create_connection()
        cursor = self._execute_sql(sql_replace_url.format(original_url, now))
        self.conn.commit()
        # Check update was performed
        return self.search_url(original_url)
