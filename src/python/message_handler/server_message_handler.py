import socketserver

from common.config_load import LISTEN_SERVER_IP, LISTEN_SERVER_PORT
from message_handler.http_get_message import MessageHandler


class ContinuousServer:
    def __init__(self):
        with socketserver.TCPServer((LISTEN_SERVER_IP, LISTEN_SERVER_PORT), MessageHandler) as httpd:
            print(f"Serving {LISTEN_SERVER_IP} on port {LISTEN_SERVER_PORT}")
            httpd.serve_forever()
