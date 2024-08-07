import socketserver

from common.config_load import SERVER_IP, SERVER_PORT
from message_receive.http_get_message import MessageHandler
from data_processing.data_split import DataSplit
from data_processing.data_schema import DataSchema


def __main__():
    """with socketserver.TCPServer((SERVER_IP, SERVER_PORT), MessageHandler) as httpd:
        print(f"Serving {SERVER_IP} on port {SERVER_PORT}")
        httpd.serve_forever()
    """
    testInput = (
        "/weatherstation/updateweatherstation.php?ID=01&PASSWORD=&action=updateraww&realtime=1&rtfreq=5&dateutc"
        "=now&baromin=29.90&tempf=81.8&dewptf=60.2&humidity=48&windspeedmph=1.5&windgustmph=1.5&winddir=300"
        "&rainin=0.0&dailyrainin=0.0&solarradiation=756.83&UV=5.9&indoortempf=78.4&indoorhumidity=54")

    dat = DataSplit(testInput)

    print(dat.get_data())

    schem = DataSchema(dat)
    print(schem)


if __name__ == "__main__":
    __main__()
