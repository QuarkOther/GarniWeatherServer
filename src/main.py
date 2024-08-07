import socketserver

from common.config_load import SERVER_IP, SERVER_PORT
from message_receive.http_get_message import message_handler


def __main__():
    with socketserver.TCPServer((SERVER_IP, SERVER_PORT), message_handler) as httpd:
        print(f"Serving {SERVER_IP} on port {SERVER_PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    __main__()
