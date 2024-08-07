import http.server


class MessageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request from {self.client_address}")
        print(f"Path: {self.path}")
