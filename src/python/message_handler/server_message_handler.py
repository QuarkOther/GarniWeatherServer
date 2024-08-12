import socketserver

from common.config_load import SERVER_IP, SERVER_PORT
from message_handler.http_get_message import MessageHandler


class ContinuousServer:
    def __init__(self):
        with socketserver.TCPServer((SERVER_IP, SERVER_PORT), MessageHandler) as httpd:
            print(f"Serving {SERVER_IP} on port {SERVER_PORT}")
            httpd.serve_forever()
