import http.server as server_http
import _thread
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

import random
import socket
import main
from model import Operacao

class Server():
    def __init__(self, main):
        self.main = main
        
        self.port = random.randint(7500, 8000)
        self.host = socket.gethostbyname(socket.gethostname())

        self.httpd = server_http.HTTPServer((self.host, self.port), Handler)
        
        _thread.start_new_thread(self.start, ())
    def start(self):
        print('Will call')
        self.httpd.serve_forever()
        print('Stop')
        
    

class Handler(server_http.BaseHTTPRequestHandler):
    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        return postvars
    
    def do_POST(self):
        print('Call Post')
        variables = self.parse_POST()
        if s.path == "/update/":
            self.main.notifyupdate(variables['id'], variables['value'])

        if s.path == "/complete/":
            op = Operacao(variables['id'], variables['compra'], variables['price'], variables['quantity'])
            self.main.notifycompletion(op)

    