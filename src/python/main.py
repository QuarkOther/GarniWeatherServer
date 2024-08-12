import time

import mysql

from common.config_load import SLEEP_TIME_FOR_MYSQL_START_SECONDS
from message_handler.server_message_handler import ContinuousServer
from db_handler.mysql_connector import MySQLConnector
from mysql.connector import Error
import mysql


def __main__():
    # ContinuousServer()

    print(f"sleeping for {SLEEP_TIME_FOR_MYSQL_START_SECONDS} seconds")
    time.sleep(SLEEP_TIME_FOR_MYSQL_START_SECONDS)

    db_connector = MySQLConnector(host='localhost', database='weather_data', user='admin', password='mysql')

    try:
        db_connector.connect()
    except Exception as e:
        print(f"Connection failed: {e}")

    try:
        result = db_connector.execute_query("SHOW DATABASES;")
        for row in result:
            print(row)
    except Error as e:
        print(f"Query failed: {e}")
    finally:
        db_connector.close()


if __name__ == "__main__":
    __main__()
