import time

import mysql

from common.config_load import SLEEP_TIME_FOR_MYSQL_START_SECONDS, LISTEN_SERVER_IP
from message_handler.server_message_handler import ContinuousServer
from db_handler.mysql_connector import MySQLConnector
from mysql.connector import Error
import mysql


def __main__():
    # ContinuousServer()

    print(f"sleeping for {SLEEP_TIME_FOR_MYSQL_START_SECONDS} seconds")
    time.sleep(SLEEP_TIME_FOR_MYSQL_START_SECONDS)

    db_connector = MySQLConnector(host=LISTEN_SERVER_IP, database='weather_data', user='admin', password='mysql')
    db_connector.connect()

    result = db_connector.execute_query("SHOW DATABASES;")
    print(result)
    db_connector.close()


if __name__ == "__main__":
    __main__()
