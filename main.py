import model
import server
import manager
import comunic
import view

class Controller:
    def __init__(self):
        self.manager = manager.DataManager()
        self.comunic = comunic.Comunicacao()
        print('start thread')
        self.server = server.Server(self)
        print('Server Started')
        print(self.server.host,' - ',self.server.port)
        self.view = view.View(self)

#view chama o main para repassar para comunic
    def addoperation(self, operation):
        operation.ip = self.server.host
        operation.port = self.server.port
        
        self.comunic.request_addoperation(operation)

    def listento(self, identifier):
        emp = self.manager.getcompanie_id(identifier)
        if(emp is None):
            emp = self.comunic.getcompany_id(identifier)
            
            self.manager.addcompany(emp)
            
        self.comunic.request_listento(emp, self.server.host, self.server.port)
        
        print(identifier)
        return emp

    def updatedlist(self):
        return self.comunic.request_companieslist()


#Sei la ....
#    def updateview(self):


#Comunic chama o main para repassar para a view
    def notifyupdate(self, identifier, value):
        self.view.updatevalues(identifier, value)

    def notifycompletion(self, operation):
        self.view.notifycompletion(operation)

    
if __name__ == "__main__":
    Controller()
