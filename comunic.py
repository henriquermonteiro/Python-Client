#import main
import model
import urllib.request as urllib2
import xml.dom.minidom as minidom
import http.client as httplib

# Classe responsavel pelas comunicacoes
class Comunicacao:
    
    # Inicializacao com o caminho URL do server
    def __init__(self):
        self.host = 'http://localhost:8080'
        self.path = '/bolsa_web/rest/bolsa/'
        
        self.url = self.host+self.path

    # Requisicao para registrar uma nova operacao de compra ou venda
    def request_addoperation(self, operation):
        ur = self.url + 'registrar'
        req = urllib2.Request(ur, data=operation.encodexml(), headers={'Content-Type': 'application/xml'})
        run = urllib2.urlopen(req)
        
        if run.status < 300:
            content = run.read()
            
    # Requisicao para retornar uma empresa cadastrada no servidor, atraves do seu ID
    def getcompany_id(self, ide):
        url = self.url + ide
        response = urllib2.urlopen(url)
        
        if response.status < 300:
            content = response.read()
        
            xml = minidom.parseString(content)
            
            empresas = xml.getElementsByTagName("empresa")
            
            if empresas.length > 0:
                emp = empresas.pop()
                
                aux = emp.childNodes.pop()
            
                price = aux.childNodes.pop().nodeValue
            
                aux = emp.childNodes.pop()
                
                name = aux.childNodes.pop().nodeValue
                
                aux = emp.childNodes.pop()
                
                ide = aux.childNodes.pop().nodeValue
                
                r_emp = model.Empresa(name, ide, price)
                
                return r_emp
        
        return None
        
    # Requisicao da lista de empresas disponiveis no server
    def request_companieslist(self):
        url = self.url + 'lista'
        response = urllib2.urlopen(url)
        
        if response.status < 300:
            content = response.read()
            
            xml = minidom.parseString(content)
            
            empresas = xml.getElementsByTagName("empresa")
            
            empresaarray = {}
            
            while empresas.length > 0:
                emp = empresas.pop()
                
                aux = emp.childNodes.pop()
                
                price = aux.childNodes.pop().nodeValue
                
                aux = emp.childNodes.pop()
                
                name = aux.childNodes.pop().nodeValue
                
                aux = emp.childNodes.pop()
                
                ide = aux.childNodes.pop().nodeValue
                
                r_emp = model.Empresa(name, ide, price)
                
                empresaarray[r_emp.getid()] = r_emp
                
            
            return empresaarray
        
        return {}

    # Requisicao que registra um novo ouvinte a uma determinada empresa
    def request_listento(self, empresa, ip, port):
        ur = self.url + 'escutar'
        
        conn = httplib.HTTPConnection('127.0.0.1:8080')
        XML = ('<wrapper>' + empresa.encodexml() + '<reference><ip>'+ip + '</ip><port>' + str(port) + '</port></reference></wrapper>')
        headers = {"Content-type": "application/xml"}
        conn.request("POST", self.path+'escutar', XML, headers)
        print(XML)
       # conn.send(bytes(XML, 'UTF-8'))
        
        run = conn.getresponse()
        
        print(run.status)
        
        #req = urllib2.Request(ur, data=().encode(encoding='UTF-8'), headers={'Content-Type': 'application/xml'})
     #   run = urllib2.urlopen(req)
        
     #   if run.status < 300:
     #       content = run.read()

# Foi para server.py
#    def service_complete(self, operation):


#    def service_update(self, identifier, new_value):

        
