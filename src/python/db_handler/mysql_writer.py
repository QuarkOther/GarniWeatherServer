import time

from common.config_load import LISTEN_SERVER_IP, LISTEN_SERVER_PORT
from db_handler.mysql_connector import MySQLConnector
from pyparsing import Empty


class DbWriter:

    def __init__(self):
        self.connection = MySQLConnector(host=LISTEN_SERVER_IP, database='weather_data', user='admin', password='mysql')
        self.connected = self.connection.connect()
        print(f"Connected to MySQL database on {LISTEN_SERVER_IP}:{LISTEN_SERVER_PORT}")

    def check_if_table_exists(self, table_name):
        tables_result = self.connection.execute_query(f"SHOW TABLES;")
        if tables_result.__sizeof__() > 0:
            for table in tables_result:
                return table.__contains__(table_name)
        else:
            print("None table found, creating table")
            return False


    def create_table(self, table_name, create_table_query):
        table_exists = self.check_if_table_exists(table_name)
        if not table_exists:
            result = self.connection.execute_query(create_table_query)
            print(f"create table query: {create_table_query}\nresult: ")
            print(result)

            sleep_time_seconds = 20
            print(f"sleep time {sleep_time_seconds}s after table creation")
            time.sleep(sleep_time_seconds)

            self.create_table(table_name, create_table_query)
        else:
            return True


    def write_data(self, insert_query):
        cursor = self.connection.cursor()
        cursor.execute(insert_query)
        return self.connected.commit()


    def close_connection(self):
        self.connection.close()
        print("Connection closed")