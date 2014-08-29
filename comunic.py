#import main
import model
import urllib.request as urllib2
import xml.dom.minidom as minidom

class Comunicacao:
    def __init__(self):
        self.url = 'http://localhost:8080/bolsa_web/rest/bolsa/'


    def request_addoperation(self, operation):
        ur = self.url + 'registrar'
        req = urlib2.Request(ur, data=operation.encodexml(), headers={'Content-Type': 'application/xml'})
        run = urllib2.urlopen(req)
        
        if run.status < 300:
            content = run.read()
            
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


    def request_listento(self, empresa, ip, port):
        ur = self.url + 'registrar'
        req = urlib2.Request(ur, data=(empresa.encodexml() + '<Reference><ip>'+ip + '</ip><port>' + port + '</port></Reference>'), headers={'Content-Type': 'application/xml'})
        run = urllib2.urlopen(req)
        
        if run.status < 300:
            content = run.read()

# Foi para server.py
#    def service_complete(self, operation):


#    def service_update(self, identifier, new_value):

        
