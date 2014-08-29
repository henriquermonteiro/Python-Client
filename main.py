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
        self.view_ = view.View(self)
        self.view_.start()

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

    def notifyupdate(self, identifier, value):
        print(identifier + " updated!!")
        self.manager.getcompanie_id(identifier).price = value
        self.view_.updatevalues(identifier, value)

    def notifycompletion(self, operation):
        self.view_.notifycompletion(operation)

    

#Sei la ....
#    def updateview(self):


#Comunic chama o main para repassar para a view
    
if __name__ == "__main__":
    Controller()
