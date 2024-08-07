import http.server


class message_handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request from {self.client_address}")
        print(f"Path: {self.path}")
