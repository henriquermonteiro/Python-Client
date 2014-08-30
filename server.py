import http.server as server_http
import _thread
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

import random
import socket
import main
from model import Operacao

instance = None

# Classe para receber mensagens do server
class Server():
    
    # Inicializacao
    def __init__(self, main):
        self.main = main
        
        self.port = random.randint(7500, 8000)
        self.host = socket.gethostbyname(socket.gethostname())

        self.httpd = server_http.HTTPServer((self.host, self.port), Handler)
        
        global instance
        instance = main
        
        _thread.start_new_thread(self.start, ())
        
    # Inicia a thread
    def start(self):
        print('Will call')
        self.httpd.serve_forever()
        print('Stop')
        
# Classe de manipulacao do metodo POST
class Handler(server_http.BaseHTTPRequestHandler):
    
    # Preparacao de tipos de conteudo
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
    
    # Metodo para notificar opercao realizada e atualizacao de valores de uma acao
    def do_POST(self):
        print('Call Post')
 #       variables = self.parse_POST()
 #       print(variables)
        global instance
        if self.path.startswith("/update/"):
            fields = self.path.split(';')
            print(fields)
            instance.notifyupdate(fields[1].split("$")[1], fields[2].split("$")[1])
            
            self.send_response(200)

        if self.path.startswith("/complete/"):
            fields = self.path.split(';')
            print(fields)
            op = Operacao(fields[1].split('$')[1], fields[2].split('$')[1], fields[3].split('$')[1], fields[4].split('$')[1])
            instance.notifycompletion(op)
            
            self.send_response(200)

    