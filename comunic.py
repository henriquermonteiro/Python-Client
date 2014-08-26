import main
import model
import urllib
import urllib2

class Comunicacao:
    def __init__(self):
        self.url = '127.0.0.1'


    def request_addoperation(self, operation):


    def request_companieslist(self):
        url = self.url + '/get_companies'
        response = urllib2.urlopen(url)


    def request_listento(self, empresa):
        

    def service_complete(self, operation):


    def service_update(self, identifier, new_value):

        
