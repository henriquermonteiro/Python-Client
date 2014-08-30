import model
import server
import manager
import comunic
import view

class Controller:
    # Inicializacao
    def __init__(self):
        self.manager = manager.DataManager()
        self.comunic = comunic.Comunicacao()
        print('start thread')
        self.server = server.Server(self)
        print('Server Started')
        print(self.server.host,' - ',self.server.port)
        self.view_ = view.View(self)
        self.view_.start()

    # Registra uma nova operacao de compra ou venda
    def addoperation(self, operation):
        operation.ip = self.server.host
        operation.port = self.server.port
        
        self.comunic.request_addoperation(operation)

    # Metodo que registra um novo ouvinte a uma determinada empresa
    def listento(self, identifier):
        emp = self.manager.getcompanie_id(identifier)
        if(emp is None):
            emp = self.comunic.getcompany_id(identifier)
            
            self.manager.addcompany(emp)
            
        self.comunic.request_listento(emp, self.server.host, self.server.port)
        
        print(identifier)
        return emp

    # Atualiza a lista das empresas
    def updatedlist(self):
        return self.comunic.request_companieslist()

    # Recebe notificacao de atualizacao dos valores da acao de uma empresa
    def notifyupdate(self, identifier, value):
        print(identifier + " updated!!")
        self.manager.getcompanie_id(identifier).price = value
        self.view_.updatevalues(identifier, value)

    # Recebe notificacao de operacao realizada
    def notifycompletion(self, operation):
        self.view_.notifycompletion(operation)


# Inicializacao
    
if __name__ == "__main__":
    Controller()
