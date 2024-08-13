import http.server

from data_processing.data_schema import DataSchema
from data_processing.data_split import DataSplit

from db_handler.mysql_writer import DbWriter


class MessageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        dat = DataSplit(self.path).get_data()
        schem = DataSchema(dat)
        schem.get_data()

        create_table_query = f"CREATE TABLE weather_data ({schem.get_sql_columns()});"

        db_writer = DbWriter()
        db_writer.create_table("weather_data", create_table_query)

        data_insert_query = f"INSERT INTO weather_data ({schem.get_write_columns()}) VALUES ({schem.get_write_values()});"
        print(data_insert_query)
        db_writer.write_data(data_insert_query)
        db_writer.close_connection()

    def get_received_data(self):
        return str(self.path)
