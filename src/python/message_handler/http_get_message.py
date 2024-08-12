import http.server

from data_processing.data_schema import DataSchema
from data_processing.data_split import DataSplit


class MessageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        dat = DataSplit(self.path).get_data()
        schem = DataSchema(dat)

        print(schem.get_data())

    def get_received_data(self):
        return str(self.path)
