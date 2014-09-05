#import main
import model
import urllib.request as urllib2
import xml.dom.minidom as minidom
import http.client as httplib

# Classe de comunicação do o Servidor
class Comunicacao:
    def __init__(self):
      #  self.host = 'http://localhost:8084'
        self.host = 'http://localhost:8080'
        self.path = '/bolsa_web/rest/bolsa/'
        
        self.url = self.host+self.path

    # Envio de requisição de transação
    def request_addoperation(self, operation):
     
        ur = self.url + 'registrar'
        
    #    conn = httplib.HTTPConnection('127.0.0.1:8084')
        conn = httplib.HTTPConnection('127.0.0.1:8080')
        XML = operation.encodexml()
        headers = {"Content-type": "application/xml"}
        conn.request("POST", self.path+'registrar', XML, headers)
        print(XML)
       # conn.send(bytes(XML, 'UTF-8'))
        
        run = conn.getresponse()
        
        print(run.status)
            
    # Envio de requisição de recuperação dos dados de uma empresa        
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
        
    # Envio de requisição de todas as empresas
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

    # Envio de requisição de monitoramento dos valores das ações de uma empresa
    def request_listento(self, empresa, ip, port):
        ur = self.url + 'escutar'
        
    #    conn = httplib.HTTPConnection('127.0.0.1:8084')
        conn = httplib.HTTPConnection('127.0.0.1:8080')
        XML = ('<wrapper>' + empresa.encodexml() + '<reference><ip>'+ip + '</ip><port>' + str(port) + '</port></reference></wrapper>')
        headers = {"Content-type": "application/xml"}
        conn.request("POST", self.path+'escutar', XML, headers)
        print(XML)
       # conn.send(bytes(XML, 'UTF-8'))
        
        run = conn.getresponse()
        
        print(run.status)
        
