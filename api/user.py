from http.server import BaseHTTPRequestHandler
from os.path import join


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open(join('data', 'file.txt'), 'r') as file:
            for line in file:
                self.wfile.write(line.encode())
        return
